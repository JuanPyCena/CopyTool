# CopyTool
Python Tool to copy files from a USB stick to a predefined directory on the pc

Python version:
Python 3.6

Required Python modules:
os, shutil, subprocess, guizero, datetime, time, platform  


# How to install
* If you do not have git installed yet you can do that here for:
  * macOS -> [GIT for MAC](https://sourceforge.net/projects/git-osx-installer/files/latest/download)
  * Windows -> [GIT for Windows](https://github.com/git-for-windows/git/releases/download/v2.15.1.windows.2/Git-2.15.1.2-64-bit.exe)
#### Via the console:  
* Open a shell and navigate to the desired installation directory
* Enter: *git clone --recursive https://github.com/JuanPyCena/CopyTool.git*

#### Via the GUI:
* Download the repository as a *ZIP* via the green <span style="color:green"> *Clone or Download* </span> button.
* Copy the *ZIP-file* to your desired installation directory, and *extract* it there.

#### On Mac:
* In the shell run the [installCopyToolMac.sh](installCopyToolMac.sh).

#### On Windows:
* First you must download [Python 3.6 64bit](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe). (_If your system is not 64bit you should use this link [Python 3.6 32bit](https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe)_)
* After installing **Python 3.6** execute the [installRequiredPythonPackages.sh](installRequiredPythonPackages.sh) script to install all required pacakes

# How to use the CopyTool

* To use the copy tool you must start [CopyTool](CopyTool.py) by double clicking the file, or running the script from the console.
* The program starts and waits for a USB device to be connected.
* After a USB device has been connected a dialog window is shown, and you are asked to enter a directory name (**NOTE: DIALOG LANGUAGE: GERMAN**)
  * The USB device must have a folder named _DCIM_, since this is the files structure of a digital camera. 
  Only the files from this directory will be copied.
* The directory is created in _Pictures_ on your PC
* It is possible to delete the files from the USB after copying the files from the USB via the dialog
* The program start copying after closing the dialog window.
* You will get another dialog window when the copying is done.
* The pogram exits after closing all of its windows.
* *NOTE:The program creates *log-files* in the directory *log*. This will be created in the **CopyTool** folder.*

# Modification
* Please feel free to enter modifications into the [modification](https://github.com/JuanPyCena/CopyTool/tree/public_modification_branch) branch.
* Continuos improvement is very important to keep the software relevant.
