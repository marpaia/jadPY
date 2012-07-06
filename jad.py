#!/usr/bin/env python
import os, glob, zipfile, sys, getopt

#############################
# Default JAD Path			
#############################
jad = "C:\Tools\jad.exe"

def help():
	print '''
####################################################################
#
#       o8o                 .o8      ooooooooo.   oooooo   oooo 
#       `-/                 888      `888   `Y88.  `888.   .8'  
#      oooo  .oooo.    .oooo888       888   .d88'   `888. .8'   
#      `888 `P  )88b  d88' `888       888ooo88P'     `888.8'    
#       888  .oP"888  888   888       888             `888'     
#       888 d8(  888  888   888  .o.  888              888      
#       888 `Y888""8o `Y8bod88P" Y8P o888o            o888o     
#       888                                                     
#   .o. 88P                                                     
#   `Y888P                                                
#
####################################################################
#
#	Usage:
#
#		-f	<jar file>
#
#		-d	<C:\Directory\of\jar\files\>
#
#		-p	<C:\path\\to\jad.exe>
#
#		-h	(help)
#
#	Examples:
#
#		python jad.py -f file.jar
#		python jad.py -f file.jar -p "C:\path\\to\jad.exe"
#		python jad.py -d "C:\Users\mike\jarfiles\"
#
####################################################################
#
#	For more info, see:
#
#		http://arpaia.co
#
#	Or email:
#
#		mike@arpaia.co
#
####################################################################
	'''

def args():
	global jar, dir
	jar = 0
	dir = 0

	try:
		opts, args = getopt.getopt(sys.argv[1:], "f:p:d:h")
	except:
		help()
		return 0

	if len(opts) == 0:
		help()
		return 0

	for i in opts:
		if i[0] == "-h":
			help()
			return 0
		if i[0] == "-f":
			global jarfile
			jarfile = i[1]
			jar = 1
		if i[0] == "-p":
			global jad
			jad = i[1]
		if i[0] == "-d":
			global directory
			directory = i[1]
			dir = 1

	if not jar ^ dir: return 0
	return 1

def unzipjar(jar):
	file = zipfile.ZipFile(jar)
	file.extractall(os.path.splitext(jar)[0])
	
def q(s):
	quote = "\""
	s = quote + s + quote
	return s

def scandirs(path):
	space = " "
	opts = "-o -s java -d "
	for currentFile in glob.glob( os.path.join(path, "*") ):
		if os.path.isdir(currentFile): scandirs(currentFile)
		elif os.path.splitext(currentFile)[1] == ".class":
			command = q(jad) + space + opts + q(os.path.dirname(currentFile)) + space + q(currentFile)
			os.system(q(command))
			os.system("del " + q(currentFile))
			
def lookforjars(path):
	for currentFile in glob.glob( os.path.join(path, "*") ):
		if os.path.isdir(currentFile): lookforjars(currentFile)
		elif os.path.splitext(currentFile)[1] == ".jar":
			unzipjar(currentFile)
			scandirs(os.path.splitext(currentFile)[0])

if __name__ == "__main__":			
	arg = args()
	if arg == 1:
		if dir == 1:
			lookforjars(directory)
		elif jar == 1:
			unzipjar(jarfile)
			scandirs(os.path.splitext(jarfile)[0])