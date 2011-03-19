from clint.packages import colorama

"""
Simple colorama wrapper
"""

class ColoredString(object):
    def __init__(self, color, s):
        super(ColoredString, self).__init__()
        self.s = s
        self.color = color
        self.color_str = '%s%s%s' % (
            getattr(colorama.Fore, self.color), self.s, colorama.Fore.RESET)
        
    def __len__(self):
        return len(self.s)
        
    def __repr__(self):
        return "<%s-string: '%s'>" % (self.color, self.s)
        
    def __str__(self):
        return self.__unicode__().encode('utf8')
        
    def __unicode__(self):
        return self.color_str
        
    def __add__(self, other):
        return self.color_str + str(other)
        
    def __radd__(self, other):
        return str(other) + self.color_str

colorama.init(autoreset=True)

def black(string):
    return ColoredString('BLACK', string)

def red(string):
	return ColoredString('RED', string)

def green(string):
	return ColoredString('GREEN', string)

def yellow(string):
	return ColoredString('YELLOW', string)

def blue(string):
	return ColoredString('BLUE', string)

def magenta(string):
	return ColoredString('MAGENTA', string)

def cyan(string):
	return ColoredString('CYAN', string)

def white(string):
	return ColoredString('STRING', string)
