#!/usr/bin/python
# coding=utf-8

import re
import sys

if len(sys.argv) < 2:
    exit()

pattern = re.compile('889[0-9]')

match_ret = pattern.match(sys.argv[1])

if match_ret:
    print match_ret.group()