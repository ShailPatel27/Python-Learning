for i in range(1, 21): 
    for j in range(1, 11):
        table = f"{i} X {j} = {i*j}"
        
        with open(f"F:\\Python\\codewithharry\\Chapter9(File IO)\\tables\\table_{i}.txt", "a") as f:
            f.write(f"{table}\n")