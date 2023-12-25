from file_worker import FileWorker


def main(
        path_generate_file: str,
        path_calculate_divident_result: str,
) -> None:
    """Главная функция для работы."""

    # Инициализация необходимых классов
    file_worker = FileWorker(
        path_generate_file,
        path_calculate_divident_result,
    )

    # Запуск необходимых функций
    file_worker.generate_data()
    file_worker.calculate_divident()


if __name__ == "__main__":
    """Запуск приложения"""

    main(
        path_generate_file="data_files/file_generate.txt",
        path_calculate_divident_result="data_files/file_result.txt",
    )
