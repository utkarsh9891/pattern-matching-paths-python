from collections import defaultdict

from path import Path


class Pattern:
    """
    The matching pattern object to be used for validation against Paths
    """
    SEPARATOR = ','
    WILDCARD = '*'

    def __init__(self, input_pattern):
        """
        initializes the pattern with the input string passed in
        :param input_pattern: a string value representing a match pattern e.g. w,x,*,*

        self.pattern is set as the array representation of the input string e.g. ['w', 'x', '*', '*']
        self.wildcard_pattern is set as the array representation of the wildcard occurrences e.g. ['0', '0', '1', '1']
        self.wildcard_weight is set as the numeric representation of the wildcard occurrence map e.g. 3 above
            >> in case of a conflict between two patterns with same number of wildcards, the one with a lower weight
                is a closer match
        """
        self.input_pattern = input_pattern
        self.pattern = input_pattern.split(self.SEPARATOR)
        self.wildcard_pattern = ['1' if item is self.WILDCARD else '0' for item in self.pattern]
        self.wildcard_weight = int(''.join(self.wildcard_pattern), 2)

    @property
    def length(self):
        return len(self.pattern)

    @property
    def wildcard_count(self):
        return self.wildcard_pattern.count('1')

    def matches_path(self, path_obj):
        """
        validates if the pattern matches the requested path
        :param path_obj: a path object to match this pattern against
        :return: Boolean return on basis of pattern match succeeds or fails
        """
        if not isinstance(path_obj, Path):
            return False

        if self.length != path_obj.length:
            return False

        for pattern_item, path_item in zip(self.pattern, path_obj.path):
            if pattern_item not in [path_item, self.WILDCARD]:
                # pattern item does not match path item and is not a wildcard
                return False

        return True


class PatternGroup:
    """
    Groups of patterns on basis of their lengths
    """
    def __init__(self, patterns=None):
        """
        initializes a pattern group. if patterns are passed in, they are added to respective group maps
        :param patterns: the patterns to initialize the groups with
        """
        self.pattern_map = defaultdict(list)
        if patterns:
            for pattern in patterns:
                self.add_pattern(pattern=pattern)

    def add_pattern(self, pattern):
        """
        adds a pattern to the respective length map
        :param pattern: the pattern object being added to the group
        :return: None
        """
        self.pattern_map[pattern.length].append(pattern)
