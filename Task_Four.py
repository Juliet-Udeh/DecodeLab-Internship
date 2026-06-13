score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    score += 1

answer = input("What is 5 + 5? ")
if answer == "10":
    score += 1

answer = input("What color is the sky on a clear day? ")
if answer.lower() == "blue":
    score += 1

print("Your final score is:", score, "/3")
