def write_file(file_name, file_content):
    with open(file_name + ".txt", mode='w', encoding='utf-8') as new_file:
        new_file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + ".txt", mode='a', encoding='utf-8') as new_file:
        new_file.write(append_content)

def read_file(file_name):
    with open(file_name + ".txt", encoding='utf-8') as new_file:
        return new_file.read()
