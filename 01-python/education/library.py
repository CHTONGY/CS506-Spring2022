import tools
def draw_library():
    # print("library not found")
    name = 'library'
    name_len = len(name)
    # print('-----------')
    tools.print_row(name_len)
    # print('| library |')
    tools.print_name(name)
    # print('-----------')
    tools.print_row(name_len)
    return