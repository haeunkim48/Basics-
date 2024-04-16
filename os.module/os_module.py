import os 
print (dir(os)) # shows us everything 

print (os.getcwd()) # cwd: current working directory 

os.chdir('/Users/gracefile/Desktop') # chdir change directory 

os.listdir( ) #listing the folders in current directory

os.mkdir('OS-Dremo') # 

os.makedirs('OS-Dremo/sub') # make deeper level directories that you need 

# remove 
os.rmdir('OS-Dremo') # will not remove deeper level directories 
os.removedirs('OS-Dremo/sub')

#rename 
os.rename('test.txt', 'demo.txt')

#information of the file
print (os.stat('demo.txt').st_mtime) # st_mtime is modified time 

import os 
from datetime import datetime 

mod_time = os.stat('demo.txt').st_mtime
print (datetime.fromtimestamp(mod_time))

#wanna see the entire directory tree and files 
os.walk()

for dirpath, dirname, filenames in os.walk('/Users/gracefile/Desktop'):
    print ('current path: ', dirpath)
    print ('directories: ', dirname)
    print ('files: ', filenames)
    print ()

os.environ.get('HOME')

'test.txt'

file_path = os.environ.get('HOME') + 'test.txt' # this can miss some slash
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

os.path.basename('/tmp/test.txt')
os.path.dirname('/tmp/test.txt')
os.path.split('/tmp/test.txt')

#checking if the directory is fake 
os.path.exists('/tmp/test.txt')

print (os.path.isfile('/tmp/test.txt')) # this is when you check the file 

print (os.path.splitext) # split the extension 
