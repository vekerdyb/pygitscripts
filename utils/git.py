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
        f"git reflog show --date=iso | grep 'checkout: moving from'" f"| head -n 100"
    )
    output = stream.read()

    formatted_options = sorted(
        [
            {"date": branch.split("{")[1][:19], "branch": branch.split(" ")[-1]}
            for branch in output.strip().split("\n")
        ],
        key=lambda x: x["date"],
        reverse=True,
    )

    single_branch_options = []
    branches_seen = set()
    for formatted_option in formatted_options:
        if formatted_option["branch"] not in branches_seen:
            single_branch_options.append(
                f"{formatted_option['date']}: {formatted_option['branch']}"
            )
            branches_seen.add(formatted_option["branch"])

    return single_branch_options[:10]


def show_git_menu(
    options,
    command_template,
    needs_confirmation=True,
    get_command_param_from_selected_option=(
            lambda selected_line: selected_line.split(" ")[0]
    ),
):
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
    selected_option = get_command_param_from_selected_option(selected_line)
    command = command_template.format(option=selected_option)

    print(f"\nWill execute:\n\n\t{command}\n")

    if needs_confirmation:
        confirmation = input("Ok to proceed? Y/n")
        if confirmation.lower() == "y" or not confirmation:
            os.system(command)
    else:
        os.system(command)
