#logging example
#6/12/2019

#levels of logging with paired numberic value: Notset-0, Debug-10, 
#                       Info-20, Warning-30, Error-40, Critical-50
#you can create additional levels

import logging
import math

#print(dir(logging))

#create and configure logger
#python.org has more infor for formating logs
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\python\\Lumberjack.Log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w') #filemode = 'w'  will overwrite the log instead of simply append
logger = logging.getLogger()

#Test the logger
logger.info("Our first message.") #doesn't print message because level of logger

print(logger.level)
#basicConfig sets to the level to 30 as a default

#Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx+ c = 0"""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a,b,c))

    #Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    #Compute the two roots
    logger.debug("#Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b + math.sqrt(disc)) / (2*a)

    #Return the two roots as a tuple
    logger.debug("#Return the two roots as a tuple")
    return (root1, root2)

roots = quadratic_formula(1, 0, 0)
print(roots)