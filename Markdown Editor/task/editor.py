def header():
    level = int(input('Level: '))
    while level not in range(1, 7):
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    text = input('Text: ')
    prefix = ''
    for _ in range(level):
        prefix += '#'
    return prefix + ' ' + text + '\n'


def plain():
    return input('Text: ')


def bold():
    return '**' + input('Text: ') + '**'


def italic():
    return '*' + input('Text: ') + '*'


def inline_code():
    return '`' + input('Text: ') + '`'


def newline():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return '[' + label + '](' + url + ')'


def md_list():
    global inp
    otp = ''
    num_of_rows = int(input('Number of rows: '))
    while num_of_rows <= 0:
        print('The number of rows should be greater than zero')
        num_of_rows = int(input('Number of rows: '))

    if inp.startswith('o'): # unordered list
        for i in range(1, num_of_rows + 1):
            str_i = str(i)
            row = str(i) + '. ' + input('Row #' + str_i)
            otp += row + '\n'
    else:
        for i in range(1, num_of_rows + 1):
            str_i = str(i)
            row = '* ' + input('Row #' + str_i)
            otp += row + '\n'
    return otp


formats = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header, 'link': link, 'inline-code': inline_code, 'ordered-list': md_list, 'unordered-list': md_list, 'new-line': newline}
otp = ''
while True:
    inp = input('Choose a formatter: ')
    if inp == '!done':
        fh = open('output.md', 'w')
        fh.write(otp)
        fh.close()
        break
    elif inp == '!help':
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')
    elif inp not in formats:
        print('Unknown formatting type or command')
    else:
        otp += formats[inp]()
        print(otp)
