from .relationship_finder import RelationshipFinder

class ClassFinder:

    class_list = []

    @classmethod
    def find_classes(cls, class_content_list, relationship_content):
        for class_info in class_content_list:
            class_name = class_info.split(' ')[1]
            info = class_info.split("\n")
            attributes = [line for line in info if line.find(":")
                          is not -1 and line.find("(") is -1]
            methods = [line for line in info if line.find("(") is not -1]
            relationships = [RelationshipFinder.find_relationship(relationship,
                                                                  class_name)
                             for relationship in
                             relationship_content.split("\n") if
                             RelationshipFinder.find_relationship(relationship,
                                                                  class_name)]
            new_tuple = (class_name, attributes, methods, relationships)
            cls.class_list.append(new_tuple)
        return cls.class_list