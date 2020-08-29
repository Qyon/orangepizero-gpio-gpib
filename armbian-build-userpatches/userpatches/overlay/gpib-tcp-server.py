#!/usr/bin/python2.7
# coding=utf-8
__author__ = 'Qyon'

import sys
import SocketServer
import argparse
import logging
import Gpib
from multiprocessing import Process

logger = logging.getLogger('GPIBTCPSever')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class GPIBTCPSeverHandler(SocketServer.StreamRequestHandler):
    timeout = 0.01

    def __init__(self, request, client_address, server):
        SocketServer.StreamRequestHandler.__init__(self, request, client_address, server)
        self.instrument = None

    def handle(self):
        logger.info("New connection %s" % (self.client_address[0], ))

        assert isinstance(self.server, GPIBTCPSever)
        logger.debug("Opening instrument %d" % (self.server.dev_id,))
        self.instrument = Gpib.Gpib(0, self.server.dev_id)

        while True:
            try:
                self.data = self.rfile.readline().strip()
                if not self.data:
                    return
            except Exception as e:
                self.data = None

            if self.data:
                logger.debug("T(%s)> %s..." % (self.client_address[0], self.data[:30]))

                logger.debug("G(%d)< %s..." % (self.server.dev_id, self.data[:10]))
                self.instrument.write(self.data)

            iread_data = self.instrument.read(1000)

            if iread_data:
                logger.debug("G(%d)> %s" % (self.server.dev_id, iread_data[:10]))

                logger.debug("T(%s)< %s" % (self.client_address[0], iread_data[:10]))
                self.wfile.write(iread_data)

    def finish(self):
        logger.info("Connection %s closed" % (self.client_address[0], ))

        if self.instrument:
            self.instrument.close()


class GPIBTCPSever(SocketServer.TCPServer):
    def __init__(self, dev_id, tcp_port):
        self.tcp_port = tcp_port
        self.dev_id = dev_id
        logger.info("Initializing GPIB TCP Server on port %d for device %d" % (self.tcp_port, self.dev_id))
        SocketServer.TCPServer.__init__(self, ("0.0.0.0", self.tcp_port), GPIBTCPSeverHandler)

    def run(self):
        self.serve_forever()


def server_process(port, gpib_address):
    server = GPIBTCPSever(dev_id=gpib_address, tcp_port=port)
    server.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--tcp-port-base", help="TCP Port Base (dest port = base + gpib address)", type=int, required=True)
    args = parser.parse_args()
    for gpib_address in range(1, 30):
        tcp_port = gpib_address + args.tcp_port_base
        p = Process(target=server_process, args=(tcp_port, gpib_address))
        p.start()



