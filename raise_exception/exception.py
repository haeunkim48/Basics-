class Accident (Exception):
    def __init__(self):
        self.msg = msg 
    def print_excpetion (self):
        print ("User defined excpetion", self.msg)


try: 
    raise Accident ('crash between two cars')
except Accident as e: 
    e.print_excpetion()

#---------
def process_file():
    try: 
        f = open ('file path')
        x = 1/0
    except FileNotFoundError as e: 
        print ('inside except')
    finally: # it will always execute the code in finally block no matter what 
        print ('cleaning up file')
        f.close()