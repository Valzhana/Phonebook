import json

with open('phone_book.txt', 'r') as ph:
    book = ph.readlines()
with open("data_file.json", "w") as write_file:
    json.dump(book, write_file, indent=4)
