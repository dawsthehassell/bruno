import click
import os
import json
from config import DEFAULT_DATA_PATH, ensure_data_dir_exists

@click.command(name="search", help="Search specific entries by name, category, visit_again, or see them all!")
@click.option("--category", default=None, help="Filter by category (ex: restaurant, coffee shop, etc.)")
@click.option("--term", default=None, help="Search term to look for in entry log")
@click.option("--visit_again", is_flag=True, help="Search for all results with visit_again = True data")
@click.option("--data-path", default=DEFAULT_DATA_PATH, help="Path to entry log JSON file")
def search_entries(term, category, visit_again, data_path):
    ensure_data_dir_exists()
    try:
        with open(data_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return

    term = term.strip().lower() if term else None
    results = []

    if category:
        category = category.strip().lower()
        if category in data:
            if term:
                for entry in data[category]:
                    for value in entry.values():
                        if term in str(value).lower():
                            results.append((category, entry))
            else:
                for entry in data[category]:
                    results.append((category, entry))

    else:
        for category_name, entries_list in data.items():
            if term:
                for entry in entries_list:
                    for value in entry.values():
                        if term in str(value).lower():
                            results.append((category_name, entry))
            else:
                for entry in entries_list:
                    results.append((category_name, entry))
            
    if visit_again:
        results = [(cat, entry) for (cat, entry) in results if entry.get("visit_again") == True]
    
    if results:
        for i, (cat, entry) in enumerate(results, 1):
            print(f"\n{i}.")
            print(f"   Category: {cat}")
            for key, value in entry.items():
                print(f"   {key.capitalize()}: {value}")
    else:
        click.echo("No results found!")