import logging
import socket
host = socket.gethostname()
ip   = socket.gethostbyname(host)
#change the default level as DEBUG
logging.basicConfig(level = logging.DEBUG,
                    filename = "err.log",
                    format="%(message)s %(asctime)s "+ip)
logging.debug("message-1")    # 10>=DEFAULT - log  else supress
logging.info("message-2")     # 20>=DEFAULT - log  else supress
logging.warning("message-3")  # 30>=DEFAULT - log  else supress
logging.error("message-4")    # 40>=DEFAULT - log  else supress
logging.critical("message-5") # 50>=DEFAULT - log  else supress




