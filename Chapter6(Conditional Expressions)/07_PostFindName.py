post = input("Enter post: ")
name = input("Enter Name: ")

if(name.lower() in post.lower()):
    print(f"This post is talking about {name}")
else:
    print(f"This post is not talking about {name}")