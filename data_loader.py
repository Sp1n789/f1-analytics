import os
from datetime import datetime
import fastf1

fastf1.set_log_level('WARNING')

CACHE_DIR = 'cache_folder'


def init_cache():
    os.makedirs(CACHE_DIR, exist_ok=True)
    fastf1.Cache.enable_cache(CACHE_DIR)


def get_schedule(year: int):
    if year < 2018:
        raise ValueError(
            "FastF1 не поддерживает подробные данные по кругам для сезонов до 2018 года"
        )
    return fastf1.get_event_schedule(year)


def get_event(schedule, round_number: int):
    event = schedule[schedule['RoundNumber'] == round_number]
    if event.empty:
        raise ValueError(f"Этап с номером {round_number} не найден в календаре")

    event_date = event['EventDate'].iloc[0]
    if event_date > datetime.now():
        raise ValueError(
            f"Гонка '{event['EventName'].iloc[0]}' ещё не состоялась "
            f"(дата: {event_date.date()})"
        )
    return event


def load_session(year: int, round_number: int, session_type: str):
    session = fastf1.get_session(year, round_number, session_type)
    session.load()
    return session