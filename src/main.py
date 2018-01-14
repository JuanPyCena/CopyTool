# Felix Sonnleitner, 25.12.2017
# Python 3.6

import os
import platform

from src.modules.copyinterface import CopyInterface
from src.modules.usbconnector import USBConnector
from src.modules.gui import GUI
from src.modules.logmod import Logger


def run():

    user = os.getlogin()
    # Edit DESTINATION to define your parent directory
    if platform.system() == "Windows":
        DESTINATION = "C:\\Users\\{user}\\Pictures\\".format(user=user)
    if platform.system() == "Darwin":
        DESTINATION = "Users/{user}/Pictures/".format(user=user)

    TIMEOUT = 300
    WAIT    = 1

    # start logging
    log = Logger()
    log.write_to_log("---------------------STARTING UP---------------------", consoleOutput=True)

    # create usbconnector
    connector = USBConnector(timeout=TIMEOUT, wait=WAIT)

    # delete logfiles that are older then one day
    if log.delete_old_logfiles():
        log.write_to_log("INFO: Old logfile removed", consoleOutput=True)

    # get connection
    if connector.get_connected():
        log.write_to_log("SUCCESS: Devices connected:", consoleOutput=True)
        connected_devices = connector.get_devices()

        # log the connected devices and select the first one in the list
        # as the devices from which the files should be copied from
        log.write_to_log("---------------------BEGIN: LIST OF DEVICES----------------------")
        for dev in connected_devices:
            log.write_to_log(dev, timestamp=False)
        log.write_to_log("----------------------END: LIST OF DEVICES-----------------------")
        log.write_to_log("INFO: First Device will be selected: " + connected_devices[0])
        log.write_to_log("Proceeding")

        # GUI for entereing the destination directory
        dialog = GUI(info=False)
        destination = dialog.get_dir()
        delete_after_copying = dialog.get_delete_on_usb()

        # create the copy interface
        interface = CopyInterface(connector=connector,
                                  device=connected_devices[0],
                                  destination=str(DESTINATION + destination),
                                  delete_after_copy=delete_after_copying)

        # copy the files to the destination given by the GUI dialog.
        # checks if the destination was defined and if it is available.
        if destination != "":
            if interface.destination_directory_exists(str(DESTINATION + destination)):
                if interface.copy_file_from_usb_to_HD():
                    dialog.finished_window()
            else:
                dialog.error_window()
        else:
            dialog.error_window()

        # delete the files from the usb device if this is wished.
        if delete_after_copying is True:
            if interface.remove_files_from_source():
                dialog.finished_removing_window()
            else:
                dialog.error_removing_window()

    else:
        log.write_to_log("INFO: Nothing connected.... Nothing to do ......", consoleOutput=True)

    log.write_to_log("--------------------SHUTTING DOWN--------------------", consoleOutput=True)


#EOF
