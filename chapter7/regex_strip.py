import re

def r_strip(passed_string, strip_char=''):
    if strip_char != '':
        compiled_regex = re.compile('^[{}]+|[{}]+$'.format(strip_char, strip_char))
        return compiled_regex.sub('', passed_string)
        
    else:
        compiled_regex = re.compile(r'^\s+|\s$')
        return compiled_regex.sub('', passed_string)
        

spam = r_strip('SpamSpamBaconSpamEggsSpamSpam', 'Spam')
print(spam)