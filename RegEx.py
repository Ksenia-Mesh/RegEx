import re
import csv



def open_file(file_name):
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return(contacts_list)

def change_number(contacts_list):
    phone_number = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    result_phone_number = r'+7(\2)\3-\4-\5 \6\7'
    new_list = list()
    for item in contacts_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(phone_number, result_phone_number, item[5]),
                  item[6]]
        new_list.append(result)
    return join_duplicates(new_list)

def format_name(contacts_list):
    employee_name = r'^([А-ЯЁа-яё])(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,|\s?)([А-ЯЁа-яё]*)'
    employee_name_new = r'\1\4 \7 \9'
    contacts_list_updated = list()
    for date in contacts_list:
        date_as_string = ','.join(date)
        formatted_date = re.sub(employee_name, employee_name_new, date_as_string)
        date_as_list = formatted_date.split(',')
        contacts_list_updated.append(date_as_list)
    return contacts_list_updated


def join_duplicates(contacts_list):
    for con in contacts_list:
        for j in contacts_list:
            if con[0] == j[0] and con[1] == j[1] and con is not j:
                if con[2] == '':
                    con[2] = j[2]
                if con[3] == '':
                    con[3] = j[3]
                if con[4] == '':
                    con[4] = j[4]
                if con[5] == '':
                    con[5] = j[5]
                if con[6] == '':
                    con[6] = j[6]
    contacts_list_updated = list()
    for card in contacts_list:
        if card not in contacts_list_updated:
            contacts_list_updated.append(card)
    return contacts_list_updated

def write_file(contacts_list):
    with open("phone_book_formatted.csv", "w", encoding="utf-8") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(contacts_list)

if __name__ == '__main__':
    contacts = open_file('phonebook_raw.csv')
    contacts = change_number(contacts)
    contacts = format_name(contacts)
    contacts = join_duplicates(contacts)
    contacts[0][2] = 'patronymic'
    write_file(contacts)
    print(contacts)