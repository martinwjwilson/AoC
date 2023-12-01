# read file
f = open("input.txt")
content = f.read()

buffer = []
counter = 0
for letter in content:
    buffer.append(letter)
    if len(buffer) > 14:
        buffer.pop(0)
    counter += 1
    if len(buffer) == 14:  # only check when buffer is full
        if len(buffer) == len(set(buffer)):
            break

print(counter)
