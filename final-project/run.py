from pathlib import Path
from shutil import copytree, copy, move, rmtree
from time import ctime
import os

def confirm():
    choice = input("Do you want to proceed? y/n: ")
    return choice == 'y'

def bytes_to_human_readable(size):
    suffix = "B"
    if size > 1024:
        size /= 1024
        suffix = "KB"
    if size > 1024:
        size /= 1024
        suffix = "MB"
    if size > 1024:
        size /= 1024
        suffix = "GB"
    if size > 1024:
        size /= 1024
        suffix = "TB"
    size = round(size, 2)
    return f"{size} {suffix}"
    # Anything larger is fine to keep in TB.

class CurrDir:
    directory = ""
    # 'choices' is a dictionary where: key is the number you can choose,
    # the key is a tuple of (filetype, absolute path, displayed path)
    choices = {}

    def __init__(self, path):
        self.directory = Path(path).resolve()
        self.choices = {}

    # Directory Functions
    def ls_dir(self):
        self.choices = {
            0: ("D", Path(self.directory), ". (current directory)"),
            1: ("D", Path(self.directory.parent), ".. (parent directory)")
        }
        for i, child in enumerate(self.directory.iterdir()):
            filetype = "F"
            if child.is_dir():
                filetype = "D"
            self.choices[i + 2] = (filetype, child.resolve(), child.name)
        # Now, print 'self.choices':
        for i in self.choices.keys():
            print(f"{i} ({self.choices[i][0]}): {self.choices[i][2]}")

    def ch_dir(self, new_dir):
        new_dir = Path(new_dir).resolve()
        if new_dir.exists():
            self.directory = new_dir
        else:
            print("That directory doesn't exist!")

    def mk_dir(self, dirname):
        new_dir = Path(dirname).resolve()
        try:
            new_dir.mkdir()
        except FileExistsError:
            print("That file or folder already exists.")
            return
        except FileNotFoundError:
            print("You tried to make a directory in a non-existing parent directory!")
            print("Make the parent directory first.")

    def mv_dir(self, dir_from, dir_to):
        dir_from = Path(dir_from).resolve()
        dir_to = Path(dir_to).resolve()
        if dir_to.exists() and dir_to.is_file():
            print(str(dir_to), "already exists as a file!")
            return
        if dir_from.samefile(self.directory):
            print("You can't move the current directory!")
            return
        print("You are about to move", str(dir_from), "to", str(dir_to))
        if confirm():
            move(dir_from, dir_to)

    def copy_dir(self, dir_from, dir_to):
        dir_from = Path(dir_from).resolve()
        dir_to = Path(dir_to / (dir_from.name)).resolve()
        if dir_to.exists() and dir_to.is_file():
            print("The 'to' option can't already exist as a file!")
            return
        if not dir_from.exists():
            print("The 'from' option must exist in order to copy it!")
            return
        if not dir_from.is_dir():
            print("The 'from' option must be a directory, not a file!")
            return
        if dir_from.exists() and dir_to.exists() and dir_from.samefile(dir_to):
            # Shouldn't reach this anyway since dir_to can't exist
            print("You can't copy a directory into itself!")
            return
        print("You are about to copy", str(dir_from), "to", str(dir_to))
        if confirm():
            try:
                copytree(dir_from, dir_to, dirs_exist_ok=True)
            except FileExistsError:
                print("That file already exists?")
    def rm_dir(self, dirname):
        dirname = dirname.resolve()
        if not dirname.exists() or dirname.is_file():
            print("You must name a directory, and it must exist")
            return
        if self.directory.samefile(dirname):
            print("You can't delete the current directory!")
            return
        print("You are about to delete", str(dirname), "and everything in it.")
        if confirm():
            rmtree(dirname)


    # File functions:
    def mk_file(self, filename):
        filename = filename.resolve()
        if filename.exists():
            print("That file already exists!")
            return
        open(filename, mode = 'x')

    def file_details(self, filename):
        f = filename.resolve()
        if not f.exists():
            print("File doesn't exist!")
            return
        last_mod = ctime(os.path.getmtime(f))
        size = bytes_to_human_readable(os.path.getsize(f))
        print()
        print("--------------------")
        print("Filename:", str(f))
        print("Last modified:", last_mod)
        print("Size:", size)
        print("--------------------")
        print()

    def mv_file(self, file_from, file_to):
        file_from = file_from.resolve()
        file_to = file_to.resolve()
        if file_to.exists() and not file_to.is_dir():
            print("The 'to' file already exists!")
            return
        move(file_from, file_to)

    def copy_file(self, file_from, file_to):
        file_from = file_from.resolve()
        file_to = file_to.resolve()
        if file_to.exists() and not file_to.is_dir():
            print("The 'to' file already exists!")
            return
        copy(file_from, file_to)

    def rm_file(self, filename):
        filename = filename.resolve()
        if not filename.exists():
            print("That file doesn't exist!")
            return
        if filename.is_dir():
            print("That's a directory, not a file!")
            return
        print("You are about to remove:", filename)
        if confirm():
            filename.unlink()

def print_menu():
    print("0. Exit")
    print("1. Change Directory")
    print("2. Make New Directory")
    print("3. Create New File")
    print("4. Cut")
    print("5. Copy")
    print("6. Paste")
    print("7. Delete")
    print("8. Show File/Directory Information")


# Clipboard contains (filetype, fullpath, operation)
# filetype "X" means nothing in clipboard
# operation can be either "C" for copy or "M" for move
clipboard = ("X", "", "")

def make_choice(wd, choice):
    global clipboard
    select1 = False
    if choice == 1:
        #cd
        select1 = int(input("Enter directory number: "))
        wd.ch_dir(wd.choices[select1][1])
    if choice == 2:
        #mkdir
        name = input("Enter the name for the new directory: ")
        wd.mk_dir(wd.directory / name)
    if choice == 3:
        #mk file
        name = input("Enter the new file's name: ")
        wd.mk_file(wd.directory / name)
    if choice == 4:
        #cut (put in clipboard to MOVE)
        select1 = int(input("Enter the number of the file/folder to cut: "))
        filetype = ""
        if wd.choices[select1][1].is_dir():
            filetype = "D"
        else:
            filetype = "F"
        clipboard = (filetype, wd.choices[select1][1], "M")
    if choice == 5:
        #copy (put in clipboard to COPY)
        select1 = int(input("Enter the number of the file/folder to copy: "))
        filetype = ""
        if wd.choices[select1][1].is_dir():
            filetype = "D"
        else:
            filetype = "F"
        clipboard = (filetype, wd.choices[select1][1], "C")
    if choice == 6:
        if clipboard[0] == "X":
            print("There is nothing in the clipboard!")
            return
        if clipboard[0] == "F":
            if clipboard[2] == "C":
                wd.copy_file(clipboard[1], wd.directory)
            elif clipboard[2] == "M":
                wd.mv_file(clipboard[1], wd.directory)
        elif clipboard[0] == "D":
            if clipboard[2] == "C":
                wd.copy_dir(clipboard[1], wd.directory)
            elif clipboard[2] == "M":
                wd.mv_dir(clipboard[1], wd.directory)
        clipboard = ("X", "", "")
    if choice == 7:
        # rm (-r for dir)
        select1 = int(input("Enter the number of the file/folder to delete: "))
        if wd.choices[select1][1].is_dir():
            wd.rm_dir(wd.choices[select1][1])
        else:
            wd.rm_file(wd.choices[select1][1])
    if choice == 8:
        #print info
        select1 = int(input("Enter the number of the file/folder to view info: "))
        wd.file_details(wd.choices[select1][1])


def main():
    # Make sure that any files passed into CurrDir functions are ABSOLUTE paths!
    # Check for relative paths (no leading /, leading ./ or ../) before passing in
    # also check for windows relpath (not starting with C:\ or other drive letter)
    curr_dir = CurrDir('.')
    going = True
    while going:
        print()
        print_menu()
        print()
        print("Current directory:", str(curr_dir.directory))
        curr_dir.ls_dir()
        print()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            going = False
            continue
        make_choice(curr_dir, choice)

main()
