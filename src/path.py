class Path:
    """
    The class definition for the Path wrt which the patterns are to be matched
    """
    SEPARATOR = '/'

    def __init__(self, input_path):
        """
        initializes the path with the input string passed in
        :param input_path: a string value representing a path e.g. /w/x/y/z/

        self.path is set as the array representation of the input string e.g. ['w', 'x', 'y', 'z']
        """
        self.input_path = input_path
        self.path = list(filter(None, input_path.split(self.SEPARATOR)))

    @property
    def length(self):
        return len(self.path)
