def main():
    x = input("input it:").strip().lower().split(".")[-1]
    extensions(x)

def extensions(n):
    match n:
        case "gif" | "jpeg" | "png":
            print("image/" + n)
        case "jpg":
            print("image/jpeg")
        case "pdf" | "zip":
            print("application/" + n)
        case "txt":
            print("text/plain")
        case "mp4":
            print("video/mp4")
        case "csv":
            print("text/csv")
        case _:
            print("application/octet-stream")

main()