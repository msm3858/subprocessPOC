import argparse
from logger import logger

def __get_parser():
    parser = argparse.ArgumentParser(description='ElvUI updater.')
    parser.add_argument('-f', '--filename', help='Name of file to be created.')
    parser.add_argument('-d', '--delay', help='Delay of file creation.')
    return parser

args = __get_parser().parse_args()