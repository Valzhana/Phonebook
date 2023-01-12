
def write_in_txt_line(data):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        for i in data:
            file.write(i + '\n')


def write_in_txt_column(data):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        for i in data:
            file.write('; '.join(str(s) for s in i) + '\n')


def write_in_csv(data):
    with open('phone_book.csv', 'a', encoding='utf-8') as file:
        for i in data:
            file.write(';'.join(str(s) for s in i) + '\n')


def print_from_txt():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for i in file:
            print(i, end='')
