import sys
from tree import get_color_tree

def main():
    print(sys.argv)
    get_color_tree(sys.argv[1])

if __name__ == "__main__":
    main()