from encodings import utf_8


def log_expr(a):
    with open('sem7_file.txt', 'w', encoding=utf_8) as f:
        f.write(f'Уравнение: {a} = 0 \n')  # f.write(a)

def log_ans(a):
    with open('sem7_file.txt', 'a', encoding=utf_8) as f:
        f.write(f'Корни уравнения: {a} = 0 \n')