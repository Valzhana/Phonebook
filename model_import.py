import model_search as s


def get_number():
    print("Enter '0' to exit")
    phones = []
    while True:
        last_name = input('Last name = ')
        if last_name == '0':
            break
        first_name = input('First name = ')
        phone = input('Phone = ')
        note = input('Note = ')
        input_data = last_name, first_name, phone, note
        phones_data = ';'.join(input_data)
        if s.find_similar(f'{phones_data}'):
            print('This contact already exists')
            continue
        else:
            phones.append((last_name, first_name, phone, note))
    return phones


def get_number_line():
    print('Example: Fursov; Dmitriy; 89173457806; mobile')
    phones = []
    while True:
        phones_data = input('')
        if phones_data == '0':
            break
        if s.find_similar(f'{phones_data}'):
            print('This contact already exists')
            continue
        else:
            str(phones.append(phones_data)).join(";")
    return phones
