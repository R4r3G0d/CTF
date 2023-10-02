import hashlib

# Функция для вычисления MD5 хеша строки
def calculate_md5_hash(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Ожидаемый MD5 хеш
expected_hash = 'c8b852d2c9c1e3f0d68b579905b0f6be'

# Проход по файлам i.txt, где i меняется от 0 до 9999
for i in range(10000):
    file_path = f'{i}.txt'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Удалите символ новой строки и хешируйте строку
                line = line.strip()
                md5_hash = calculate_md5_hash(line)
                
                # Проверьте соответствие хеша ожидаемому значению
                if md5_hash == expected_hash:
                    print(f'Ожидаемый хеш найден в файле {file_path}: {expected_hash}')
                    print(f'Содержимое файла {file_path}:')
                    print(line)
                    exit()  # Завершить программу после нахождения ожидаемого хеша
    except FileNotFoundError:
        continue  # Если файл не найден, перейти к следующему файлу
    except Exception as e:
        print(f'Произошла ошибка при обработке файла {file_path}: {str(e)}')

# Если программа дошла до этой точки, ожидаемый хеш не был найден
print(f'Ожидаемый хеш не найден в файлах.')
