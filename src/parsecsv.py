# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
import os
import sys
import logging
import logframework
from CustomException import CustomException

logger = logging.getLogger('parsecsv')
def parse_csv_and_get_columns(filename):
    logger.info("Enter in Execution")
    if os.path.isfile(filename):
        csvFile = open(filename, 'r')
        lines = csvFile.readlines()
    else:
        raise CustomException('File is not availble')
    for line in lines[1:]:
        val = line.split(",")
        try:
            test_zero_div =  (int(val[0]) / int(val[11]))
            print(test_zero_div)
        except TypeError:
            logger.info("Exception Occured TypeError")
            raise CustomException('Invalid Types')
        except ZeroDivisionError:
            logger.info("Exception Occured ZeroDivisionError")
        except ValueError:
            logger.info("Exception Occured ValueError")    

                


if __name__ == "__main__":

    logframework.setup_logging()
    logger.info("input File: "+sys.argv[1])
    parse_csv_and_get_columns(filename=sys.argv[1])
