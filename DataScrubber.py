# -*- coding: utf-8 -*-
"""
Created on Sun 07 May 2017

@author: 10011952 - Niamh Lynagh

commit class:
    
    1. commit class contains the data
    2. 
    
"""



class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.__revision = revision
        self.__author = author
        self.__date = date
        self.__comment_line_count = comment_line_count
        self.__changes = changes
        self.__comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.__revision-1) 
                
                

    def setRevision(self, value):
        self.__revision = value
    
    def setAuthor(self, value):
        self.__author = value
        
    def setDate(self,value):
        self.__date = value
 
    def setCommentLineCount(self, value):
        self.__comment_line_count = value
        
    def setChanges(self, value):
        self.__changes = value      
        
    def setComment(self, value):
       self.__comment = value       

        
    def getRevision(self):
        return self.__revision
    
    def getAuthor(self):
        return self.__author
        
    def getDate(self):
        return self.__date
 
    def getCommentLineCount(self):
        return self.__comment_line_count
        
    def getChanges(self):
        return self.__changes        
        
    def getComment(self):
        return self.__comment      

 
 
