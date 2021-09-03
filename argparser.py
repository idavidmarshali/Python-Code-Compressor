import os

usage = "---Usage : [Options] PATH"
name = "-Python Code Compressor"

class ArgParser:
    """
    Main class parsing the arguments of the console
    """
    class Help:
        def __init__(self):
            print(f"""       {name}-\n\nCompresses Python Raw Code using ';'\nPositional :\n\n PATH |> if not specified uses flags
Options:\n\n-h : --help |> Shows this help text
\n-t STRING : --text STRING |> to compress an string of python code instead of a file\n
-f PATH : --file PATH |> Path of a python file(.py) to compress\n\n\n Created by DavidMarshal®\n""")
    @classmethod
    def parse(cls, args: list[str]):
        if len(args) <= 1:
            print(f"\n{name}: No Arguments were specified\n{usage}\n -h or --help for more info\n")
            return
        if args[1] in ["-h", "--help"]:
            cls.Help()
            return
        elif args[1] in ["-t", "--text"]:
            return ''.join(args[2:])
        elif args[1] in ["-f", "--file"]:
            if os.path.isfile(nm := ''.join(args[2:])):
                with open(nm) as f:
                    return f.readlines()
            print(f"\n{name}: File ({nm}) was not found.\n")
        elif args[1].startswith("-"):
            print(f"\n{name}: Invalid Option ({args[1]}). use -h or --help for Info!\n")
        else:
            if os.path.isfile(nm := ''.join(args[1:])):
                with open(nm) as f:
                    return f.readlines()
            print(f"\n{name}: File ({nm}) was not found.\n")