import os

from investing_parse import REPORT_DIR_PATH, BASE_DIR


def main():
    print('Начало тестов behave')
    json_path = os.path.join(REPORT_DIR_PATH, 'behave.json')
    start_dir = os.path.join(BASE_DIR, 'features')
    command = f'behave {start_dir} --outfile {json_path} --format json.pretty --no-summary --no-capture'
    os.system(command)
    print('Конец тестов')


if __name__ == '__main__':
    main()
