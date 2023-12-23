"""
The main backend script and the entry point.

In this template we just have 1 main function 'main_backend_foo' in this 
script that is our entry point and runs the main backend logic. So from the
app we just call that main function, but we can also test this by calling
'__main__' from the command line.

Note:
  * in '__main__'. It collects command line arguments, so we can control 
  behavior of the script with command line arguments.
  * also it reads the main config.yaml, so we try to put all configs in that
  file
  * also it sets up the logger with some options from the config

@author: Domantas M.
"""
import backend.additional_backend as mylib


def main_back_foo(str_arg, int_arg):
    """The main backend function.
    
    This this is our mockup main function for the backend logic. It can of 
    course call other stuff from other modules like mylib.string_multi in this 
    mockup case.
    
    Args:
        str_arg: a string
        int_arg: an int
        
    Returns:
        Returns a string
    """
    res = mylib.string_multi(str_arg, int_arg)
    
    return res
    
def log_message(log, message):
    """Just a dummy function that writes a message into a logger.
    
    Args:
        log:  logger object
        message: a string
    """
    from datetime import datetime
    time_stamp = str(datetime.now())
    log.info(message+' '+time_stamp)

if __name__ == '__main__':
 
    # get command line arguments
    print('Getting args...')
    args = mylib.get_args()

    # reading the main config file
    print('Reading config file...')
    config = mylib.read_config(args.config)
    
    # setting up logger
    print('Setting up logger...')
    log = mylib.setup_logger(config['logging'], 'debug_stream')
    
    # just checking for some optional args if provided else we use predefined in script
    my_string = 'test'
    if args.string:
        log.info('String is: '+ args.string)
    else:
        log.info('String is: '+ my_string)    
     
    # we take parameter from the config file
    log.info('Multiplier is: ' + str(config['parameter']['multi']))
    
    # now we call the main function in this script
    res = main_back_foo('go', 3)
    log.info('Result is: ' + res)
    
    print('---')
    log_message(log, 'Hi from main_backend.')
    
    
    
    