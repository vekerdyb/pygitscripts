#!/usr/bin/env python3
import argparse

from utils import get_last_commits, show_git_menu


def main(add_all=False):
    options = get_last_commits()
    maybe_add_all = ""
    if add_all:
        maybe_add_all = "git add --all && "
    show_git_menu(options, maybe_add_all + "git commit --fixup {option}")


if __name__ == "__main__":
    # use argparse to get an optional 'add' argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--add-all",
        action="store_true",
        help="add all files before commiting",
    )
    args = parser.parse_args()
    main(args.add_all)
