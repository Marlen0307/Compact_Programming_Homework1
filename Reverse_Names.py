first_name = input('Enter your first name:   ')
last_name = input('Enter your last name:   ')


def reverse_string(text):
    return text[::-1]


print(reverse_string(last_name), " ", reverse_string(first_name),)
