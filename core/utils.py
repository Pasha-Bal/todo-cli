def validate_text(text):

    if not text.strip():

        raise ValueError(
            "Пустой текст задачи"
        )