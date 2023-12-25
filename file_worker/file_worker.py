import random

from config import COUNT_GENERATE, NAME_GENERATE, SURNAME_GENERATE, PRICE_BONDS, PERCENT_DIVIDENT


class FileWorker:
    """Класс для работы с текстовым файлом"""
    def __init__(self, path_generate_file: str | None = None, path_calculate_divident_result: str | None = None):

        if path_generate_file is None:
            print(f"Предупреждение. Путь path_generate_file = {path_generate_file}")
        else:
            self.path_generate_file = path_generate_file

        if path_calculate_divident_result is None:
            print(f"Предупреждение. Путь path_calculate_divident_result = {path_calculate_divident_result}")
        else:
            self.path_calculate_divident_result = path_calculate_divident_result

    def generate_data(self):
        """Функция для генерации data в текстовый файл."""

        with open(self.path_generate_file, "w", encoding="utf-8") as file:
            for _ in range(COUNT_GENERATE):
                random_name = random.choice(NAME_GENERATE)
                random_surname = random.choice(SURNAME_GENERATE)
                count_bond = str(random.randint(1, 100))
                file.writelines(f"{random_name.rjust(10)} | {random_surname.rjust(10)} | {count_bond.rjust(10)}\n")

    def calculate_divident(self):
        """Функция для рассчеты дивидентов и запись их в текстовый файл."""

        with open(self.path_generate_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            replace_lines = []
            for count in range(COUNT_GENERATE):
                replace_lines.append(lines[count].strip().replace(" ", ""))

        with open(self.path_calculate_divident_result, "w", encoding="utf-8") as file:
            for count in range(COUNT_GENERATE):
                result_divident = int(replace_lines[count].split("|")[-1]) * PRICE_BONDS * PERCENT_DIVIDENT
                file.writelines(f"{replace_lines[count]}|{str(result_divident)}\n")
