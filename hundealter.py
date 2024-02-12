def hundealter(alter):
    if alter == 1:
        return "Your dog is 14 years old in human age"
    elif alter == 2:
        return "Your dog is 22 years old in human age"

    elif alter > 2:
        age = 22
        for i in range(3, alter + 1):
            age += 5
        return f"Your dog is {age} years old"



result = hundealter(3)
print(result)