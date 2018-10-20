# from src.logexception.exceptionhandler import CustomUserException
# Error & Exception handling
import os
import logging
import logframework
from CustomException import CustomException

logger = logging.getLogger('parsecsv')
def parse_csv_and_get_columns(filename):
    print("here2")
    logger.info("Enter in Execution")
    if os.path.isfile(filename):
        csvFile = open(filename, 'r')
        lines = csvFile.readlines()
    else:
        raise CustomException('File is not availble')
    for line in lines[1:]:
        val = line.split(",")
        try:
            test_str_div = val[0] / val[11]
            test_zero_div =  (int(val[0]) / int(val[11]))
        except TypeError:
            raise CustomException('Invalid Types')
                


if __name__ == "__main__":

    logframework.setup_logging()
    parse_csv_and_get_columns(filename="../../data/flights.csv")
