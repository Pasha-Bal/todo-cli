# Todo CLI

CLI-приложение для управления задачами.

## Установка

```bash
git clone https://github.com/USERNAME/todo-cli.git
cd todo-cli
pip install -r requirements.txt
```

## Команды

### Добавить задачу

```bash
python main.py add "Текст задачи"
```

### Показать список задач

```bash
python main.py list
```

### Отметить задачу выполненной

```bash
python main.py done 1
```

### Удалить задачу

```bash
python main.py delete 1
```

## Используемые технологии

- Python
- Git
- GitHub
- JSON

## Структура проекта

```text
todo-cli/
│
├── main.py
├── README.md
├── requirements.txt
│
├── core/
│   ├── commands.py
│   ├── storage.py
│   ├── utils.py
│   └── errors.py
│
├── data/
│   └── tasks.json
│
└── tests/
```
