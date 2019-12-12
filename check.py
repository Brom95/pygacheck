import argparse

def main(args):

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if gmail account exist.')
    parser.add_argument('-i', help="Emails for checking")
    parser.add_argument('-o', help="File to write checked emails")
    args = parser.parse_args()
    main(args)
