import os

from investing_parse import REPORT_DIR_PATH, BASE_DIR, CHROMEDRIVER_PATH, GECKODRIVER_PATH


def check_access(path):
    if not os.access(path, os.F_OK):
        raise FileExistsError(f'Файла {path} несуществует')
    if not os.access(path, os.X_OK):
        raise PermissionError(f'У файла {path} нет прав на исполнение')


def main():
    check_access(CHROMEDRIVER_PATH)
    check_access(GECKODRIVER_PATH)
    print('Начало тестов behave')
    json_path = os.path.join(REPORT_DIR_PATH, 'behave.json')
    start_dir = os.path.join(BASE_DIR, 'features')
    command = f'behave {start_dir} --outfile {json_path} --format json.pretty --no-summary --no-capture'
    os.system(command)
    print('Конец тестов')


if __name__ == '__main__':
    main()
