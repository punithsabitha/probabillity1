print("Guess the Event Type")

print("Type: dependent / independent / mutually exclusive / not mutually exclusive")

score = 0

print("\n1. Tossing a coin twice")
ans1 = input("Your answer: ")
if ans1 == "independent":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\n2. Picking 2 cards without replacement")
ans2 = input("Your answer: ")
if ans2 == "dependent":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\n3. Getting 1 and 6 on a die at same time")
ans3 = input("Your answer: ")
if ans3 == "mutually exclusive"
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\n4. Getting a red card or king")
ans4 = input("Your answer: ")
if ans4 == "not mutually exclusive":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\nScore:", score)
print("End of game")