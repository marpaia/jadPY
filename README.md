jadPY
=====

jadPY is a utility used to decompile JAR files. This was originally written for Windows and has only been tested on Windows. jadPY is basically just a wrapper for jad.exe, the Java decompiler. 


Functionality
-------------

### Point jadPY at a jar file and it will:

* Decompress the jar file using the "unzip" library
* Recursively traverse all directories to locate all .class files
* Decompile all .class files using jad.exe
* Delete the .class files

### Point jadPY at a directory and it will:

* Recursively traverse all directories to locate all .jar files
* Decompress each jar file using the "unzip" library
* Recursively traverse all directories within the unzipped .jar file to locate all .class files
* Decompile all .class files using jad.exe
* Delete the .class files

This results in a directory structure similar to the jar file, except everything is decompressed and decompiled.

Usage
-----

Point jadPY at your jar file using the `-f` flag. 
	python jad.py -f file.jar

Point jadPY at your direcotry of jar files using the `-d` flag
	python jad.py -d "C:\Users\mike\jarfiles\"

The default directory for jad.exe is `C:\tools\jad.exe`. If that is not where your install of jad.exe is, you can specify the path at runtime using the `-p` flag or manually edit the code to jad.py and change the default path. 
	python jad.py -f file.jar -p "C:\path\to\jad.exe"`


Run `python jad.py -h` for help.

Contact
-------

Mike Arpaia

mike@arpaia.co

http://arpaia.co