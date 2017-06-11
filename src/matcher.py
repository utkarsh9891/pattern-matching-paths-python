class Matcher:
    """
    Set of functions to match a path against a pattern
    """
    @classmethod
    def get_closest_matching_pattern_for_path(cls, path, pattern_group=None, patterns=None):
        """
        Returns the closest match of a path from a list of patterns
        :param path: the path to match the patterns against
        :param pattern_group: the pattern group to use for selecting patterns on basis of length
        :param patterns: if pattern group is not passed in, this parameter is used as source of patterns to be matched
        :return: the pattern object that best matches the requested path
        """
        if pattern_group:
            patterns = pattern_group.pattern_map[path.length]

        matching_patterns = cls.get_matching_patterns(path=path, patterns=patterns)
        closest_match = cls.closest_matching_pattern(matching_patterns=matching_patterns)
        return closest_match

    @classmethod
    def get_matching_patterns(cls, path, patterns=None):
        """
        gets list of all patterns that match the path
        :param path: path object to match the patterns against
        :param patterns: list of patterns from which matching aptterns are to be filtered
        :return: list of matching patterns
        """
        patterns = patterns or []
        matches = []
        for pattern in patterns:
            if pattern.matches_path(path_obj=path):
                matches.append(pattern)

        return matches

    @classmethod
    def closest_matching_pattern(cls, matching_patterns=None):
        """
        gets the closest matching pattern from a list of already matching pattern
        :param matching_patterns: list of patterns that matched a path
        :return: the closest matched pattern
        """
        if not matching_patterns:
            return None

        if len(matching_patterns) == 1:
            return matching_patterns[0]

        # sort the patterns in ascending order by wildcard count & weight to get the closest match on first position
        sorted_matches = sorted(matching_patterns,
                                key=lambda pattern: (pattern.wildcard_count, pattern.wildcard_weight))
        return sorted_matches[0]
