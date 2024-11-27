message = input("Enter your message: ")

if(("Make a lot of money" in message) or  ("buy now" in message) or ("subscribe this" in message) or ("click this" in message)):
    print("Spam Comment!")
else:
    print("Valid Comment!")