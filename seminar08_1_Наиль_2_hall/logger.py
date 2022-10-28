def write_employees(a):
    with open('seminar_8_employees.txt', 'a', encoding='utf-8') as f:
        f.write(f'{a}\n')
        
def read_employees():
    mass = []
    with open('seminar_8_employees.txt', 'r', encoding='utf-8') as f:
        for i in f:
            mass.append(i)
        return mass  

def rename_data(mass):
    with open('seminar_8_employees.txt', 'w', encoding='utf-8') as f:
        for i in mass:
            f.write(i)

def write_re(a):
    with open('seminar_8_employees.txt', 'w', encoding='utf-8') as f:
        for i in a:
            f.write(i+'\n')




