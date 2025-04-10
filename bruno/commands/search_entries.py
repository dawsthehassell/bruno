import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="search")
@click.option("--category", default=None, help="Filter by category (ex: restaurant, coffee shop, etc.)")
@click.option("--term", required=True, help="Search term to look for in entry log")
def search_entries(term, category):
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    term = term.strip().lower()
    if category:
        category = category.strip().lower()
    results = []

    if category:
        if category in data:
            for entry in data[category]:
                for value in entry.values():
                    if term in str(value).lower():
                        results.append(entry)
    else:
        for category_name, entries_list in data.items():
            for entry in entries_list:
                for value in entry.values():
                    if term in str(value).lower():
                        results.append(entry)
    
    if results:
        for i, entry in enumerate(results, 1):
            print(f"\n{i}.")
            for key, value in entry.items():
                print(f"   {key.capitalize()}: {value}")
    else:
        print("No results found!")