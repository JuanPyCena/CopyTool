# Felix Sonnleitner, 27.12.2017
# Python 3.6
# This module is used to create and use a small dialog window

from guizero import App, Text, TextBox, CheckBox, PushButton, info, warn
from logmod import Logger

class GUI:

    def __init__(self, info=False):
        """
        :param info: bool
                    Defines if an additional Infobox is shown
        """
        self.log           = Logger()
        self.info          = info
        self.dir           = ""
        self.delete_on_usb = False

        self.app = None
        self.main_window()

    #################################################################################

    def main_window(self):
        try:
            self.app = App(title="Bilder kopieren", width=1200, height=400)
            welcome = Text(self.app, "Wilkommen in der Bilder Kopier App.", size=20)
            enter = Text(self.app,
                         "Gib bitte im Feld unten den Namen des Ordners ein in dem du deine Bilder kopieren möchtest. "
                         "\n (Wenn es diesen Ordner noch nicht gibt wird er für dich unter \"Bilder\" erstellt) "
                         "\n"
                         "\nDanach wähle aus ob die Bilder von dem USB-Stick gelöscht werden sollen. "
                         "\nWenn du die Bilder vom USB Stick löschen möchtest mach ein Häckchen bei: "
                         "\n    \"Bilder nach dem Kopieren löschen...?\"     "
                         "\n"
                         "\nBestätige anschließend  deine Eingabe mit den Knopf BESTÄTIGEN", size=18)

            dir = TextBox(self.app, width=80)
            checkbox = CheckBox(self.app, text="Bilder nach dem Kopieren löschen...?")
            OK = PushButton(self.app, text="BESTÄTIGEN", command=info,
                            args=["INFO", "Die Bilder werden kopiert sobald du das Fenster geschlossen hast. \nDu kannst nun das Fenster schließen"])

            if self.info:
                inf = info("INFORMATION", "Gib bitte im Feld unten den Namen deines Ordners ein. "
                                          "\n"
                                          "\nDanach wähle aus ob die Bilder von dem USB-Stick gelöscht werden sollen. "
                                          "\nWenn du die Bilder vom USB Stick löschen möchtest mach ein Häckchen bei: "
                                          "\n    \"Bilder nach dem Kopieren löschen...?\"     "
                                          "\n"
                                          "\nBestätige anschließend deine Eingabe mit den Knopf \"BESTÄTIGEN\"",
                           size=18)

            self.app.focus()
            self.app.display()

            self.dir = dir.get()
            self.log.write_to_log("INFO: The directory in which the files should be copied to is " + self.dir,
                                  consoleOutput=True)

            if checkbox.get_value() == 1:
                self.log.write_to_log("INFO: The copied files will be removed from the usb device", consoleOutput=True)
                self.delete_on_usb = True

        except:
            self.log.write_to_log("ERROR: The main window has failed", consoleOutput=True)

    #################################################################################

    def finished_window(self):
        info(title="Bilder kopieren fertig!!", text="Alle Bilder wurden nach {destination} kopiert.".format(destination=self.dir))

    #################################################################################

    def error_window(self):
        warn(title="Bilder kopieren fehlgeschlagen!!", text="Bilder wurden nicht kopiert!!!".format(destination=self.dir))

    #################################################################################

    def finished_removing_window(self):
        info(title="Bilder löschen fertig!!",
             text="Alle Bilder wurden vom USB Stick gelöscht.")

    #################################################################################

    def error_removing_window(self):
        warn(title="Bilder löschen fehlgeschlagen!!",
             text="Bilder wurden nicht vom USB Stick gelöscht!!!")

    #################################################################################

    def get_dir(self):
        """
        :return: string
                    The entered name for the Directory
        """
        return self.dir

    #################################################################################

    def get_delete_on_usb(self):
        """
        :return: bool
                    Defines if the files should be deleted on the USB device
        """
        return self.delete_on_usb

#EOF