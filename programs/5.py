# Цвета терминала.

def print_format_table():

    for style in range(8): 
        for foreground in range(30, 38): 
            color_string = '' 
            for background in range(40, 48): 
                format = ';'.join([str(style), str(foreground), str(background)]) 
                color_string += '\x1b[%sm %s \x1b[0m' % (format, format) 
            print(color_string) 
        print('\n') 
  
print_format_table()


# Цвета терминала.

# class foreground:
#     BLACK   = '\033[30m'
#     RED     = '\033[31m'
#     GREEN   = '\033[32m'
#     YELLOW  = '\033[33m'
#     BLUE    = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN    = '\033[36m'
#     WHITE   = '\033[37m'
#     RESET   = '\033[39m'
# 
# class background:
#     BLACK   = '\033[40m'
#     RED     = '\033[41m'
#     GREEN   = '\033[42m'
#     YELLOW  = '\033[43m'
#     BLUE    = '\033[44m'
#     MAGENTA = '\033[45m'
#     CYAN    = '\033[46m'
#     WHITE   = '\033[47m'
#     RESET   = '\033[49m'
# 
# class style:
#     BRIGHT    = '\033[1m'
#     DIM       = '\033[2m'
#     NORMAL    = '\033[22m'
#     RESET_ALL = '\033[0m'