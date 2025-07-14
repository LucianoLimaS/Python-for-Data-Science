# O PDF está meio ambiguo sobre o que precisa fazer.
# Ele pede para fazer o que está no retorno do print(filter.__doc__),
# porém pede para usar list comprehensions que deveria retornar uma lista

def ft_filter_list(function, iterable):
    """Filter an iterable with a function and return a list.

    Args:
        function: The function to apply to each item in the iterable.
                  If None, it filters for truthy values.
        iterable: The iterable to filter.

    Returns:
        A list containing only the items for which function(item) is true.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def ft_filter(function, iterable):
    """Filter an iterable with a function and return a generator.

    Args:
        function: The function to apply to each item in the iterable.
                  If None, it filters for truthy values.
        iterable: The iterable to filter.

    Yields:
        Items from the iterable for which function(item) is true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
