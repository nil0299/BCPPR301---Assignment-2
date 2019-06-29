import unittest
from interpreter.controller import Main


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.root = 'c:/test'
        self.source = 'class_diagram_plantUML'
        self.write_folder = 'test_result'
        self.controller = Main()

    def tearDown(self):
        print('DOWN')

    def test_18(self):
        self.controller.do_quit('')
        assert True

    def test_17(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        self.controller.do_write_folder(self.write_folder)
        self.controller.do_write_db('')
        assert "please write to DB first (**make_db**)"

    def test_16(self):
        self.controller.do_root(self.root)
        self.controller.do_make_db('')
        assert "Please enter the source file : source xxxx"

    def test_15(self):
        self.controller.do_make_db('')
        assert "Please enter the directory to write files to : write_folder xxxx"

    def test_14(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        self.controller.do_i_shelve('test_folder')
        assert "modules shelved to test_folder"

    def test_13(self):
        self.controller.do_root(self.root)
        self.controller.do_i_shelve('')
        assert "Please enter the source file : source xxxx"

    def test_12(self):
        self.controller.do_i_shelve('')
        assert "Please enter the directory to write files to : write_folder xxxx"

    def test_11(self):
        self.controller.do_root(self.root)
        self.controller.do_source('wrong')
        self.controller.do_check_file('')
        assert "Error - File not found"

    def test_10(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        self.controller.do_check_file('')
        assert f"Source file to interpret is: {self.root}/{self.source}"

    def test_09(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        self.controller.do_write_folder(self.write_folder)
        self.controller.do_interpret('')
        assert "Interpreting Complete"

    def test_08(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        self.controller.do_write_folder(self.write_folder)
        assert self.controller.write_folder is not None

    def test_07(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        assert self.controller.write_folder is None

    def test_06(self):
        self.controller.do_root(self.root)
        self.controller.do_source(self.source)
        assert self.controller.source_file is not None

    def test_05(self):
        self.controller.do_root(self.root)
        assert self.controller.source_file is None

    def test_04(self):
        self.controller.do_root(self.root)
        assert self.root is self.controller.root_directory

    def test_03(self):
        self.controller.do_root(self.root)
        self.controller.do_source('blank.txt')
        assert "Error - File must contain plant UML"

    def test_02(self):
        self.controller.do_root(self.root)
        self.controller.do_source('wrong')
        assert "Error - File not found"

    def test_01(self):
        assert self.controller.root_directory is None


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
