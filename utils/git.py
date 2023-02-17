import os

from simple_term_menu import TerminalMenu


def get_last_commits():
    stream = os.popen("git log --oneline -n 10")
    output = stream.read()
    return [commit for commit in output.strip().split("\n") if commit]


def get_git_user_name():
    stream = os.popen("git config --get user.name")
    output = stream.read()
    return output.strip()


def get_last_branches():
    stream = os.popen(
        f"git for-each-ref --sort=-committerdate "
        f"--format='%(author) | %(committerdate) | %(refname:short)' "
        f"refs/heads/ "
        f"| grep -i {get_git_user_name().split()[0]} "
        f"| head -n 10"
    )
    output = stream.read()
    return [
        branch.split("|")[2].strip()
        for branch in output.strip().split("\n")
        if branch.split("|")[2].strip()
    ]


def show_git_menu(options, command_template, needs_confirmation=True):
    if not options:
        print("No options found.")
        return
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        return
    if type(menu_entry_index) is not int:
        print("Not a valid option.")
        return
    selected_line = options[menu_entry_index]
    selected_option_first_word = selected_line.split(" ")[0]
    command = command_template.format(option=selected_option_first_word)

    print(f"\nWill execute:\n\n\t{command}\n")

    if needs_confirmation:
        confirmation = input("Ok to proceed? Y/n")
        if confirmation.lower() == "y" or not confirmation:
            os.system(command)
    else:
        os.system(command)
