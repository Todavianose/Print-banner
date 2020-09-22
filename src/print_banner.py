import os
from pyfiglet import Figlet


def print_banner(banner, sub_banner, type_font="big", clear=True):
    """ Print banner 
        type_font: https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts
    """
    banner_text = Figlet(font=type_font)
    if clear:
        os.system('clear')
    return str(banner_text.renderText(banner) + sub_banner)

if __name__ == "__main__":
    #Test
    print(print_banner("NoseII", '   https://www.todavianose.com'))