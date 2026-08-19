import time
import webbrowser
import plotly.graph_objects as go
import plotly.express as px

from analysis import SECTOR_COLOR_MAP, get_team_color

OUTPUT_DIR = r"c:\Users\Admin\Desktop\f1"


def save_and_open(fig, filename: str):
    path = rf"{OUTPUT_DIR}\{filename}"
    fig.write_html(path)
    webbrowser.open(f"file:///{path.replace(chr(92), '/')}?t={int(time.time())}")


def plot_lap_times(laps_d1, laps_d2, driver1, driver2, event_name, year, session_type):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=laps_d1['LapNumber'], y=laps_d1['LapTimeSeconds'],
                              mode='lines+markers', name=driver1))
    fig.add_trace(go.Scatter(x=laps_d2['LapNumber'], y=laps_d2['LapTimeSeconds'],
                              mode='lines+markers', name=driver2))
    fig.update_layout(
        title=f'{driver1} vs {driver2} — Lap Times, {event_name} {year} ({session_type})',
        xaxis_title='Lap Number',
        yaxis_title='Lap Time (s)'
    )
    save_and_open(fig, "lap_times.html")


def plot_tyre_degradation(session, driver1, driver2, event_name, year):
    all_laps = session.laps.pick_drivers([driver1, driver2]).copy()
    all_laps['LapTimeSeconds'] = all_laps['LapTime'].dt.total_seconds()
    all_laps = all_laps[all_laps['IsAccurate'] == True]

    fig = px.scatter(
        all_laps, x='TyreLife', y='LapTimeSeconds', color='Compound',
        facet_col='Driver', trendline='ols',
        title=f'Tyre Degradation: Lap Time vs Tyre Age — {event_name} {year}'
    )
    save_and_open(fig, "tyre_degradation.html")


def plot_qualifying_segments(driver1, driver2, times1: dict, times2: dict, event_name, year):
    q_sessions = ['Q1', 'Q2', 'Q3']
    fig = go.Figure()
    for drv_code, times in [(driver1, times1), (driver2, times2)]:
        fig.add_trace(go.Bar(x=q_sessions, y=[times[q] for q in q_sessions], name=drv_code))
    fig.update_layout(
        title=f'{driver1} vs {driver2} — Qualifying Segments, {event_name} {year}',
        yaxis_title='Lap Time (s)',
        barmode='group'
    )
    save_and_open(fig, "qualifying_segments.html")


def plot_sector_table(driver_code, laps, filename):
    driver_color = get_team_color(laps)

    def colors_for(col):
        return [SECTOR_COLOR_MAP[c] for c in laps[col]]

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Driver', 'Lap', 'Sector 1', 'Sector 2', 'Sector 3'],
            fill_color='#333', font=dict(color='white'), align='center'
        ),
        cells=dict(
            values=[
                laps['Driver'], laps['LapNumber'],
                laps['Sector1Seconds'].round(3),
                laps['Sector2Seconds'].round(3),
                laps['Sector3Seconds'].round(3),
            ],
            fill_color=[
                ['#222'] * len(laps), ['#222'] * len(laps),
                colors_for('Sector1Color'), colors_for('Sector2Color'), colors_for('Sector3Color'),
            ],
            font=dict(color=[driver_color, 'white', 'black', 'black', 'black']),
            align='center'
        )
    )])
    fig.update_layout(title=f'{driver_code} — Sector Times')
    save_and_open(fig, filename)