import os
import sys

import easygui

def guiCallback(option):
	folderPath=sys.argv[1]+'\\'
	print folderPath
	
	if (option._text=='Replace String'):
		values=easygui.multenterbox("Enter replace data:", "Replace",["Replace What? : ","Replace With ? : "])
		if values != None:
			whatStr=values[0]
			withStr=values[1]
			for fn in os.listdir(folderPath):
				os.rename(folderPath+fn,folderPath+fn.replace(whatStr,withStr))
	elif (option._text=='Add String to End'):
		values=easygui.multenterbox("Enter string data:", "Add to End",["String to be added : "])
		if values != None:
			whatStr=values[0]
			for fn in os.listdir(folderPath):
				ext=fn.split('.')[1]
				name=fn.split('.')[0]
				os.rename(folderPath+fn,folderPath+name+whatStr+"."+ext)
	elif (option._text=='Add String to Start'):
		values=easygui.multenterbox("Enter string data:", "Add to Start",["String to be added : "])
		if values != None:
			whatStr=values[0]
			for fn in os.listdir(folderPath):
				ext=fn.split('.')[1]
				name=fn.split('.')[0]
				os.rename(folderPath+fn,folderPath+whatStr+name+"."+ext)
	elif(option._text=='Give sequence number to files'):
			Counter=0
			z=list(os.listdir(folderPath))
			list.sort(z)
			for fn in z:
				ext=fn.split('.')[1]
				name=fn.split('.')[0]
				Counter+=1
				os.rename(folderPath+fn,folderPath+str(Counter)+name+"."+ext)
	elif(option._text=='Change extension of files'):
		values=easygui.multenterbox("Enter extension:", "To which",["Enter : "])
		if values != None:
			whatStr=values[0]
			for fn in os.listdir(folderPath):
				ext=fn.split('.')[1]
				name=fn.split('.')[0]
				os.rename(folderPath+fn,folderPath+name+"."+whatStr)
	elif (option._text=='About :)'):
		easygui.msgbox("Programmed By Ammar Rajab :)","About")	
easygui.buttonbox('What do you want to do with the files ?', 'Files Options', ('Change extension of files','Replace String', 'Add String to End', 'Add String to Start','Give sequence number to files', 'About :)'),callback=guiCallback)


