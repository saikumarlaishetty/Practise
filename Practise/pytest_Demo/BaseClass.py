import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]   # To correct the test case name while printing in logs it was printing baseclass always with __name_
        logger = logging.getLogger(loggerName)   # logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)  # INFO, warning , error and critical are printed
        return logger
