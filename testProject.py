# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:04:24 2018
@author: Vikiest Vik
"""

import os
import sys
import docx
import nltk
import pandas


def filterTag(pos_tag,text):
    returnList = []
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    for word,tag in tagged:
        if(tag in tag_list):
            returnList.append(word)
    return returnList

def extractBaseContext(text):
    context = []
    tag_list = ['NNP','NN','VBZ']
    filtered = filterTag(tag_list,tagged)
    bigrams = nltk.bigrams(filtered)
    trigrams = nltk.trigrams(filtered)
    return context

def isContextSame(text,txt_list):
    return False


def isHeader(paragraph):
    if(paragraph.style.name.startswith('Heading')):
        return True
    else:
        return False

def pushData(text,fileName):
    #print(text)
    print("Creating file name:"+fileName+".txt at F:\\PythonWorkSpace\\testData\\")
    file = open("F:\\PythonWorkSpace\\testData\\"+fileName+".txt","w")
    file.writelines(text)
    file.close
    

def readDocx(filePath,fileName):
    print("Entering the function")
    cwd = os.getcwd()
    absPath = filePath+fileName
    data = []
    file_counter = 0
    if(os.path.isfile(absPath)):
        document = docx.Document(absPath)
        for paragraph in document.paragraphs:
            if(isHeader(paragraph)):
                print("Breaking context")
                if (len(data) < 1):
                    print("Do nothing")
                else:
                    file_counter = file_counter + 1
                    pushData(data,"context"+str(file_counter))
                    data.clear()
            elif(isContextSame(0,0)):
                print("Breaking context")
                if (len(data) < 1):
                    print("Do nothing")
                else:
                    file_counter = file_counter + 1
                    pushData(data,"context"+str(file_counter))
                    data.clear()                
            else:
                #extractBaseContext(paragraph.text)
                data.append(paragraph.text)        
    else:
        print("File does not exists, exiting")
        
if __name__ == "__main__":
    print("Starting Module")
    readDocx("F:\\PythonWorkSpace\\testData\\","demo.docx")

#print("Entering "+ __name__) 
#readDocx("F:\\PythonWorkSpace\\testData\\","demo.docx")
