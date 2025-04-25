import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command("export", help="Exports the entry log to a .txt file for easy viewing and sharing.")
def export():
    click.echo("Starting export process...")

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return
    
    export_filename = click.prompt("Enter filename to export to (ex: my_log.txt)", default="bruno_export_log.txt", show_default=False).strip()
    export_path = os.path.join(BASE_DIR, "..", "data", export_filename)
    if os.path.exists(export_path):
        overwrite = click.confirm(f"{export_path} already exists. Overwrite?", default=False)
        if not overwrite:
            click.echo("Export cancelled.")
            return
    
    lines = []
    for category, entries in data.items():
        lines.append(f"==={category.upper()}===\n")
        for entry in entries:
            for key, value in entry.items():
                lines.append(f"{key.capitalize()}: {value}")
            lines.append("\n")
        lines.append("\n")

    with open(export_path, "w") as f:
        f.write("\n".join(lines))

    click.echo(f"Entry log successfully exported to {export_path}")
