import re


class RelationshipFinder:

    @classmethod
    def find_relationship(cls, relationship, class_name):
        if relationship.startswith(class_name):
            related_class = relationship.split(" ")[4]
            if re.search(r"\*--", relationship):
                return tuple(("comp", related_class))
            if re.search(r"--", relationship):
                return tuple(("assos", related_class))
        elif relationship.endswith(class_name):
            if re.search(r"<\|--", relationship):
                ext_class = relationship.split(" ")[0]
                return tuple(("extends", ext_class))