from pathlib import Path
from colorama import Fore, Style

def parse_folder(path, iteration_count):
    for element in path.iterdir():
        space_before = ' '*4*iteration_count
        if element.is_dir():
            print(space_before + Fore.BLUE + element.name + '/')
            parse_folder(element, iteration_count + 1)
        if element.is_file():
            print(space_before + Fore.GREEN + element.name)
        

def get_color_tree(path: str):
    absolute_path = Path(path)

    if not absolute_path.exists() or not absolute_path.is_dir():
        print('Dir not found')
        return

    parse_folder(absolute_path, iteration_count=0)
    print(Style.RESET_ALL)