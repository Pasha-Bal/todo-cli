import json
import os

FILE_PATH = "data/tasks.json"


def load_tasks():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:

        try:
            return json.load(file)

        except json.JSONDecodeError:
            return []


def save_tasks(tasks):

    with open(FILE_PATH, "w", encoding="utf-8") as file:

        json.dump(
            tasks,
            file,
            indent=4,
            ensure_ascii=False
        )