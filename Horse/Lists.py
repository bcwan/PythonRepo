lucky_numbers = [1, 2, 3]
other_lucky_numbers = [4, 5, 6]

# mutates lucky_numbers
lucky_numbers.extend(other_lucky_numbers)

# adding new items / like .push in JS
lucky_numbers.append(7)

lucky_numbers.insert(0, 0)

print(lucky_numbers)
# [0, 1, 2, 3, 4, 5, 6, 7]

lucky_numbers.remove(0)

print(lucky_numbers)
