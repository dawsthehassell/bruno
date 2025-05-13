import click
import os
import json
from bruno.commands.config import DEFAULT_DATA_PATH, ensure_data_dir_exists


@click.command(name="clear-all", help="Clears all entries in the Log with a warning confirmation before deletion.")
@click.option("--force", is_flag=True, help="Skips all warnings and clears entry log immediately. Use with caution!")
@click.option("--dry-run", is_flag=True, help="Simulates the clear-all action without deleting anything.")
@click.option("--data-path", default=DEFAULT_DATA_PATH, help="Path to entry log JSON file")
def clear_all(dry_run, force, data_path):
    ensure_data_dir_exists(data_path)
    click.echo("Starting Clear All entries from log process...")

    if dry_run:
        try:
            with open(data_path, "r") as f:
                data = json.load(f)
            total_entries = sum(len(entries) for entries in data.values())
            click.echo(f"Dry run: This action would delete {len(data)} category(ies) and {total_entries} total entries.")
        except FileNotFoundError:
            click.echo("Dry run: No data found, nothing to delete.")
        return

    if force:
        click.echo("Clearing all entries immediately with --force...")
        with open(data_path, "w") as f:
            json.dump({}, f, indent=2)
        click.echo("All entries have been deleted. Experience Log is now empty.")
        return
    
    clear = click.prompt("Are you sure you want to delete all entries? This cannot be undone! (yes/no)").strip().lower()
    
    if clear == "yes":
        with open(data_path, "w") as f:
            json.dump({}, f, indent=2)
        click.echo("All entries have been deleted. Experience Log is now empty.")
        return
    else:
        click.echo("Clear all action cancelled.")
        return