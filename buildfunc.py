def func(data):
    data = data.lower()
    print("1", data)
    data = data.strip("define function ")
    print("2", data)
    data = data.replace(" ","_")
    print("3", data)
    return "def " + data+"()"
