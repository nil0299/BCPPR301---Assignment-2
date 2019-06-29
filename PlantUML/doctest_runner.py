# Runs all individual doctest files

def test():
    import doctest
    doctest.testfile('doc_tests/attribute_doctest', verbose=1)
    doctest.testfile('doc_tests/class_builder_doctest', verbose=1)
    doctest.testfile('doc_tests/interpreter_doctest', verbose=1)
    doctest.testfile('doc_tests/method_doctest', verbose=1)
    doctest.testfile('doc_tests/module_doctest', verbose=1)
    doctest.testfile('doc_tests/relationship_doctest', verbose=1)
    doctest.testfile('doc_tests/doctest_controller', verbose=1)


if __name__ == "__main__":
    test()
