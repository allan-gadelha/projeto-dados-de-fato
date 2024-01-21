def create_list_of_lists_from_strings(strings_list: list,
                                      sep: str) -> list:
    """
    Makes a list of list-shaped strings become a list of lists of strings.
    """
    return [row.split(sep) if row else 'empty' for row in strings_list]


def flatten(nested_list: list) -> list:
    """
    Blows up a list of lists.
    """
    return [item for sublist in nested_list for item in sublist]


def create_unique_languages_list(raw_list: list,
                                 sep: str) -> list:
    """
    Creates a list of unique languages from a list of list-shaped strings.
    """
    list_of_lists = create_list_of_lists_from_strings(raw_list, sep)

    flattened_list = flatten(list_of_lists)

    return list(set(flattened_list))
