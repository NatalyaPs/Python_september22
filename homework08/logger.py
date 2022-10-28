from encodings import utf_8

def write_data(b):
    with open('directory.txt', 'a', encoding='utf-8') as f:
        f.write(b) 

def read_data():
    with open('directory.txt', 'r', encoding='utf-8') as f:
        return f.read()    

def edit_data(d):
    with open('directory.txt', 'w+', encoding='utf-8') as f:
        #for i in d:
        f.write(d)
