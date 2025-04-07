import logging

def setup_logging(log_file='text_analyzer.log'):
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',  
        filename=log_file,  
        filemode='a'  
    )
    logging.info("Logging is configured.")