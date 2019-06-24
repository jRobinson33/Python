#python exception handling example
#6/24/2019

"""
example of how exception clauses work

try:
    #Runs first
    < code >
except:
    #Runs if exception occurs in try block
    < code >
else:
    # Executes if try block *succeeds*
    <code>
finally:
    #This code *always* executes
    < code >
"""

#Writing a function that reads binary file and returns data
#Measure time required

import logging
import time

#create logger
logging.basicConfig(filename = "C:\\Users\\Turing\\Desktop\\Python\\exception_handling\\problems.log",
                     level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode = "rb") #rb = read binary
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err) #if the file isn't found we log the error
        raise  #instructs python to pass along the file not found error
    else: #only executes if there are no errors in the try block
        f.close() #We have to close it here, because f wouldn't be a file object if it wasn't found
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.debug("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed("E:\\some_directory\\imaginary_file.png")