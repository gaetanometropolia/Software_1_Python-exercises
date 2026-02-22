import random
import mariadb

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Gaetrig1992.",
    database="flight_game",
    autocommit=True
)

MONTHS = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

# Each tournament:
# ("Tournament Name", points_if_win, money_if_win, airport_ident)
#
# airport_ident = ICAO code found in your airport table (airport.ident)
TOURNAMENTS = [
    ("Australian Open (Melbourne)", 700, 10000, "YMML"),  # Melbourne
    ("Dubai Open", 300, 5000, "OMDB"),                    # Dubai
    ("Indian Wells", 500, 7000, "KPSP"),                  # Palm Springs (near Indian Wells)
    ("Monte Carlo", 500, 7000, "LFMN"),                   # Nice (near Monaco)
    ("Rome Open", 500, 7000, "LIRF"),                     # Rome Fiumicino
    ("Roland Garros (Paris)", 700, 10000, "LFPG"),        # Paris CDG
    ("Wimbledon (London)", 700, 10000, "EGLL"),           # London Heathrow
    ("Cincinnati", 500, 7000, "KCVG"),                    # Cincinnati/Northern Kentucky
    ("US Open (New York)", 700, 10000, "KJFK"),           # New York JFK
    ("Shanghai", 500, 7000, "ZSPD"),                      # Shanghai Pudong
    ("Paris Masters", 500, 7000, "LFPG"),                 # Paris CDG
    ("Season Final (London)", 600, 8000, "EGLL"),         # simplified
]

START_MONEY = 3000
FLIGHT_COST = 100
ENTRY_FEE = 50

START_SKILL = 20
WIN_THRESHOLD = 70

def get_airport_by_ident(ident: str):
    cur = connection.cursor()
    cur.execute("""
        SELECT ident, name, iso_country
        FROM airport
        WHERE ident = %s
        LIMIT 1
    """, (ident,))
    row = cur.fetchone()
    cur.close()
    return row  # (ident, name, iso_country) or None

def get_fallback_airport():
    cur = connection.cursor()
    cur.execute("""
        SELECT ident, name, iso_country
        FROM airport
        WHERE latitude_deg IS NOT NULL
        ORDER BY RAND()
        LIMIT 1
    """)
    row = cur.fetchone()
    cur.close()
    return row

def compute_ranking(points: int) -> int:
    # Winnable ranking
    rank = 250 - (points // 25)
    return max(1, rank)

def show_status(player, month):
    print("\n========================================")
    print(f"Month: {month}")
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Money: ${player['money']}")
    print(f"Points: {player['points']}")
    print(f"Ranking: #{player['ranking']}")
    print(f"Skill: {player['skill']}")
    print("========================================")

def play_tournament(player, tournament):
    t_name, win_points, win_money, airport_ident = tournament
    total_cost = FLIGHT_COST + ENTRY_FEE

    airport = get_airport_by_ident(airport_ident)
    if airport is None:
        # If ICAO is not found in DB, use fallback (still keeps the game running)
        airport = get_fallback_airport()
        airport_ident = airport[0]
        print(f"⚠️ Warning: tournament airport not found in DB, using fallback airport {airport_ident}")

    print("\n--- TOURNAMENT ---")
    print(f"Tournament: {t_name}")
    print(f"Destination: {airport[1]} ({airport[2]}) [{airport[0]}]")
    print(f"Costs: flight ${FLIGHT_COST} + entry ${ENTRY_FEE} = ${total_cost}")

    if player["money"] < total_cost:
        print("❌ Not enough money to travel + enter. You must skip this month.")
        return

    player["money"] -= total_cost
    player["location"] = f"{airport[0]} - {airport[1]} ({airport[2]})"

    roll = random.randint(1, 100) + player["skill"]
    print(f"Roll: (1..100) + skill({player['skill']}) = {roll} (need >= {WIN_THRESHOLD})")

    if roll >= WIN_THRESHOLD:
        print("🏆 RESULT: WIN!")
        player["points"] += win_points
        player["money"] += win_money
        print(f"Rewards: +{win_points} points, +${win_money}")
    else:
        print("❌ RESULT: LOSE!")
        print("Rewards: +0 points, +$0")

    player["ranking"] = compute_ranking(player["points"])
    print(f"Updated ranking: #{player['ranking']}")

def maybe_upgrade(player):
    upgrade_cost = 1000
    upgrade_gain = 10
    if player["money"] < upgrade_cost:
        return
    choice = input(f"\nUpgrade skill for ${upgrade_cost}? (+{upgrade_gain} skill) (y/n): ").strip().lower()
    if choice == "y":
        player["money"] -= upgrade_cost
        player["skill"] += upgrade_gain
        print("✅ Skill upgraded!")

def main():
    print("=== Tennis Pro 2026 ===")
    name = input("Enter player name: ").strip() or "Player1"

    player = {
        "name": name,
        "money": START_MONEY,
        "points": 0,
        "ranking": 250,
        "skill": START_SKILL,
        "location": "HOME"
    }

    for i in range(12):
        month = MONTHS[i]
        tournament = TOURNAMENTS[i]

        show_status(player, month)

        choice = input(f"Do you want to play {tournament[0]}? (y/n): ").strip().lower()
        if choice == "y":
            play_tournament(player, tournament)
            maybe_upgrade(player)
        else:
            print("You skipped this month.")

        if player["ranking"] == 1:
            print("\n🏆 You reached World No.1! You win!")
            break

    print("\n=== SEASON FINISHED ===")
    print(f"Final Points: {player['points']}")
    print(f"Final Money: ${player['money']}")
    print(f"Final Ranking: #{player['ranking']}")

    connection.close()

if __name__ == "__main__":
    main()