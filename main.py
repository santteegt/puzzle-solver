#!/usr/bin/env python3
"""
Rooftop Challenge
"""

__author__ = "Santiago Gonzalez"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging

from api import check_puzzle, fetch_puzzle_by_email, request_counter
from puzzle import check


logging.basicConfig(level=logging.INFO)


def main(args):
    """ Entry point """
    try:
        print('Feching.......')
        puzzle = fetch_puzzle_by_email(args.email)
        print('Puzzle Fethed!')
        if puzzle:
            print('Solving.......')
            sorted_blocks = check(puzzle['data'].copy(), puzzle['api_token'])
            answer = ''.join(sorted_blocks)
            print('Got it! Let me verify my answer......')
            solved = check_puzzle(answer, puzzle['api_token'])
            print('=====================================')
            print('=========== Puzzle Solver ===========')
            print('============== RESULTS ==============')
            print('=====================================')
            print('Puzzle:', answer)
            print('----------------------')
            print('Solved?', '🎉 SUCESS 🎉' if solved else '👎 No 👎')
            print('----------------------')
            print('Total API requests:', request_counter())
            print('=====================================')
            print('=====================================')
        else:
            logging.error('Failed to fetch a puzzle for given email')
    except Exception as err:
        logging.error('An internal error has occurred: {}'.format(err))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(
        description="Puzzle Solver. I'll solve a puzzle if you feed me your email address",
        prog='PuzzleSolver'
    )
    parser.add_argument("-e", "--email", help="An email address to use the API", required=True)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
