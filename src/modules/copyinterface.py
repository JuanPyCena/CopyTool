# Felix Sonnleitner, 25.12.2017
# Python 3.6
# Module used to copy files from a device to a location

import os
from shutil import copy2
from subprocess import PIPE, Popen
import platform

from src.modules.logmod import Logger

class CopyInterface:
    """This class is used to create an interface between the USB devices and the PC"""

    def __init__(self, connector=None, device=None, destination=None, delete_after_copy=False):
        self.log       = Logger()
        self.connector = connector
        self.device    = device
        self.HD        = self.connector.get_HD()

        self.usb_directories   = None
        self.destination       = destination
        self.delete_after_copy = delete_after_copy
        self.sys               = platform.system()
        self.WINDOWSSYSTEM     = "Windows"

        if self.sys == self.WINDOWSSYSTEM:
            self.src           = str(self.device) + "DCIM\\"
        else:
            self.src           = str(self.device) + "/DCIM/"

        self.list = self.get_list_of_files_in_src(self.src)

    #################################################################################

    def copy_file_from_usb_to_HD(self):
        for l in self.list:
            try:
                src = str(self.src) + l
                if os.path.isfile(src):
                    copy2(src, self.destination)
                    self.log.write_to_log("SUCCESS: Copying " + l + " to " + self.destination)
                else:
                    self.log.write_to_log("INFO: {l} was not copied. {l} is a directory".format(l=src))
            except:
                self.log.write_to_log("ERROR: Could not copy " + l + " to " + self.destination)
                return False

        return True

    #################################################################################

    def remove_files_from_source(self):
        for l in self.list:
            try:
                src = str(self.src) + l
                if os.path.isfile(src):
                    os.remove(src)
                    self.log.write_to_log("SUCCESS: Removed " + l + " from USB device")
                else:
                    self.log.write_to_log("INFO: {l} was not removed. {l} is a directory".format(l=src))
            except:
                self.log.write_to_log("ERROR: Could not remove " + l + " from USB device")
                return False

        return True

    #################################################################################

    def destination_directory_exists(self, dir="/Volumes/Macintosh HD/Users/SunnyMOD/Pictures/destination"):
        """
        :param dir: string
                    Defines the directory where the files should be copied to
                    Default: ~/Pictures/destination
        :return: bool
                    Returns True if the directory already exists. Otherwise it tries to create the directory.
                    If this fails False is returned.
        """

        if os.path.exists(dir):
            return True

        try:
            self._cmdline("mkdir {dir}".format(dir=dir))
            self.log.write_to_log("INFO: " + dir + " not found. Creating this directory to start copying")
            return True
        except:
            self.log.write_to_log("ERROR: Could not create directory " + dir)
            return False

    #################################################################################

    def get_list_of_files_in_src(self, src):
        """
        :param src: string
                    The absoute path of the source directory
        :return: list of string
                    Return all elements in the source path as a list of string
        """

        list = []

        if self.sys == self.WINDOWSSYSTEM:
            list = os.listdir(src)

        else:
            ls = self._cmdline("ls {src}".format(src=src))
            word = ""
            for l in ls:
                if l == "\n":
                    list.append(word)
                    word = ""
                else:
                    word = word + l


        self.log.write_to_log("--------------------------BEGIN: LIST TO COPY--------------------------")

        for l in list:
            self.log.write_to_log(l, timestamp=False)

        self.log.write_to_log("---------------------------END: LIST TO COPY---------------------------")

        return list

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

#EOF