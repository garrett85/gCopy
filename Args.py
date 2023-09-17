import sys
import argparse

def getArgs():
    """Return list of arguments and options"""
    parser = argparse.ArgumentParser(
        description="Recursivly compare directories and copy differences if desired"
    )
    parser.add_argument("source", help="Source Directory", type=str, default="./")
    parser.add_argument("target", help="Target Directory", type=str, default="./")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--copy", help="Copy source files to target", type=str)
    group.add_argument("-m", "--move", help="Move source files to target ", type=str)
    group.add_argument("-o", "--compare-only", help="Run comparison of source and target files", type=str)

    args = vars(parser.parse_args())
    return args