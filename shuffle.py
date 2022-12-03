#!/usr/bin/env python
""" Randomizes the lines of a text file and writes the randomized lines as a new text file """

import random
import argparse


def main(args: argparse.Namespace) -> None:
    corpus_list = []
    with open(input, "r") as source:
        for line in source:
            stripped_line = line.rstrip()
            corpus_list.append(stripped_line)


    random.seed(seed)
    random.shuffle(corpus_list)


    with open(output, "w") as sink:
        for line in corpus_list:
            print(line, file=sink)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path to the file to be shuffled.")
    parser.add_argument("output", help="path to the shuffled file.")
    parser.add_argument("--seed", type=int, help="")
    main(parser.parse_args())