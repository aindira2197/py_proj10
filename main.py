numbers = [45, 12, 78, 34, 89, 23, 11, 90]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Saralangan ro'yxat:")

for number in numbers:
    print(number)

smallest = numbers[0]
largest = numbers[-1]

print("Eng kichik:", smallest)
print("Eng katta:", largest)

middle = len(numbers) // 2
print("O'rta element:", numbers[middle])
