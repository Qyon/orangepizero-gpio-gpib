ifneq ($(LINUXINCLUDE),)
	LINUXINCLUDE := -I$(GPIB_TOP_DIR)/compat/include $(LINUXINCLUDE)
endif

subdir-ccflags-y := -I$(src)/include \
			-DHAVE_DEV_OF_NODE=$(HAVE_DEV_OF_NODE) \
			-DGPIB_CONFIG_KERNEL_DEBUG=$(GPIB_CONFIG_KERNEL_DEBUG)


obj-y += sys/
obj-y += raspi_gpib/

