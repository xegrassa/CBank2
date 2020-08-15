import os


def main():
    print('Начало тестов behave')
    os.chdir('..')
    json_path = os.path.join(os.getcwd(), 'report', 'behave.json')
    command = f'behave -n 1 -o {json_path} -f json.pretty --no-summary --no-capture'
    os.system(command)
    print('Конец тестов')


if __name__ == '__main__':
    main()
