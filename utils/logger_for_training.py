import logging


def get_logger(exp_name):
    logger = logging.getLogger(exp_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    import time
    log_time = time.strftime("%Y-%m-%d-%H-%M", time.gmtime())
    file_handler = logging.FileHandler(f'{exp_name}_{log_time}.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
  
  
if __name__ == '__main__':
    logger.info('TEST')
    
    
