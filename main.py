#!/usr/bin/env python3.8
import subprocess
import sys
import time

from subprocess import Popen

from logger import logger
from argparser import args


def are_arguments_passed():
    logger.info("Checking passed arguments...")
    if len(sys.argv) > 1:
        return True
    return False

def create_file(delay, file_name):
    time.sleep(int(delay))
    with open(file_name, 'w') as file:
        file.write(delay)


def main():
    logger.info("Started.")
    if are_arguments_passed():
        create_file(args.delay, args.filename)
    else:
        Popen(["./main.py", '-f', 'file5.txt', '-d', '5'])
        Popen(["./main.py", '-f', 'file10.txt', '-d', '10'])

    logger.info(f"Finished [Delay: {args.delay}, FileName: {args.filename}].")
    







if __name__ == '__main__':
    main()
