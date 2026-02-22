#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : LCM & GCD
# Version : 2.1.0
# Python  : 3.13.5
# License : MIT
# Author  : Gerard Bajona
# Created : 17/07/2022
# Changed : 22/02/2026
# URL     : http://github.com/gerardbm/maths
# --------------------------------------------------
"""LCM & GCD calculator"""

import argparse
from math import gcd
from functools import reduce

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="LCM & GCD calculator.")
    parser.add_argument(
        "numbers",
        type=str,
        help="Integers separated by comma (e.g., 12,18,24)")
    args = parser.parse_args()
    try:
        values = list(map(int, args.numbers.split(",")))
    except ValueError:
        parser.error("Provide a list of integers separated by comma.")
    if len(values) < 2:
        parser.error("Provide at least two integers.")
    return values

def lcm(a, b):
    """LCM of two integers."""
    return abs(a * b) // gcd(a, b)

def get_lcm_gcd(values):
    """LCM & GCD"""
    result_gcd = reduce(gcd, values)
    result_lcm = reduce(lcm, values)
    values_fmt = str(values).strip('[,]')

    print()
    print(f"> LCM({values_fmt}) =", result_lcm)
    print(f"> GCD({values_fmt}) =", result_gcd)

def main():
    """Main program."""
    values = parse_arguments()
    get_lcm_gcd(values)

if __name__ == '__main__':
    main()
