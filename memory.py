memory = {}

def remember(functions):
    def save_args(*args):
        print("args >> ", args)
        if args[1:] in memory.values():
            print("Identical Shape already exist")
            exit (-1)

        memory[args[0]] = args[1:]
        print("memory >> ", memory)
        functions(*args)

    return save_args    