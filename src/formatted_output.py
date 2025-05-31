import rich

def p_info(msg, end="\n"):
    rich.print('[gray]' + msg + '[/gray]', end=end)

def p_instruct(msg, end="\n"):
    rich.print('[underline blue]' + msg + '[/underline blue]', end=end)

def p_warn(msg, end="\n"):
    rich.print('[bold red]' + msg + '[/bold red]', end=end)

def enter_to_continue(msg="Press enter to continue..."):
    rich.print('[dim]' + msg + '[/dim]', end="")
    input()