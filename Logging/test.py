from logger import logging

def add(a,b):
    logging.debug("Addition is going to Done")
    return a+b

logging.debug("additional Process Started")
add(10,15)
logging.debug("additional Process Completed")


