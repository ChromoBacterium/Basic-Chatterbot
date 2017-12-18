while True:
    userInput = input(">>>")
    if userInput in ['hello','HELLO','Hello','HAI']:
        print("Hello")
    if userInput in ['bye']:
        print("Bye")
    else:
        print("I did not understand what you said.")
