import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="delete", help="Deletes a single entry from the log.")
def delete_entry():
    click.echo("Starting delete entry process...")

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return
    
    category = click.prompt("What experience category is the entry you want to delete from? (bar, restaurant, coffee shop, etc.)")

    if category not in data or not data[category]:
        click.echo("No entries found under category '{category}'")
        return
    
    ### keep going on this
