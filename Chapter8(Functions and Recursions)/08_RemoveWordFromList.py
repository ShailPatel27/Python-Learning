def rem(l, word):
    for i in l:
        l.remove(word)
        return l
        

l = ["Shail", "Raj", "Mohit", "Shubham", "Meet"]
word = input("Enter a name: ")
print(rem(l, word))