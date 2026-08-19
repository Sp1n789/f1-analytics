import pandas as pd

TEAM_COLORS = {
    'Red Bull Racing': '#3671C6',
    'Ferrari': '#E8002D',
    'Mercedes': '#27F4D2',
    'McLaren': '#FF8000',
    'Aston Martin': '#006F62',
    'Alpine': '#00A1E8',
    'Williams': '#64C4FF',
    'RB': '#6692FF',
    'Kick Sauber': '#52E252',
    'Haas F1 Team': '#B6BABD',
}

SECTOR_COLOR_MAP = {'purple': '#9d4edd', 'green': '#2ecc71', 'yellow': '#f1c40f'}


def get_driver_laps(session, driver_code: str) -> pd.DataFrame:
    laps = session.laps.pick_drivers(driver_code).copy()
    laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
    return laps


def add_sector_seconds(laps: pd.DataFrame) -> pd.DataFrame:
    laps = laps.copy()
    for sector in ['Sector1Time', 'Sector2Time', 'Sector3Time']:
        col = sector.replace('Time', 'Seconds')
        laps[col] = laps[sector].dt.total_seconds()
    return laps


def classify_driver_sectors(laps: pd.DataFrame) -> pd.DataFrame:
    """Помечает лучший круг пилота в каждом секторе как 'green', остальные — 'yellow'."""
    laps = laps.copy()
    for sector in ['Sector1Seconds', 'Sector2Seconds', 'Sector3Seconds']:
        best = laps[sector].min()
        color_col = sector.replace('Seconds', 'Color')
        laps[color_col] = laps[sector].apply(lambda t: 'green' if t == best else 'yellow')
    return laps


def get_team_color(laps: pd.DataFrame) -> str:
    team = laps['Team'].iloc[0]
    return TEAM_COLORS.get(team, '#FFFFFF')


def get_qualifying_times(session, driver_code: str) -> dict:
    row = session.results[session.results['Abbreviation'] == driver_code].iloc[0]
    times = {}
    for q in ['Q1', 'Q2', 'Q3']:
        t = row[q]
        times[q] = t.total_seconds() if t is not None and str(t) != 'NaT' else None
    return times