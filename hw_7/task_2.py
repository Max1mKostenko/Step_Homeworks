text = input("Please enter any text: ")
words = input("Please enter some words from text space-separated: ")
total = 0
for i in words.split(" "):
    total += text.count(i)
print(total)
