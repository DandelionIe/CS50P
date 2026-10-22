def main():
    ans = input("What's The Answer to the Great Question?").strip()
    deep(ans)

def deep(a):
    if a == "42" or a.lower() == "forty-two" or a.lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()