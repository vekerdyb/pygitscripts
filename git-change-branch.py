#!/usr/bin/env python3
from utils import get_last_branches, show_git_menu


def main():
    options = get_last_branches()
    show_git_menu(options, "git checkout {option}", needs_confirmation=False)


if __name__ == "__main__":
    main()
