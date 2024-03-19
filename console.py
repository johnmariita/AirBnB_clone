#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, line):
        """End of File signal that exits the program
        """
        print("End of File encountered")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
