import pandas
import sys
import logging
import logframework

class CSVManipulator:

    def __init__(self, csvfile):
        self.csvfile = csvfile


    def removeColumnfromCSVFile(self,cloumn):
        logger.info("In removeColumnfromCSVFile")
        columnsinFile = list(pandas.read_csv(self.csvfile, nrows =1))
        print(columnsinFile)
        csvwithremovedCloumn = pandas.read_csv(self.csvfile,usecols =[i for i in columnsinFile if i != cloumn])
        print(csvwithremovedCloumn)

    def renameColumn(self,fromCloumn,toCloumn):
        logger.info("In renameColumn")
        csvFile = pandas.read_csv(self.csvfile)
        csvFile.rename(columns={fromCloumn: toCloumn}, inplace=True)
        print(csvFile.columns)




if __name__ == "__main__":
    logger = logging.getLogger('csvmanipulation')
    logframework.setup_logging()
    logger.info("input File: "+sys.argv[1])
    csvmanipulate = CSVManipulator(sys.argv[1])
    csvmanipulate.removeColumnfromCSVFile("DAY_OF_WEEK")
    csvmanipulate.renameColumn("WHEELS_OFF","HAS_WHEELS")
   
   
