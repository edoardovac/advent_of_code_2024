list1 = []
list2 = []
similarity = 0

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

for num in list1:
    repeat = list2.count(num)
    similarity += num * repeat

print("Similarity: ", similarity)