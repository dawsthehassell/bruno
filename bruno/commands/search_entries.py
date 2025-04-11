import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="search")
@click.option("--category", default=None, help="Filter by category (ex: restaurant, coffee shop, etc.)")
@click.option("--term", default=None, help="Search term to look for in entry log")
@click.option("--visit_again", is_flag=True, help="Search for all results with visit_again = True data")
def search_entries(term, category, visit_again):
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    term = term.strip().lower() if term else None
    results = []

    if category:
        category = category.strip().lower()
        if category in data:
            if term:
                for entry in data[category]:
                    for value in entry.values():
                        if term in str(value).lower():
                            results.append(entry)
            else:
                results.extend(data[category])

    else:
        for category_name, entries_list in data.items():
            if term:
                for entry in entries_list:
                    for value in entry.values():
                        if term in str(value).lower():
                            results.append(entry)
            else:
                results.extend(entries_list)
            
    if visit_again:
        results = [entry for entry in results if entry["visit_again"] == True]
    
    if results:
        for i, entry in enumerate(results, 1):
            print(f"\n{i}.")
            for key, value in entry.items():
                print(f"   {key.capitalize()}: {value}")
    else:
        print("No results found!")