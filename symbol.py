def symbol(data):
    """
    This function is used to handel symbol use due to speech recognition
    For getting any symbol in python you must say......
        symbol (_______) followed by symbol name

    Symbol currently included are:-
    +, -, ., #, *, %, !,
    """
    if "dot" in data.lower():
        return "."
    elif "hash" in data.lower():
        return "#"
    elif "plus" in data.lower() or "+" in data:
        return "+"
    elif "minus" in data.lower() or "-" in data:
        return "-"
    elif "equal" in data.lower() or "equal to" in data or "=" in data:
        return "="
    elif "multiply" in data.lower()or "multiplication" in data.lower() or "*" in data:
        return "*"
    elif "modulo" in data.lower() or "percentage" in data.lower() or "%" in data:
        return "%"
    elif "not in" in data.lower() or "exclamation" in data.lower() or "!" in data:
        return "!"
