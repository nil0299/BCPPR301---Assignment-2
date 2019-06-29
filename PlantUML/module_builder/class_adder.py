from module_builder.class_builder import ClassBuilder


class ClassAdder:

    @classmethod
    def add_class(cls, args):
        new_class = ClassBuilder()
        new_class.build_class(args)
        return new_class