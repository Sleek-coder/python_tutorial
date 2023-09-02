book = {}
book['tom'] = {
    'name': 'tom',
    'addresss': '1 red street, NY',
    'phone': 98989898
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 23424234
}

import json
s = json.dumps(book)
with open("./data/book.txt", "w") as f:
    f.write(s)
    