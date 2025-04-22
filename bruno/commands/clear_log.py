import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="clear-all")
@click.option("--force", is_flag=True, help="Skips all warnings and clears entry log immediately. Use with caution!")
def clear_all(force):
    click.echo("Starting Clear All entries from log process...")

    if force:
        click.echo("Clearing all entries immediately with --force...")
        with open(DATA_PATH, "w") as f:
            json.dump({}, f, indent=2)
        click.echo("All entries have been deleted. Experience Log is now empty.")
        return
    
    clear = click.prompt("Are you sure you want to delete all entries? This cannot be undone! (yes/no)").strip().lower()
    
    if clear == "yes":
        with open(DATA_PATH, "w") as f:
            json.dump({}, f, indent=2)
        click.echo("All entries have been deleted. Experience Log is now empty.")
        return
    else:
        click.echo("Clear all action cancelled.")
        return