"""
Created on Sun May 07 2017

@author: 10011952 - Niamh Lynagh

Data Scrubber App:
    
    1. imports data scrubber class
    2. 
    
"""
from DataScrubber import Commit

# in this instance the file being scrubbed is changes_python.txt
# the code assumes the file is in the same folder as this App 
#  therefore no file path is required

# set the file name to the file handle in the program
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.


data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

# viewing the file has identified the line separator as 72 hyphens
# create a variable to represent the line separator

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.


commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())
