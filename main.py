import data_loader as dl
import analysis as an
import plots as pl

dl.init_cache()

year = int(input("Введи год сезона (например 2026): ").strip())
schedule = dl.get_schedule(year)

print("\nГонки сезона:")
print(schedule[['RoundNumber', 'EventName', 'Country']].to_string(index=False))

round_number = int(input("\nВведи номер этапа (RoundNumber): ").strip())
event = dl.get_event(schedule, round_number)
event_name = event['EventName'].iloc[0]

session_types = {'1': 'FP1', '2': 'FP2', '3': 'FP3', 'Q': 'Q', 'R': 'R'}
print("\nТипы сессий: 1=FP1, 2=FP2, 3=FP3, Q=Квалификация, R=Гонка")
session_choice = input("Выбери тип сессии: ").strip().upper()
if session_choice not in session_types:
    raise ValueError("Некорректный тип сессии")
session_type = session_types[session_choice]

session = dl.load_session(year, round_number, session_type)

available_drivers = sorted(session.laps['Driver'].unique())

print("\nРезультаты сессии:")
leaderboard = session.results[['Position', 'Abbreviation', 'FullName', 'TeamName']].copy()
leaderboard = leaderboard.sort_values('Position')
print(leaderboard.to_string(index=False))

driver1 = input("\nВведи код первого пилота (например VER): ").strip().upper()
driver2 = input("Введи код второго пилота (например ALO): ").strip().upper()
if driver1 not in available_drivers or driver2 not in available_drivers:
    raise ValueError("Один из пилотов не участвовал в этой сессии")

laps_d1 = an.get_driver_laps(session, driver1)
laps_d2 = an.get_driver_laps(session, driver2)

if len(laps_d1) < 3 or len(laps_d2) < 3:
    print(f"\n⚠️ Мало кругов ({driver1}: {len(laps_d1)}, {driver2}: {len(laps_d2)}) — вероятно, сход.")

pl.plot_lap_times(laps_d1, laps_d2, driver1, driver2, event_name, year, session_type)

print(f"\n{driver1} average sectors:")
print(an.add_sector_seconds(laps_d1)[['Sector1Seconds', 'Sector2Seconds', 'Sector3Seconds']].mean())
print(f"\n{driver2} average sectors:")
print(an.add_sector_seconds(laps_d2)[['Sector1Seconds', 'Sector2Seconds', 'Sector3Seconds']].mean())

if session_type == 'R':
    pl.plot_tyre_degradation(session, driver1, driver2, event_name, year)
elif session_type == 'Q':
    times1 = an.get_qualifying_times(session, driver1)
    times2 = an.get_qualifying_times(session, driver2)
    pl.plot_qualifying_segments(driver1, driver2, times1, times2, event_name, year)
else:
    print(f"\nДля сессии {session_type} график деградации/квалификации пропущен.")

for drv, laps in [(driver1, laps_d1), (driver2, laps_d2)]:
    accurate_laps = session.laps.pick_drivers(drv).copy()
    accurate_laps = accurate_laps[accurate_laps['IsAccurate'] == True].copy()
    accurate_laps = an.add_sector_seconds(accurate_laps)
    accurate_laps = an.classify_driver_sectors(accurate_laps)
    pl.plot_sector_table(drv, accurate_laps, f"{drv.lower()}_table.html")