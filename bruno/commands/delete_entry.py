import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="delete", help="Deletes a single entry from the log.")
@click.option("--data-path", default=DATA_PATH, help="Custom data path option for testing")
def delete_entry(data_path):
    click.echo("Starting delete entry process...")

    try:
        with open(data_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return
    
    category = click.prompt("What experience category is the entry you want to delete from? (bar, restaurant, coffee shop, etc.)")

    if category not in data or not data[category]:
        click.echo("No entries found under that category, try again with another category name!")
        return
    
    click.echo(f"\nEntries under category '{category}'")
    for idx, entry in enumerate(data[category]):
        name = entry.get("name", "Unnamed")
        date = entry.get("date", "Unknown date")
        click.echo(f"{idx + 1}. {name} - {date}")
    try:
        choice = int(click.prompt("Enter the numer of the entry you'd like to delete"))
        if not (1 <= choice <= len(data[category])):
            raise ValueError
    except ValueError:
        click.echo("Invalid selection!")
        return
    
    entry = data[category][choice - 1]
    confirm = click.prompt(f"Are you sure you want to delete '{entry.get('name', 'Unnamed')}'? (yes/no)").strip().lower()

    if confirm == "yes":
        del data[category][choice - 1]
        with open(data_path, "w") as f:
            json.dump(data, f, indent=2)
        click.echo("Selected entry has been deleted successfully.")
    else:
        click.echo("Deletion cancelled.")