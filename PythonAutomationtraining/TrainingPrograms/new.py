import sys
import logging as log

# default log level - DEBUG
# redirect the logs to "Err.log"
log.basicConfig(level=log.DEBUG, filename="err.log")
print(sys.argv)
scriptname = sys.argv[0]
print(scriptname)
if len(sys.argv) == 4:
    try:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            if sys.argv[3]=='add':
                print(num1+num2)
            if sys.argv[3]=='sub':
                print(num1-num2)
            if sys.agrv[3]=='mul':
                print(num1*num2)
            if sys.agrv[3] =='div':
                print(num1/num2)
            else:
                log.error("Error - Factor operation is not supported")
        else:
            log.debug("one of the argument is a string")
            raise ValueError("one of the input is a string")

        res = num1 + num2
    except IndexError as e:
        log.debug(e)
    except Exception as e1:
        log.debug("Type of Exception = " + str(e1) + " " + str(type(e1)))
    else:
        print("Result = ", res)
    finally:
        print("End of program")
else:
    print("Error = In sufficient args")
    print("Usage:")
    print("C:\> python %s <int> <int>" % (scriptname))

