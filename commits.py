import datetime
from datetime import datetime


   
# create the commit class to hold each of the elements - 422.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None, add_count = 0, modify_count = 0, delete_count = 0, authors = {}, commitDates = {}, strippedDates = {}):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.add_count = add_count
        self.modify_count = modify_count
        self.delete_count = delete_count
        self.authors = authors
        self.commitDates = commitDates
        self.strippedDates = strippedDates
        
    def max(self, values):
        return reduce(lambda a,b: a if (a>b) else b, values)              
    
    def min(self, values):
        return reduce(lambda a,b: a if (a<b) else b, values)
    
    def days_between(self, d1, d2):
        return abs((d2 - d1).days) 

    def convert_date(self, value):
        return datetime.strptime(value , '%Y%m%d')
# stores authors in a dict and their occurrences
    def store_authors(self, value):   
        if value not in self.authors:
            self.authors[value] = 1
        else:
            self.authors[value] += 1
        return self.authors[value]
# isolates the date on each commit and stores it, strips - from the date
# and stores it in a second list 
    def store_dates(self, value):    
        if value not in self.commitDates:
            self.commitDates[value] = 1
            strippedDate = str(value[0:4])  + str(value[5:7]) + str(value[8:10])
            self.strippedDates[strippedDate] = 1
            return self.strippedDates[strippedDate]
        else:
            self.commitDates[value] += 1
            return 0
# picks out the occurrences of A,M,D in the changes and sums them
    def count_commit_types(self, value):
        for word in value:
            if word.startswith("A"):
                self.add_count += 1 
            elif word.startswith("M"):
                self.modify_count += 1
            elif word.startswith("D"):
                self.delete_count += 1        
        return 1


# open the file - and read all of the lines.
changes_file = 'changes_python.txt'

# use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print'lines read: ' + str((len(data)))

sep = 72*'-'
# instantiate the commits list, and other variables
commits = []
current_commit = None
index = 0


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
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break
# display the number of commits
print 'commit lines: ' + str((len(commits)))

# reverse the set and start from the end
commits.reverse()

for index, commit in enumerate(commits):
# store your authors and the no. of times committed by each
    current_commit.store_authors(commit.author)
        
# count the number of files added, modified and deleted by all authors    
    current_commit.count_commit_types(commit.changes)

# store the dates committed, identify the first and last date for all commits       
    current_commit.store_dates(commit.date[:10])
        
# calculate the dates when the commits started and when they stopped
date_min = current_commit.convert_date(current_commit.min(current_commit.strippedDates))
date_max = current_commit.convert_date(current_commit.max(current_commit.strippedDates))

# display the start and end dates for the commits
print 'commits start date: ' + str(date_min)[:10]
print 'commits end date: ' + str(date_max)[:10]

# calculate the number of days from the first date committed to the last date committed
print 'elapsed days commits: ' + str(current_commit.days_between(date_min, date_max))

print 'commit authors: ' + str(len(current_commit.authors)) 
print 'no. of added files: ' + str(current_commit.add_count) 
print 'no. of modifed files: ' + str(current_commit.modify_count)
print 'no. of deleted files: ' + str(current_commit.delete_count)

# calculate the total files amended by commits
total_files = current_commit.add_count + current_commit.modify_count + current_commit.delete_count

print 'total files amended: ' + str(total_files)

# sort from highest to lowest.
print 'authors listed by number of commits: '
for key, value in sorted(current_commit.authors.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print  "%s: %s" % (key, value) 

# plotting your output ~ 
 
import matplotlib.pylab as plt
import numpy as np

# wrap the text for better display
def split_word(s):
    n=7
    return '-\n'.join(s[i:i+n] for i in range(0, len(s), n))
# set your tick size on the y axis
ax = plt.gca()
ax.yaxis.set_tick_params(width=5)

# set the bar chart layout
plt.bar(range(len(current_commit.authors)), current_commit.authors.values(), align="center")
# assign values to the chart
plt.xticks(range(len(current_commit.authors)), [split_word(i) for i in current_commit.authors.keys()])
# rotate your labels on the x  axis.
labels = ax.get_xticklabels()
plt.setp(labels, fontsize=8, rotation = 30.)
# plot your chart
plt.show()