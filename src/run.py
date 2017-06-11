from path import Path
from pattern import Pattern, PatternGroup
from matcher import Matcher


class PatternMatchingPaths:
    """
    Driver class for this project
    """
    @classmethod
    def get_inputs(cls):
        """
        Gets the input from stdin
        :return: the inputs retrieved & then grouped into corresponding objects
        num_patterns -- the number of patterns
        pattern_group -- the PatternGroup generated for the input patterns
        num_paths -- the number of paths input
        paths -- the list of Path objects for the input paths
        """
        num_patterns = int(input())
        pattern_group = PatternGroup()
        for i in range(num_patterns):
            pattern = cls.get_input_object(object_type=Pattern)
            pattern_group.add_pattern(pattern)

        num_paths = int(input())
        paths = []
        for i in range(num_paths):
            paths.append(cls.get_input_object(object_type=Path))

        return num_patterns, pattern_group, num_paths, paths

    @classmethod
    def get_input_object(cls, object_type):
        return object_type(input().strip())

    @classmethod
    def run(cls):
        """
        the driver function that retrieves input from stdin for patterns & paths & prints the result to stdout
        :return: None
        """
        num_patterns, pattern_group, num_paths, paths = cls.get_inputs()
        for path in paths:
            closest_match = Matcher.get_closest_matching_pattern_for_path(path=path,
                                                                          pattern_group=pattern_group)
            print(closest_match.input_pattern if closest_match else 'NO MATCH')


if __name__ == '__main__':
    PatternMatchingPaths.run()
