
# def find_similar(data_to_find):
#     with open('phone_book.txt', 'r', encoding='utf-8') as file:
#         data = file.readlines()
#         for i in data:
#             if i == data_to_find:
#                 return True


def search_by(data):
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        data_to_find = []
        for line in book:
            for text in line.split(';'):
                if data.lower() in text.lower():
                    rec = line.split(';')
                    rec[0] = f'{rec[0]}'
                    rec[1] = f'{rec[1]}'
                    data_to_find.append(rec)
        print(''.join(*data_to_find))


def find_similar(data):
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        for line in book:
            for text in line.split(';'):
                if data.lower() in text.lower():
                    return True
