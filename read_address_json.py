f = open("./data/book.txt", "r")
txt = f.read()
print("txt has type: ", type(txt))

print("================================================")
print("read as dictionary")

import json 
book = json.loads(txt)
print(f"book has type;{type(book)}")
print(f"book for tom is", book['tom'])

for person in book:
    print(f"book by person {book[person]}")