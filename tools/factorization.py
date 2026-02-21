#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Factorization in prime factors
# Version : 2.0.0
# Python  : 3.13.5
# License : MIT
# Author  : Gerard Bajona
# Created : 02/06/2018
# Changed : 21/02/2026
# URL     : http://github.com/gerardbm/maths
# --------------------------------------------------
"""Tool to factorize a number into prime factors."""

import argparse

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
            description="Factorization tool for the command line.")
    parser.add_argument('number',
            type=int,
            help="Integer value to factorize in prime factors")
    args = parser.parse_args()
    if args.number < 2:
        parser.error("The number must be an integer greater than 1.")
    return args.number

def decomposition(number):
    """Decompose the number into prime factors!"""
    dividend = number
    divisor = 2
    columns = []
    factors = []
    while dividend >= divisor:
        while dividend % divisor == 0:
            aligned = abs(len(str(dividend)) - len(str(number)))
            columns.extend([
                " ",
                " " * aligned,
                dividend,
                " | ",
                divisor,
                "\n",
            ])
            dividend = int(dividend / divisor)
            factors.extend([divisor])
        divisor = divisor + 1
    return columns, factors, divisor

def format_group(factors):
    """Formatted output: group factors and exponents."""
    grouped = []
    for factor in factors:
        exponent = factors.count(factor)
        grouped.extend([(factor, exponent)])
    grouped = sorted(set(grouped))
    return grouped

def format_join(grouped):
    """Formatted output: join factors and exponents."""
    joined = []
    for group in grouped:
        group = '^'.join(map(str, group))
        joined.extend([group])
    joined = ' * '.join(map(str, joined))
    return joined

def output(joined, columns, number, factors, divisor):
    """Show the result."""
    lennum = int(len(str(number)) + 3)
    lendiv = int(len(str(divisor)))
    columns = ''.join(map(str, columns))
    print()
    print(" " + ("-" * (lennum)) + ("-" * lendiv))
    print(columns)
    print('Factorization in prime factors:')
    print('>', number, '=', ' * '.join(map(str, factors)))
    print()
    print('Exponential form:')
    print('>', number, '=', joined)

def main():
    """Main program."""
    number = parse_arguments()
    columns, factors, divisor = decomposition(number)
    grouped = format_group(factors)
    joined = format_join(grouped)
    output(joined, columns, number, factors, divisor)

if __name__ == '__main__':
    main()
