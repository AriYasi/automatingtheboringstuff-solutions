spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list_parameter):
    if len(list_parameter) > 0:
        for index, item in enumerate(list_parameter):
            if index == len(list_parameter) - 1:
                print('and ' + item)
            else:
                print(item, end=', ')
    else:
        print('Empty list given.')

comma(spam)