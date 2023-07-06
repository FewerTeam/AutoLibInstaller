"""This file contain the class for this lib"""

try:
    import os
except ModuleNotFoundError:
    print("You need the os librairie !")
    exit(-1)
    
#Class

class ALI(object):
    def __init__(self, lib:str, log=True):
        self.log = log
        self.lib = lib
        
    def auto(self):
        """return the imported lib"""
        if self.check_installed():
            return self.import()
        else:
            self.install()
            return self.import
        
    def check_installed(self):
        """check if the lib is installed"""
        try:
            self.import()
            return True
        except ModuleNotFoundError:
            self.install()
            try:
                self.import()
                return False
            except:
                raise RuntimeError("something when wrong")
        
    def import(self):
        """import the lib"""
        with open("a.py, "w") as temp:
            temp.write("""TEMP FILE OF ALI
import {0} as l
def ret():
    return l""".format(self.lib)
        import a
        return a.ret()
        
    def install(self):
        """install the lib"""
        os.system("pip install {0}".format(self.lib))