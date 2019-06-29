from .module_builder.interpreter import Interpreter
import sys
import cmd
from plantweb.render import render_file


class Main(cmd.Cmd):
    """Plant UML to Python Interpreter"""
    
    prompt = ">>>>"
    
    root_directory = None
    write_folder = None
    source_file = None
    db = None

    def cmdloop(self, intro="PlantUML to Python Convertor"):
        return cmd.Cmd.cmdloop(self, intro)

    def do_interpret(self, line):
        """
            ***
            Translates your SOURCE plantUML file to a python file
            in the ROOT directory provided
            Update ROOT directory: root [file_location]
            Update SOURCE file: source [source_file]
            ***
        """
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            uml = Interpreter()
            uml.add_file(self.source_file, self.write_folder)
            uml.write_modules()
            if len(uml.all_my_errors) > 0:
                for an_error in uml.all_my_errors:
                    print(an_error)
            print("Interpreting complete")
        
    def do_root(self, line):
        """Change the root directory"""
        self.root_directory = line
        if self.source_file:
            self.source_file = self.root_directory + "/" + self.source_file
        print(f"Root directory to read & write files is:  {line}")

    def do_write_folder(self, line):
        """Change the folder to write files directory"""

        if self.root_directory:
            self.write_folder = self.root_directory + "/" + line
            print(f"Folder to write files is: {self.root_directory}/{line}")
        else:
            self.write_folder = line
            print(f"Folder to write files is: {line}")
        
    def do_source(self, line):
        """Change the source file"""

        if self.root_directory:
            self.source_file = self.root_directory + "/" + line
            self.do_check_file(self.source_file)
        else:
            self.source_file = line
            self.do_check_file(self.source_file)

    def do_check_file(self, line):
        try:
            with open(self.source_file, "rt") as my_file:
                if my_file.read().find("@startuml") != -1:
                    if self.root_directory:
                        print(f"Source file to interpret is: {self.root_directory}/{line}")
                    else:
                        print(f"Source file to interpret is: {line}")
                else:
                    print("Error - File must contain plant UML")
        except FileNotFoundError:
            print("Error - File not found")
            print(f"looking for file at {self.source_file}")
        except Exception as e:
            print(e)

    def do_i_shelve(self, line):
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            uml_shelf = Interpreter()
            uml_shelf.add_file(self.source_file, self.write_folder)
            if self.root_directory:
                uml_shelf.shelve_modules(self.root_directory + "/" + line)
            else:
                uml_shelf.shelve_modules(line)
            print(f"modules shelved to {line}")

    def do_make_db(self, line):
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            uml_db = Interpreter()
            uml_db.add_file(self.source_file, self.write_folder)
            self.db = uml_db.create_db()

    def do_write_db(self, line):
        if self.db:
            self.db.read_db()
        else:
            print("please write to DB first (**make_db**)")

    def do_quit(self, line):
        print("Closing Down")
        return True

    def do_print_uml(self, line):
        with open(self.source_file, "rt") as my_file:
            contents = my_file.read()
        in_file = self.root_directory + "plant_uml.png"
        with open(in_file, 'wb') as fd:
            fd.write(contents.encode('utf-8'))
        print('==> INPUT FILE:')
        print(in_file)
        outfile = render_file(
            in_file,
            renderopts={
                'engine': 'plantuml',
                'format': 'png'
            },
            cacheopts={
                'use_cache': False
            }
        )
        print('==> OUTPUT FILE:')
        print(outfile)
        
    def help_interpret(self):
        print("Translates your SOURCE plantUML file to a python file")
        print("in the ROOT directory provided")
        print("Update ROOT directory: root [file_location]")
        print("Update SOURCE file: source [source_file]")
        
    def help_source(self):
        print("Update SOURCE file: source [source_file]")
        print("This file will be interpreted")

        
    def help_root(self):
        print("Update ROOT directory: root [file_location]")
        print("Files will be read and written to this location")

    def help_write_folder(self):
        print("The folder to which your files will be written")
        print("PLEASE create this folder prior to interpreting your file")

    def help_check_file(self):
        print("Use this function to check if your file is suitable for translation")

    def help_print_uml(self):
        print("Print your source PlantUML file to a PNG")

    def help_i_shelve(self):
        print("Store the class data in a \'shelf\' for later use")

    def help_make_db(self):
        print("Save the program data to a database")

    def help_write_db(self):
        print("Write the data saved in the database")

    def help_quit(self):
        print("Quit the program")

    def help_cmd(self):
        print("""
            ***Plant UML to Python Interpreter***
            
            check_file      Checks that the surce file is a text file and that it contains plantUML
            i_shelve        Shelves all the classes in the module as objects
            make_db         Write the module to a database
            write_db        Prints the information in the database
            source          Sets the source file to interpret
            write_folder    Sets the folder to write the module to
            interpret       Reads the source file, and writes each class to a seperate Python file
            print_uml       Prints a png file of the PlantUML diagram from the source file
            root            Change the root directory for the source file and written files
            quit            Quit the program
            """)


if __name__ == '__main__':

    if len(sys.argv) == 3:
        root_directory = sys.argv[1]
        source_file = sys.argv[2]
        if source_file.endswith(".txt"):
            x = Interpreter()
            x.add_file(source_file, root_directory)
            x.write_modules()
            if len(x.all_my_errors) < 1:
                print(f"Python files created in {root_directory}")
        else:
            print("Error - please select a text file")
    elif len(sys.argv) > 3:
            print("Error - please only input the source file followed by the write directory")
    else:
        Main().cmdloop()
