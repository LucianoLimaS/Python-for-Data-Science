def NULL_not_found(object: any) -> int:
    type_name = type(object)
    if object is None:
        print(f"Nothing: {object} {type_name}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type_name}")

    # Em Python, 0 é considerado False em contextos booleanos
    # Portanto, 0 e False são equivalentes em termos de valor booleano
    # No entanto, eles são de tipos diferentes: int e bool, respectivamente
    # por isso este código verifica se o objeto é um int e não é False
    elif isinstance(object, int) and not(object is False) and object == 0:
        print(f"Zero: {object} {type_name}")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {type_name}")
    elif isinstance(object, bool) and not object:
        print(f"Fake: {object} {type_name}")
    else:
        print("Type not Found")
    return 1


if __name__ == "__main__":
    """ Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian")) """

""" Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
 """
