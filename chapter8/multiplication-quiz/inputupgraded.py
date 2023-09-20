import threading, re

class TimeoutException(Exception):
    pass

class RetryLimitException(Exception):
    pass

#integer input validation
def input_str(prompt: str, allowed_regexes: list = None,timeout: float = 0, retry_amount: int = 0):
    #Function to return true/false if regex cases passed
    def test_regex(regexes: list, test_str: str):
        if not regexes:
            return False
        
        test_regex_cases = False
        for regex in regexes:
            compiled_allowed_regex = re.compile(regex)
            match_object = compiled_allowed_regex.search(test_str)
            
            if match_object:
                test_regex_cases = True
        
        return test_regex_cases

    #Set MAXIMUM_TIME_REACHED to threads so they can get accessed
    #Creates a threading.Timer object and run it if timeout is greater than 0
    global MAXIMUM_TIME_REACHED
    
    MAXIMUM_TIME_REACHED = False
    timer = None
    def timer_callback():
        global MAXIMUM_TIME_REACHED

        MAXIMUM_TIME_REACHED = True
    
    if timeout > 0:
        timer = threading.Timer(timeout, timer_callback)
        timer.start()

    #will check if retries are needed
    RETRY_TEST = False
    if retry_amount > 0:
        RETRY_TEST = True

    while True:
        try:
            if RETRY_TEST and retry_amount < 1:
                if timer:
                    timer.cancel()
                raise RetryLimitException

            print(prompt, end='')
            test_input = int(input())

            #only raise exception if timer thread changes MAXIMUM_TIME_REACHED to True
            #Top priority should be raising an exception before any of the tests conclude (countdown reached )
            if MAXIMUM_TIME_REACHED:
                raise TimeoutException

            if allowed_regexes and not test_regex(allowed_regexes, str(test_input)):
                if RETRY_TEST:
                    retry_amount -= 1
                continue
            
        except ValueError:
            print('Input can only be an integer')
            continue
        else:
            if timer:
                timer.cancel()
            break