import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="edit", help="Load and edit a single entry from the entry log.")
def edit_entry():
    click.echo("\nStarting edit entry process...(type 'cancel' during the process to exit the edit process without saving.)\n")

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return
    
    category = click.prompt("What experience category is the entry you want to edit from? (bar, restaurant, coffee shop, etc.)")
    
    if category not in data or not data[category]:
        click.echo("No entries found under that category, try again with another category name!")
        return
    
    click.echo(f"\nEntries under category '{category}'")
    for idx, entry in enumerate(data[category]):
        name = entry.get("name", "Unnamed")
        date = entry.get("date", "Unknown date")
        click.echo(f"{idx + 1}. {name} - {date}")

    try:
        choice = int(click.prompt("Enter the numer of the entry you'd like to edit"))
        if not (1 <= choice <= len(data[category])):
            raise ValueError
    except ValueError:
        click.echo("Invalid selection!")
        return
    
    click.echo(f"\nType your desired changes or press enter to keep the old value the same!")

    entry = data[category][choice - 1]
    boolean_fields = {
        "visit_again", "study_work_friendly", "running", 
        "pet", "quietness", "event_again", "seating_availability"
    }

    for field, old_value in entry.items():
        if field in boolean_fields:
            response = click.prompt(f"{field} (current: {'yes' if old_value else 'no'})", default="yes" if old_value else "no", show_default=False).strip().lower()
            if response == "cancel":
                click.echo("Edit cancelled. No changes saved.")
                return
            entry[field] = response == "yes"
        else:
            new_value = click.prompt(f"{field} (current: {old_value})", default=old_value, show_default=False)
            if new_value.strip().lower() == "cancel":
                click.echo("Edit cancelled. No changes saved.")
                return
            entry[field] = new_value

    confirm = click.prompt("Save new changes? (yes/no)").strip().lower()
    
    if confirm == "yes":
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=2)
            click.echo("Changes have been saved successfully!")
    else:
        click.echo("Changes have been discarded.")