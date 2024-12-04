list1 = []
list2 = []
distance = 0

try:
    with open('input', 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

except FileNotFoundError:
    print("Error: file not found")
except ValueError:
    print("Error: only int type allowed in file")

list1.sort()
list2.sort()

for num1, num2 in zip(list1, list2):
    distance += abs(num1 - num2)

print("Distance: ", distance)