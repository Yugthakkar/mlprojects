import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
# here we are using os.makedirs to create the directory if it does not exist
# os.makedirs will not raise an error if the directory already exists
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)



logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO, 
)

if __name__=="__main__":
    logging.info("Logging has started")
    logging.error("This is an error message")
    logging.warning("This is a warning message")
    logging.debug("This is a debug message")
    logging.critical("This is a critical message")
    logging.info("Logging has ended")
    
    print(f"Logs are saved at {LOG_FILE_PATH}")