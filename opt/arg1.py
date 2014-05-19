import argparse

parser = argparse.ArgumentParser(prog="args1", description="args test")
parser.add_argument("--add", help="add num")

parser.parse_args()