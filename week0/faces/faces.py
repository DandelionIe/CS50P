def main():
    message = convert(input("Input your message: "))
    print(message)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

main()