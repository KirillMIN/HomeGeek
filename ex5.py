rating = [7, 5, 3, 3, 2]
print(f"Рейтинг - {rating}")
number = int(input("input number"))
rating.insert(0, number)
print(f"Рейтинг - {rating}")
swapped = True
while swapped:
    swapped = False
    for i in range(len(rating) - 1):
        if rating[i] < rating[i + 1]:
            rating[i], rating[i + 1] = rating[i + 1], rating[i]
            swapped = True
for index in range(len(rating) - 1):
    if rating[index] == rating[index + 1]:
        rating[index], rating[index + 1] = rating[index + 1], rating[index]
print(f"Рейтинг - {rating}")
