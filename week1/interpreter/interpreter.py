def main():
    f, how, l = input("input it:").strip().split(" ")
    interpreter(f, how, l)

def interpreter(x, h, y):
    match h:
        case "+":
            print(float(x) + float(y))
        case "-":
            print(float(x) - float(y))
        case "*":
            print(float(x) * float(y))
        case "/":
            print(float(x) / float(y))
        case _:
            return

main()