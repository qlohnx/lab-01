def iter_documents(root):
    # нумерація документів із 1
    doc_id = 1

    # Знайти всі файли з кінцівкою .txt у папці та її підпапках
    for file_path in root.rglob("*.txt"):
        try:
            # Прочитати текст із цього файлу
            text = file_path.read_text(encoding="utf-8", errors="replace")

            # Віддати цей документ назовні і зупинитися на паузу (yield)
            yield (doc_id, str(file_path), text)

            # Збільшити номер для наступного документа
            doc_id += 1
        except Exception as e:  # noqa: BLE001
            print(f"Помилка при читанні файлу {file_path}: {e}")
            # OSError, ValueError можливо
