def main():
    x = input("Hey!").strip().lower()
    bank(x)

def bank(n):
    if n[:5] == "hello":
        print("$0")
    elif(n[0] == "h"):
        print("$20")
    else:
        print("$100")

main()