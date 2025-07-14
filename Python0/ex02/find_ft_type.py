def all_thing_is_obj(obj: any) -> int:
    """Prints the type of an object.

    Args:
        obj: The object to check.

    Returns:
        An integer value.
    """
    type_name = type(obj).__name__[0].upper() + type(obj).__name__[1:]
    if isinstance(obj, (list, tuple, set, dict)):
        print(f"{type_name} : {type(obj)}")
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen: {type(obj)}")
    else:
        print("Type not found")
    return 42


"""if __name__ == "__main__":
     ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10)) """
