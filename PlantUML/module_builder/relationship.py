class Relationship:

    """Builds the class relationship data"""

    def __init__(self, new_type):
        self.name = new_type[1].lower()
        self.type = new_type[0]

    def __str__(self):
        return f"{self.name}s"
