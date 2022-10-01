#!/usr/bin/env python3

# ###
# I've grown irritated with having to set up the project structure 
# for every single one of my c/cpp projects xd
# so I decided to make a simple python script to handle that for me lol
# ###


import os

# Recursively creates directories
def makeDirectory(name):
	naems = name.split("/");
	if naems[0] == ".":
		makeDirectory(name[2 : len(name)])
		return
	try:
		os.mkdir("./" + naems[0])
	except:
		pass
	name = name[len(naems[0])+1 : len(name)]
	if len(name) > 0:
		os.chdir(naems[0])
		makeDirectory(name)
		os.chdir("..")

# Recursively creates a file with custom contents in it
def makeFile(name, contents=""):
	naems = name.split("/");
	if len(naems) > 1:
		makeDirectory(name[0 : -len(naems[-1])])
	fp = open(name, 'w')
	fp.write(contents)
	fp.close()

# Opens and dumps a file into a string
def loadFile(name):
	fp = open(os.path.dirname(os.path.abspath(__file__)) + "/" + name, "r")
	data = fp.read()
	fp.close()
	return data

# Application's entry point
def main():
	# File contents
	gitignore = loadFile("res/_gitignore")
	# File structure creation
	makeFile("src/main.c")
	makeFile("include/lib.h")
	makeFile("build/.build")
	makeFile(".gitignore", gitignore)


if __name__ == "__main__":
	main()