# Felix Sonnleitner, 25.12.2017
# Python 3.6

import copyinterface
import usbconnector
import gui

from logmod import Logger

DESTINATION = "/Users/SunnyMOD/Pictures/"
TIMEOUT     = 0

def run():

    # start logging
    log = Logger()
    log.write_to_log("---------------------STARTING UP---------------------", consoleOutput=True)

    # create usbconnector
    connector = usbconnector.USBConnector(timeout=TIMEOUT, wait=1)

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
        dialog = gui.GUI(info=False)
        destination = dialog.get_dir()
        delete_after_copying = dialog.get_delete_on_usb()

        # create the copy interface
        interface = copyinterface.CopyInterface(connector=connector,
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

        # Wait for the device to be disconnected again if the program does not have a timeout.

        log.write_to_log("INFO: Copying done! Stop the program after "
                         "the device {device} has been disconnected".format(device=connected_devices[0]), consoleOutput=True)
        connector.wait_device_disconnected(device=connected_devices[0])

    else:
        log.write_to_log("INFO: Nothing connected.... Nothing to do ......", consoleOutput=True)

    log.write_to_log("--------------------SHUTTING DOWN--------------------", consoleOutput=True)

#################################################################################

if __name__ == "__main__":
    run()

#EOF