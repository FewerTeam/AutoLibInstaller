# AutoLibInstaller
A simple Python 3 librairie that auto install librairies if there are not installed.
# Install
You have to download the project on GitHub and add it to the project.
# How to use
At the beginning of a project : 


"""Imports"""
from ALI import ALI
firstlib = ALI("time")
time = firstlib.auto()

if the lib is already installed, it will be imported. Else, it will be downloaded with pip then imported.
You can now use for example

time.sleep(5)