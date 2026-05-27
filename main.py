from core.commands import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
)

import sys


def main():

    if len(sys.argv) < 2:

        print("Команды:")
        print("add")
        print("list")
        print("done")
        print("delete")

        return

    command = sys.argv[1]

    try:

        if command == "add":

            text = sys.argv[2]
            add_task(text)

        elif command == "list":

            list_tasks()

        elif command == "done":

            task_id = int(sys.argv[2])
            complete_task(task_id)

        elif command == "delete":

            task_id = int(sys.argv[2])
            delete_task(task_id)

        else:
            print("Неизвестная команда")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()