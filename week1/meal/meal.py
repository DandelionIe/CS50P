def main():
    time = convert(input("Enter the time: ").strip())
    
    if 7 <= time <= 8:
        print("breakfast time")
    elif  12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    ch = (time + " ").split(" ")
    time = ch[0]
    ap = ch[1]
    h, m = time.split(":")
    if ap == "a.m." or ap == "p.m.":h = int(h) % 12 

    if ap == "p.m.":
        h += 12
        con = float(h) + float(m)/60.0
    else:
        con = float(h) + float(m)/60.0

    return con


if __name__ == "__main__":
    main()