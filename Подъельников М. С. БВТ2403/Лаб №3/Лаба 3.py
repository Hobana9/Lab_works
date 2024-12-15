#1 задание
def read_file(mode, filename):
    with open(filename, 'r') as f:
        if mode == 'all':
            content = f.read()
        if mode == 'line':
            content = ''
            for line in f:
                content += line
    print(content)
read_file('line', 'example.txt')
#2 задание
def write_to_file():
    text = input("Введите текст: ")
    with open('user_input.txt', 'w') as f:
        f.write(text)
def append_to_file():
    text = input("Введите текст: ")
    with open('user_input.txt', 'a') as f:
        f.write("\n" + text)
write_to_file()
append_to_file()
#3 задание
def read_file_new(mode, filename):
    try:
        with open(filename, 'r') as f:
            if mode == 'all':
                content = f.read()
            if mode == 'line':
                content = ''
                for line in f:
                    content += line
        print(content)
    except FileNotFoundError as e:
        print(f"Ошибка: файл {filename} не найден")
read_file_new('line', 'abcd.txt')
