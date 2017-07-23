#This file is used to write various utilities needed

from Constants import *

#file reading 
def openFile(nameOfFile,mode):
	if mode == READ:
		return open(nameOfFile,"r")
	elif mode == WRITE:
		return open(nameOfFile,"w")
	elif mode == READ_AND_WRITE:
		return open(nameOfFile,"r+w")
	else:
		return

