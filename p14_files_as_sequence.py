# File handle as a Sequence

#A file handle open for read of string where each line in the
#file is a string in the sequence

# we can use the for statement
#to iterate througth a sequence

#for each line in the text
#--------cOUNTING LINES IN A FILE----------------
fhand = open('file.txt')
count = 0
for line in fhand:
    count = count + 1
print('line count:', count)

#--------READING THE WHOLE FILE-----------------
fhand = open('file.txt')
inp = fhand.read() #lee letra por letra
print(len(inp)) #
print(inp[:20]) #print letter 0-20-

#-------Searching Through a file----------------
fhand = open('file.txt')
for line in fhand: #line revision of each line text 
    if line.startswith('From:') :    
        print(line)

#------Skipping with continue
fhand = open('file.txt')
for line in fhand: #line revision of each line text
    line = line.rstrip()
    if not line.startswith('From:') :
        continue #we can skip line of file with continue
    print(line) 

#----------Using in to select lines------------
#we can look for a string aniwhere in a line as our
#selection criteria
fhand = open('file.txt')
for line in fhand: #line revision of each line text
    line = line.rstrip()
    if not 'hacer' in line :
        continue
    print(line)

#-------------Prompt for file Name--------------
fname = input('Enter the file name:')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in',fname)

#--------Bad File Names----------------------------
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in',fname)       

#-----------