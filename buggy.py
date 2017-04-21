import sys
import math
import pychecker.checker

class Sample:
    """"""
 
    def __init__(self, num1, num2, num3):

        if "Windows" in platform.platform():
            print "You're using Windows!"
        if "Linux" in platform.platform():
            print "You're in Linux!"
 
        self.addition = self.addition(1, 2, 3)
 
    #----------------------------------------------------------------------
    def addition(this):
        """"""
        return 1+2+3
