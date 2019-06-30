from .method import Method
from .attribute import Attribute
from .relationship import Relationship


class ClassBuilder:

    def __init__(self):
        self.name = ""
        self.all_my_attributes = []
        self.all_my_methods = []
        self.all_my_parent_classes = []
        self.all_my_composite_classes = []
        self.all_my_associated_classes = []

    def add_class_attributes(self, new_attributes):
        for an_attribute in new_attributes:
            new_a = Attribute(an_attribute.split(":")[0],
                              an_attribute.split(":")[1])
            self.all_my_attributes.append(new_a)

    def add_class_methods(self, new_methods):
        for a_method in new_methods:
            new_m = Method(a_method.split("(")[0],
                           a_method.split(")")[1],
                           a_method[
                           a_method.find("(") + 1:a_method.find(")")])
            self.all_my_methods.append(new_m)

    def add_relationships(self, new_relationships):
        for a_relationship in new_relationships:
            new_relationship = Relationship(a_relationship, self)
            new_relationship.add_relationship()

    def build_class(self, args):
        self.name = args[0]
        self.add_class_attributes(args[1])
        self.add_class_methods(args[2])
        self.add_relationships(args[3])

    def __str__(self):
        string = ""
        string += f"class {self.name}"
        if len(self.all_my_parent_classes) > 0:
            for a_class in self.all_my_parent_classes:
                string += f"({a_class})"
        string += ":\n\n    def __init__(self):\n"
        for x in self.all_my_attributes:
            string += f"{x}"
        if len(self.all_my_composite_classes) > 0:
            for a_class in self.all_my_composite_classes:
                string += f"        self.all_my_{a_class} = []\n"
        string += "\n"
        for x in self.all_my_methods:
            string += f"{x}"
        return string

    def print_class(self):
        return self.__str__()
