#!/usr/bin/env python3
from utils import get_last_branches, show_git_menu


def main():
    options = get_last_branches()

    def get_command_param_from_selected_option(selected_line):
        return selected_line.split(": ")[1]

    show_git_menu(
        options,
        "git checkout {option}",
        needs_confirmation=False,
        get_command_param_from_selected_option=get_command_param_from_selected_option,
    )


if __name__ == "__main__":
    main()
