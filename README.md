# CopyTool
Python Tool to copy files from a USB stick to a predefined directory on the pc

Python version:
Python 3.6

Required Python modules:
os, shutil, subprocess, guizero, datetime, time, platform  


# How to install
* Open a shell and go to the desired installation directory
* Enter: *git clone --recursive https://github.com/JuanPyCena/CopyTool.git*

#### On Mac:
* In the shell run the [installCopyToolMac.sh](installCopyToolMac.sh).

#### On Windows:
* First you must download [Python 3.6 64bit](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe). (_If your system is not 64bit you should use this link [Python 3.6 32bit](https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe)_)
* After installing **Python 3.6** execute the [installRequiredPythonPackages.sh](installRequiredPythonPackages.sh) script to install all required pacakes

# How to use the CopyTool

* To use the copy tool you must start [CopyTool](CopyTool.py) by double clicking the file, or running the script from the console.
* The program starts and waits for a USB device to be connected.
* After a USB device has been connected a dialog window is shown, and you are asked to enter a directory name (**NOTE: DIALOG LANGUAGE: GERMAN**)
  * The USB device must have a floder named _DCIM_, since this is the files structure of a digital camera. 
  Only the files from this directory will be copied.
* The directory is created in _Pictures_ on your PC
* It is possible to delete the files from the USB after copying the files from the USB via the dialog
* The program start copying after closing the dialog window.
* You will get another dialog window when the copying is done.
* The pogram exits after closing all of its windows.
* *NOTE:The program creates *log-files* in the directory *log*. This will be created in the **CopyTool** folder.*
