a = ['hey', 'bro', 'you are', 'awesome']

for i in a: 
    print (i)

dir(a)

# Implement remote control class that allows you to press next button to go to next TV channel
class RemoteControl ():
    def __init__(self):
        self.channels = ['HBO', 'cnn', 'abc']
        self.index = -1

    def __iter__(self):
        return self 
    
    def __next__(self): # always define the next method
        self.index += 1 
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    
r = RemoteControl()
itr = iter(r)
print (next(itr))
print (next(itr))
print (next(itr))
print (next(itr))

