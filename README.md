# Diplom_1 — Юнит-тесты для Stellar Burgers

## Описание
Юнит-тесты для программы, помогающей заказать бургер в Stellar Burgers.
Покрыты классы: `Bun`, `Burger`, `Ingredient`, `Database`.

Покрытие кода: **100%**.

## Структура
- `praktikum/` — исходный код программы
- `tests/` — тесты

## Установка и запуск
```bash
pip install -r requirements.txt
pytest --cov=praktikum --cov-report=html --cov-report=term-missing
```

Отчёт о покрытии: `htmlcov/index.html`

## Как приложить отчёт к пул-реквесту

`htmlcov/` не хранится в репозитории (см. `.gitignore`), поэтому отчёт нужно
добавить именно в сам пул-реквест, а не в код:
1. Прогони `pytest --cov=praktikum --cov-report=term-missing` и сделай
   скриншот терминала с итоговой строкой покрытия (`TOTAL ... 100%`).
2. Вставь скриншот (или текст вывода) в описание пул-реквеста на GitHub —
   можно просто перетащить картинку в поле описания.
