# file name and path, file open mode 
f = open("C: \\data \\funny.txt", 'w')

f.write ("I Love Python")
f.close() # we always should do this 

# mode 
# w : write, a = append, r = read

# we want to create new file that has all the lines in funny text 
# plus word cound for each line 

f = open("C: \\data \\funny.txt", 'r')
print (f.read())
f.close()

# line by line 
for line in f: 
    print (line)
f.close()

# separator split() will split the string using input charater and return a list of words
for line in f: 
    tokens = line.split(' ')
    print (len(tokens))
f.close


#-------------------------------------
f = open("C: \\data \\funny.txt", 'r')
f_out = open("C: \\data \\funny_cs.txt", 'w')

for line in f: 
    tokens = line.split(' ')
    f_out.write("wordcount:" + str(len(tokens)) + license) # + operator is used to append 

f.close
f_out.close()

#-------------------------------------
# with statement, you don't need to f.close()
with open ("C: \\data \\funny.txt", 'r') as f: 
    print(f.read())

# how to check whether the file is open or closed 
print (f.closed())