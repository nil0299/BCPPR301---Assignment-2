from module_builder.module import Module


class ModuleAdder:

    @classmethod
    def add_module(cls, new_module_name, new_classes):
        new_module = Module()
        new_module.create_module(new_module_name, new_classes)
        return new_module