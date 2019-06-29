from shelve import open


class Shelver:


    def __init__(self, shelf_file):
        self.my_shelf_file = shelf_file
        self.all_my_shelved_modules = []

    def shelve_modules(self, new_module):
        with open(self.my_shelf_file) as d:
            d[new_module.write_files()[0]] = new_module
