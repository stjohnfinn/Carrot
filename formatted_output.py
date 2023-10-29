import rich

def p_info(msg, end="\n"):
    rich.print('[gray]' + msg + '[/gray]', end=end)

def p_instruct(msg, end="\n"):
    rich.print('[underline magenta]' + msg + '[/underline magenta]', end=end)

def p_warn(msg, end="\n"):
    rich.print('[bold red]' + msg + '[/bold red]', end=end)

def akc():
    '''
    Any Key Continue operation. Tells the user to press any key to continue and then accepts input of any key.
    '''
    p_instruct("Press any key to continue...", end="")
    input()