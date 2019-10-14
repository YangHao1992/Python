#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--description", help="ls additional conditions")
parser.add_argument("--path", required=True, help="ls path")
args = parser.parse_args()
print(args)
