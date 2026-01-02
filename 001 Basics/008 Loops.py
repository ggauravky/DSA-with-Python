# Python loop examples

# for loop: iterate over items in an iterable
for name in ["Ada", "Grace", "Linus"]:
    print(name)

# while loop: repeat while condition stays true
count = 3
while count > 0:
    print("count:", count)
    count -= 1

# for...else: else runs only if loop does not break
for n in range(5):
    if n == 3:
        break
else:
    print("finished without break")

# while...else: else runs only if loop does not break
num = 0
while num < 3:
    num += 1
    if num == 2:
        break
else:
    print("loop ended naturally")

# nested loops: loop inside loop (e.g., grid traversal)
for row in range(2):
    for col in range(3):
        print(f"cell ({row}, {col})")

# infinite loop: intentional loop until internal break/return
steps = 0
while True:
    steps += 1
    if steps >= 3:
        print("breaking out")
        break
