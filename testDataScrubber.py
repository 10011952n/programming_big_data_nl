#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 07 2017

@author: 10011952 - niamh lynagh

    1. create an instance of Commit inheriting the unittest class

    2. .

"""

import unittest

from DataScrubber import Commit

class DataScrubberTest(unittest.TestCase):


    
    def testCommit_SetsGets(self):
        
        myCommit = Commit('revision1', 'author1', datetime.date.today(), 1, 'changes1', 'comment1' )
        self.assertEqual('revision1', myCommit.getRevision())
        self.assertEqual('author1', myCommit.getAuthor())        
        self.assertEqual('May 07 2017', myCommit.getDate())        
        self.assertEqual(1, myCommit.getCommentLineCount())        
        self.assertEqual('changes1', myCommit.getChanges())        
        self.assertEqual('comment1', myCommit.getComment())  
               
        self.assertEqual('test revision', myCommit.setRevision))
        self.assertEqual(None, myCommit.setRevision('test revision'))        
        

    
               
if __name__ == '__main__':
    unittest.main()