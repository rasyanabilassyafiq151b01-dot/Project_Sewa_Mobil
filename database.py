import sys
import Pembeli
import Tampilan


db_one = {
    'Avanza': {'seat': 4, 'price per day' : 300000},
    'Innova': {'seat': 6, 'price per day' : 400000},
    'Kijang': {'seat': 8, 'price per day' : 500000},
}
db_two = {
    'Avanza': {'seat': 4, 'price per day' : 320000},
    'Innova': {'seat': 6, 'price per day' : 420000},
    'Kijang': {'seat': 8, 'price per day' : 520000},
}
db_three = {
    'Avanza': {'seat': 4, 'price per day' : 350000},
    'Innova': {'seat': 6, 'price per day' : 450000},
    'Kijang': {'seat': 8, 'price per day' : 550000},
}
def get_database(choice):
    if choice == 1:
        return db_one
    elif choice == 2:
        return db_two
    elif choice == 3:
        return db_three
    else:
        return None
def display_cars(database):
    print("Available cars:")
    for car, details in database.items():
        print(f"{car}: {details['seat']} seats, Price per day: {details['price per day']}")
def main():
    while True:
        try:
            choice = int(input("Select database (1, 2, or 3): "))
            database = get_database(choice)
            if database is None:
                print("Invalid choice. Please select 1, 2, or 3.")
                continue
            display_cars(database)
            break
        except ValueError:
            print("Please enter a valid number.")