import logging

def setup_logger():
    """
    Set up the logger.
    """
    logging.basicConfig(filename='ids.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    """
    Log an event or anomaly.

    Args:
        event (dict): The event or anomaly to log.
    """
    setup_logger()
    logging.info(str(event))
