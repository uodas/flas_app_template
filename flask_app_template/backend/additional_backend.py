"""
A file with a mockup bunch of various foos for the backend.

An example of additional files with various backend logic stuffs.

@author: Domantas M.
"""

import argparse, yaml, logging.config

def get_args():
    """Collect command line arguments.
    
    Returns:
        argparse.Namespace object which contains parsed command line args
    """
    parser  = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Path to config.yaml file.', required=True)
    parser.add_argument('-s', '--string', help='Provide some string.')
    args = parser.parse_args()
    return args    

def read_config(config_file_path):
    """Reads in config file.
    
    Args:
      config_file_path: a path to config yaml file.
      
    Returns:
      dict with complete conif.yaml file.
      
    """
    with open(config_file_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config
 
def setup_logger(log_config, logger_name):
    """Sets up logger.
    
    Args:
      log_config: dict with log configurations
      logger_name: str with a name which is in log_config. So the name would
      have specific setting for a specific logger.
      
    Returns:
      log object
    """
    # with this line you load  the whole logger config poriton 
    logging.config.dictConfig(log_config)
    # with this you choose which of defined loggers you actually use
    log = logging.getLogger(logger_name)
    return log

def string_multi(input_string, multiplier):
    """A function that multiplies a string by a number.
    
    Just a mockup foo to have some additional logic.
    
    Args:
        input_string: a string
        multiplier: an int by which the string will be multiplied
    Returns:
        string 
    """
    res = (input_string+' ') * multiplier
    return res
    

if __name__ == '__main__':
    
    # we can use this scripts main to run / test some foos in this script
    my_str = 'me'
    my_multi = 10
    res = string_multi(my_str, my_multi)
    print(res)
    
    