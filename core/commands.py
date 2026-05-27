
from core.storage import (
    load_tasks,
    save_tasks
)
from core.utils import validate_text

def add_task(text):
    validate_text(text)

    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "text": text,
        "done": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Задача добавлена")


def list_tasks():

    tasks = load_tasks()

    if not tasks:
        print("Список задач пуст")
        return

    for task in tasks:

        status = "✓" if task["done"] else " "

        print(
            f'{task["id"]}. [{status}] {task["text"]}'
        )


def complete_task(task_id):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            task["done"] = True

            save_tasks(tasks)

            print("Задача выполнена")

            return

    print("Задача не найдена")


def delete_task(task_id):

    tasks = load_tasks()

    new_tasks = []

    for task in tasks:

        if task["id"] != task_id:
            new_tasks.append(task)

    save_tasks(new_tasks)

    print("Задача удалена")