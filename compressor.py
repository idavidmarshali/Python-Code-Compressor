from typing import Optional; import sys; from argparser import ArgParser

class Compressor:
    """
    Main Compressor class in charge of compression

    classmethods :
        pars

        splitter
    """
    @classmethod
    def splitter(cls, string: str, sep: Optional[str] = " ") -> list[str]:
        """Splits the given string by the separator without removing it from the string!

        Arguments :
            {str} string -- string to be split

            {str} sep -- the separator character (white_space by default)

        Returns :
            {list} : a list containing the splitted string
        """
        __output = []
        __last_index = 0
        for index, character in enumerate(string):
            if character == sep:
                __output.append(string[__last_index:index])
                __last_index = index
        __output.append(string[__last_index:])
        return __output

    @classmethod
    def compress(cls, string: str) -> str:
        """Compresses the string given to it

        Argument :
            {str} string -- the string input that will be compressed

        Return :
            {str} : The compressed string
        """
        __splitted = string.split("\n")
        for index, string in enumerate(__splitted):
            __splitted_string = cls.splitter(string)
            __splitted_no_space = [c for c in __splitted_string if c != " " and c != '']
            if __splitted_no_space == [] or __splitted_no_space[0] == "":
                continue
            elif __splitted_no_space[0].replace(' ', '') in ["if", "for", "while", "else", "elif", "def", "class",
                                                            "case", "with"] or __splitted_no_space[0].replace(" ", "").startswith("@"):
                __splitted_string.append("\n")
                if index - 1 > 0 and not __splitted[index - 1].endswith("\n"):
                    __splitted_string.insert(0, "\n")
            elif __splitted_no_space[0].replace(' ', '') == "return":
                __splitted_string.append("\n")
            else:
                __splitted_string.append(";")
            __splitted[index] = ''.join(__splitted_string)
        return ''.join(__splitted)


if __name__ == "__main__":
    parsed = ArgParser.parse(sys.argv)
    if parsed is not None:
        compressed = Compressor.compress("".join(parsed))
        print(compressed)





