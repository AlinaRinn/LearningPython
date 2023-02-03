import json

def Dictionary():
    d = {'t': -18, 'b': -5, 'h': -18, 'y': 16, 'a': 6}
    print(d.keys())
    c = {'kak': 11, 'tak': 22, 't': -88}
    d = {**d, **c}
    print(d.items())
    a = [2, 2, 8, 8]
    d["a"] = a
    with open("js.json", "w") as file:
        file.write(json.dumps(d))

def Exception(a, b):
    try:
        print(a / b)
    except TypeError:
        print("Type Error")
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print("No error")
    finally:
        print("Nice try")

Dictionary()
Exception(10, 0)




