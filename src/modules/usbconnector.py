# Felix Sonnleitner, 25.12.2017
# Python 3.6
# Module used to get connected devices

import platform

from time import sleep
from datetime import datetime
from subprocess import PIPE, Popen

from src.modules.logmod import Logger


class USBConnector:
    """This class is used to find connected USB devices"""

    def __init__(self, timeout=120, wait=1):
        """
        :param timeout: int
                  timeout for the get_connected function. If <= 0 there is no timeout
               wait: int
                  waiting time for the check for devices
        """
        self.log = Logger()

        self.timeout     = timeout # timeout for the get_connected function. If <= 0 there is no timeout
        self.wait        = wait    # waiting time for the check for devices
        self.devices     = []
        self.prevDevices = []      # stores alls devices which were connected before the USB devices is connected
        self.HD          = None

        self.sys           = platform.system()
        self.MACSYSTEM     = "Darwin"
        self.WINDOWSSYSTEM = "Windows"


    #################################################################################

    def get_devices(self):
        return self.devices

    #################################################################################

    def get_HD(self):
        return self.HD

    #################################################################################

    def get_connected(self):
        begin = datetime.now().timestamp()

        while(True):
            self.log.write_to_log("INFO: Waiting for USB Device to be connected......")
            self.devices = self._find_devices()

            if self.devices is False:
                self.log.write_to_log("ERROR: Exception of usbconnector._find_devices()")
                return False

            if self.devices is False:
                self.log.write_to_log("ERROR: Exception of usbconnector._find_devices()")
                return False

            now = datetime.now().timestamp()

            if self.timeout > 0:
                if int(now - begin) >= self.timeout:
                    self.log.write_to_log("ERROR: Timeout! No USB Device got connected in time")
                    return False

            if self.devices:
                return True

            sleep(self.wait)

    #################################################################################

    def wait_device_disconnected(self, device):

        while(True):
            self.log.write_to_log("INFO: Waiting for USB Device {device} to be disconnected".format(device=device))
            connected_devices = self._find_devices()

            if device not in connected_devices:
                self.devices = []
                break

            sleep(self.wait)

    #################################################################################

    def get_prev_devices(self):
        """
        NOTE: This function gets the list of the already connected devices
        """
        devices_path = []

        if self.sys == self.MACSYSTEM:
            list = self._cmdline('ls /Volumes')
            devices = list.splitlines()

        elif self.sys == self.WINDOWSSYSTEM:
            dir = self._cmdline('fsutil fsinfo drives')
            devices = dir.split(" ")
            devices = devices[1:-1]


        self.log.write_to_log("-----------BEGIN: LIST OF AREADY CONNECTED DEVICES-----------")
        for dev in devices:
            self.log.write_to_log(dev, timestamp=False)
            devices_path.append(dev)

        self.log.write_to_log("------------END: LIST OF AREADY CONNECTED DEVICES------------")

        self.prevDevices = devices_path

    #################################################################################

    def _find_devices(self):
        try:
            if self.sys == self.MACSYSTEM:
                ls = self._cmdline('ls /Volumes')
                return self._parse_devices(ls)
            elif self.sys == self.WINDOWSSYSTEM:
                dir = self._cmdline('fsutil fsinfo drives')
                return self._parse_devices(dir)

        except:
            self.log.write_to_log("ERROR: No USB device connected")
            return False

    #################################################################################

    def _cmdline(self, command):
        """
        :param command: string
                    The console command which should be executed
        :return: string utf-8
                    The console output of the command
        """
        process = Popen(
            args=command,
            stdout=PIPE,
            shell=True
        )
        return process.communicate()[0].decode("utf-8")

    #################################################################################

    def _parse_devices(self, list):
        """
        :param list: string
                    contains all devices with the linebreak
        :return: the list of all usb devices
        """
        devices_path = []

        if self.sys == self.MACSYSTEM:
            devices = list.splitlines()
            self.HD = "Macintosh HD"
            devices.remove("Macintosh HD")
            for prevDev in self.prevDevices:
                if prevDev in devices:
                    devices.remove(prevDev)

            for dev in devices:
                devices_path.append("/Volumes/" + dev)

        elif self.sys == self.WINDOWSSYSTEM:
            devices = list.split(" ")
            self.HD = "C:\\"
            devices.remove("C:\\")
            devices = devices[1:-1]

            for prevDev in self.prevDevices:
                if prevDev in devices:
                    devices.remove(prevDev)

            for dev in devices:
                devices_path.append(dev)

        return devices_path

#EOF
