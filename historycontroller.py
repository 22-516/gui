import os
from print_color import print

from PyQt6.QtCore import * #temp
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def CheckIfHistoryFilesExist(): # make sure the file exists and all recent files exist before reading/writing
    if not os.path.isfile(recentFilePath := os.path.join("data", "recent.txt")):
        with open(recentFilePath, "x") as filePath:
            pass
    
    removedFiles = [] # remove all links that are no longer valid
    with open(recentFilePath, "r") as filePath:
        fileContent = filePath.readlines()
        for line in fileContent:
            if not os.path.exists(line):
                removedFiles.append(line)
    for filePath in removedFiles:
        RemoveFromRecentFileList(filePath)

def FetchRecentFileList():
    fileList = []
    with open(os.path.join("data", "recent.txt"), "r") as recentFileList:
        while line := recentFileList.readline():
            #print(line.rstrip())
            fileList.append(line.rstrip())
    return fileList

def PrependRecentFileList(filePath=""):
    RemoveFromRecentFileList(filePath) # remove previous entry
    with open(os.path.join("data", "recent.txt"), "r+") as recentFileList:
        tempFile = recentFileList.read() # save file to memory so that we can prepend to the beginning of the file                
        recentFileList.seek(0,0)
        recentFileList.write(filePath.rstrip("\r\n") + "\n" + tempFile)

def RemoveFromRecentFileList(filePath=""):
    print("removing from recent file list", filePath, tag="history", tag_color="yellow", color="white")
    
    with open(os.path.join("data", "recent.txt"), "r+") as recentFileList:
        fileContent = recentFileList.readlines()
        recentFileList.seek(0)
        recentFileList.truncate()
        for line in fileContent:
            if line.strip("\n") != filePath:
                recentFileList.write(line)
