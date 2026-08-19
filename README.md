# F1 Analytics
🇬🇧 [English](#english) | 🇷🇺 [Русский](#русский)

---

## English


A tool for analyzing Formula 1 driver performance, built on [FastF1](https://github.com/theOehrly/Fast-F1) data. Pick any season from 2018 onward, any round, and any session type (practice, qualifying, race), then compare two drivers by pace, sector times, and — for races — tyre degradation.

## Features

- Select season, round, and session type (FP1–FP3, Q, R)
- Session leaderboard shown before picking drivers
- Lap-by-lap pace comparison (line chart)
- Average sector times
- Tyre degradation by compound with trend lines (races)
- Qualifying segment comparison — Q1/Q2/Q3 (qualifying sessions)
- Sector time table with color coding (personal best — green, other laps — yellow) and driver names colored by team

## Stack

- Python
- [FastF1](https://github.com/theOehrly/Fast-F1) — data from the official F1 timing API
- Pandas — data processing
- Plotly — interactive charts

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The script will ask for the year, round, session type, and driver codes — everything else is built and opened in your browser automatically.

## Project structure

main.py — entry point (user input, call order)
data_loader.py — season/session loading via FastF1
analysis.py — calculations (sectors, degradation, team colors)
plots.py — chart and table rendering (Plotly)


## Examples

**Lap time comparison**
![Lap times comparison](https://github.com/user-attachments/assets/cc599f29-6d1d-4309-bd44-40b9f0837ee3)

**Tyre degradation**
![Tyre degradation](https://github.com/user-attachments/assets/2ea0c31b-1ce8-4df6-a94a-1b55bfd1d78f)

**Sector table — driver 1**
![Sector table driver 1](https://github.com/user-attachments/assets/f974f262-1406-4e7e-812d-0ad59e3f8767)


**Sector table — driver 2**
![Sector table driver 2](https://github.com/user-attachments/assets/d5281490-0f90-4fab-8501-1d8fa5dc3956)
---

## Русский


Инструмент для анализа темпа пилотов Формулы 1 на основе данных [FastF1](https://github.com/theOehrly/Fast-F1). Позволяет выбрать любой сезон с 2018 года, любую гонку и любую сессию (практика, квалификация, гонка), а затем сравнить двух пилотов по темпу, секторам и — для гонки — деградации шин.

## Возможности

- Выбор сезона, этапа и типа сессии (FP1–FP3, Q, R)
- Лидерборд сессии перед выбором пилотов
- Сравнение темпа по кругам (line chart)
- Средние времена по секторам
- Для гонки — деградация шин по компаундам с линией тренда
- Для квалификации — сравнение лучших времён по Q1/Q2/Q3
- Таблица секторов с раскраской (жёлтый / личный лучший — зелёный) и цветом команды в имени пилота

## Стек

- Python
- [FastF1](https://github.com/theOehrly/Fast-F1) — данные с официального F1 timing API
- Pandas — обработка данных
- Plotly — интерактивные графики

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

Скрипт спросит год, этап, тип сессии и коды пилотов — всё остальное построит и откроет в браузере автоматически.

## Структура проекта
main.py — сценарий (ввод пользователя, порядок вызовов)
data_loader.py — загрузка сезона/сессии через FastF1
analysis.py — расчёты (секторы, деградация, цвета команд)
plots.py — построение графиков и таблиц (Plotly)
## Примеры
**Сравнение темпа по кругам**
![Lap times comparison](https://github.com/user-attachments/assets/cc599f29-6d1d-4309-bd44-40b9f0837ee3)

**Деградация шин**
![Tyre degradation](https://github.com/user-attachments/assets/2ea0c31b-1ce8-4df6-a94a-1b55bfd1d78f)

**Таблица секторов — пилот 1**
![Sector table driver 1](https://github.com/user-attachments/assets/f974f262-1406-4e7e-812d-0ad59e3f8767)

**Таблица секторов — пилот 2**
![Sector table driver 2](https://github.com/user-attachments/assets/d5281490-0f90-4fab-8501-1d8fa5dc3956)


