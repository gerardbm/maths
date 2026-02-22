#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : LCM & GCD
# Version : 2.0.0
# Python  : 3.13.5
# License : MIT
# Author  : Gerard Bajona
# Created : 17/07/2022
# Changed : 22/02/2026
# URL     : http://github.com/gerardbm/maths
# --------------------------------------------------
"""LCM & GCD calculator"""

from numpy import lcm,gcd
import argparse

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

def get_lcm_gcd(values):
    """LCM & GCD"""
    if len(values) > 2:
        result_lcm = lcm.reduce([*values])
        result_gcd = gcd.reduce([*values])
    else:
        result_lcm = lcm(*values)
        result_gcd = gcd(*values)

    print()
    print("> LCM =", result_lcm)
    print("> GCD =", result_gcd)

def main():
    """Main program."""
    values = parse_arguments()
    get_lcm_gcd(values)

if __name__ == '__main__':
    main()
