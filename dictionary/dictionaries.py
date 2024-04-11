# dictionaries allows you to store key, value pairs.
# also known as maps, hastables, associate arrays 

d = {"tom": 234234, "sam": 23423423}

d['sam']

# deleting 
del d['sam']


for key in d: 
    print ('key: ', key, "value", d[key])

for kv, in d.items():
    print ('key: ', key, "value", d[v])

# empty the dictionary 
d.clear()