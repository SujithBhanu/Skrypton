val=input("Enter your String : ")
val2=val[::-1]
if val==val2:
    print(f"As the given word : {val} and reversed word : {val2} are same")
    print(f"The given word {val} is a PALINDROME")
else:
    print(f"As the given word : {val} and reversed word : {val2} are not same")
    print(f"The given word {val} is not a PALINDROME")