import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="view")
def view_entries():
    try:
        with open(DATA_PATH, "r") as f:
            temp = json.load(f)
            for category, entries in temp.items():
                print(f"\nCategory: {category}")
                for entry in entries:
                    name = entry["name"]
                    location = entry["location"]
                    food_ordered = entry["food_ordered"]
                    likes = entry["likes"]
                    dislikes = entry["dislikes"]
                    rating = entry["rating"]
                    visit_again = entry["visit_again"]
                    print(f"Name of experience: {name}")
                    print(f"Location of experience: {location}")
                    print(f"Food/Drink ordered: {food_ordered}")
                    print(f"Likes of experience: {likes}")
                    print(f"Dislikes of experience: {dislikes}")
                    print(f"Rating of experience: {rating}")
                    print(f"Visit again?: {visit_again}")
                    print("\n")
    
    except FileNotFoundError:
        click.echo("No entries found.")