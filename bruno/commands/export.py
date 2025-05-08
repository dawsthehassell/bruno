import click
import os
import json
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command("export", help="Exports the entry log to a .txt or .csv file for easy viewing and sharing.")
@click.option("--format", type=click.Choice(["txt", "csv"]), default="txt", help="Choose export format .txt or .csv")
@click.option("--data-path", default=DATA_PATH, help="Custom data path used for testing")
def export(format, data_path):
    click.echo("Starting export process...")

    try:
        with open(data_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No entries found.")
        return
    
    export_path = click.prompt("Enter filename to export to (without . extension)", default="bruno_export_log", show_default=False).strip()
    
    if not export_path.endswith(f".{format}"):
        export_path += f".{format}"

    export_dir = os.path.dirname(data_path)
    export_full_path = os.path.join(export_dir, export_path)

    if os.path.exists(export_full_path):
        overwrite = click.confirm(f"{export_path} already exists. Overwrite?", default=False)
        if not overwrite:
            click.echo("Export cancelled.")
            return
    
    if format == "txt":
        lines = []
        for category, entries in data.items():
            lines.append(f"==={category.upper()}===\n")
            for entry in entries:
                for key, value in entry.items():
                    lines.append(f"{key.capitalize()}: {value}")
                lines.append("\n")
            lines.append("\n")

        with open(export_full_path, "w") as f:
            f.write("\n".join(lines))

    elif format == "csv":
        columns = [
            "Category", "Name", "Date", "Location", "Company",
            "Drink_ordered", "Food_ordered", "Likes", "Dislikes",
            "Rating", "Visit_again", "Tags", "Live_events," "Vibe", 
            "Seating_availability", "Study_work_friendly", "Activities",
            "Other_activities", "Running", "Pet", "Reason", "Quietness",
            "Type", "Highlight", "Recurring", "Event_again"
        ]

        with open(export_full_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            
            for category, entries in data.items():
                for entry in entries:
                    row = {"Category": category}
                    for field in columns[1:]:
                        row[field] = entry.get(field.lower(), "")
                    writer.writerow(row)
    
    click.echo(f"Entry log successfully exported to {export_full_path}")