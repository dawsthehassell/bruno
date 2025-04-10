import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="new")
def new():
    click.echo("Starting a new entry log...")
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    category = input("New Experience Catetory (ex: restaurant, coffee shop, etc.): ")

    new_entry = {
        "name": input("Name of New Experience: "),
        "location" : input("Location: "),
        "food_ordered": input("Food/Drink Ordered: "),
        "likes": input("Likes about New Experience: "),
        "dislikes": input("Dislikes of New Experience: "),
        "rating": input("Rating out of 5: "),
        "visit_again": input("Would you visit again? (yes/no): ").strip().lower() == "yes"
    }

    if category not in data:
        data[category] = []

    data[category].append(new_entry)

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
    
    click.echo("Entry added successfully!")
