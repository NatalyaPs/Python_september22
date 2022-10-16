from encodings import utf_8


def write_contact(b):
    with open('directory.txt', 'a', encoding='utf-8') as f:
        f.write(b)  # return f.write(b)

def read_contact():
    with open('directory.txt', 'r', encoding='utf-8') as f:
        return f.read()        