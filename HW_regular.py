import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for index, person in enumerate(contacts_list[1:]):
    result = ' '.join(person[:3]).split()
    if len(result) == 2:
        result.append('')
    contacts_list[index + 1][:3] = result[:3]
sorted_list = sorted(contacts_list, key=lambda x: x[0:2])


def union_list(sort_list):
    count = 0
    while count < len(sort_list) - 1:
        for list1, list2 in zip(sort_list[count], sort_list[count + 1]):
            if list1 == list2:
                new_list = []
                for i in range(len(sort_list[count])):
                    if sort_list[count][i] == sort_list[count + 1][i]:
                        new_list.append(sort_list[count][i])

                    elif sort_list[count][i] == '':
                        new_list.append(sort_list[count + 1][i])

                    else:
                        new_list.append(sort_list[count][i])

                sort_list.remove(sort_list[count + 1])
                sort_list.remove(sort_list[count])
                sort_list.append(new_list)
            break
        count += 1
    return sort_list


def formatting_phone_numbers(text):
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?"
    substitution = r'+7(\2)\3-\4-\5\6\7\8'
    edited_text = re.sub(pattern, substitution, text)
    return edited_text


def convert_to_string(text):
    result_str = ''
    for row in text:
        result_str += ', '.join(row)
        result_str += '\n'
    return result_str


def convert_for_csv(text):
    result_text = []
    for line in text.split('\n'):
        result_text.append(line.split(', '))
    result_text.remove([''])
    return result_text


if __name__ == '__main__':
    union = union_list(sorted_list)
    convert_str = convert_to_string(union)
    formatting_phone = formatting_phone_numbers(convert_str)
    result_list = convert_for_csv(formatting_phone)

    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(result_list)
