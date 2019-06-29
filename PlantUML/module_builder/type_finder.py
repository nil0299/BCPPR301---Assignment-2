class TypeFinder:

    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            return "str"
        elif "number" in new_type:
            return "int"
        elif "list" in new_type:
            return "list"
        elif "tuple" in new_type:
            return "tuple"
        else:
            return ""