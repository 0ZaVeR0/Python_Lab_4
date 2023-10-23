memory = {}

def remember(functions):
    def save_args(*args):
        #print("args >> ", args)
        try:
            if args[1:] in memory.values():
                raise Exception("Class already exist")
        except Exception as e:
            print(e)
            exit(-1)

        memory[args[0]] = args[1:]
        print("memory >> ", memory)
        functions(*args)

    return save_args    