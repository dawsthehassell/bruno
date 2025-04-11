import click
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "entry_logs.json")

@click.command(name="new")
def new():
    click.echo("Starting a new entry log...")
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    category = input("New Experience Catetory (ex: restaurant, coffee shop, etc.): ").strip().lower()
    category_prompts = {
        "restaurant": [
            ("name", "Name of the new restaurant: "),
            ("date", "Date of new restaurant visit: "),
            ("location", "Location: "),
            ("food_ordered", "Food/Drink ordered here: "),
            ("likes", "What did you like about this restuarant experience?: "),
            ("dislikes", "What did you not like about this restuarant experience?: "),
            ("rating", "What would you rate the restaurant out of 5?: "),
            ("visit_again", "Would you visit again? (yes/no): "),
        ],
        "bar": [
            ("name", "Name of new bar: "),
            ("date", "Date of new bar visit: "),
            ("location", "Location: "),
            ("drink_ordered", "Drink/food ordered here: "),
            ("live_events", "Were there live events or music happening (and if so, what?): "),
            ("dislikes", "What did you not like about this bar experience?: "),
            ("vibe", "What was the vibe of this bar?: "),
            ("rating", "What would you rate the bar out of 5?: "),
            ("visit_again", "Would you visit again? (yes/no): "),
        ],
        "coffee shop": [
            ("name", "Name of the new coffee shop: "),
            ("date", "Date of new coffee shop visit: "),
            ("location", "Location: "),
            ("drink_ordered", "Drink/food ordered here: "),
            ("seating_availability", "Was there enough seating availability to stay here? (yes/no): "),
            ("study_work_friendly", "Is this a work/study friendly spot? (yes/no): "),
            ("rating", "What would you rate the restaurant out of 5?: "),
            ("visit_again", "Would you visit again? (yes/no): "),
        ],
        "park": [
            ("name", "Name of the new park: "),
            ("date", "Date of new park visit: "),
            ("location", "Location: "),
            ("activities", "What did you do while here?: "),
            ("other_activities", "What other activities can you do at this park?: "),
            ("running", "Is there a trail or path to run on? (yes/no): "),
            ("pet", "Is this a pet friendly park? (yes/no): "),
            ("visit_again", "Would you visit again? (yes/no): "),
        ],
        "library": [
            ("name", "Name of the new library: "),
            ("date", "Date of new library visit: "),
            ("location", "Location: "),
            ("reason", "What was the reason for the visit? (study, browse, etc.): "),
            ("seating_availability", "Was there enough seating availability to stay here? (yes/no): "),
            ("study_work_friendly", "Is this a work/study friendly spot? (yes/no): "),
            ("quietness", "Would you say this was a quiet enviornnent to be in? (yes/no): "),
            ("visit_again", "Would you visit again? (yes/no): "),
        ],
        "event": [
            ("name", "Name of the new event: "),
            ("date", "Date of new event: "),
            ("type", "What was this type of event?: "),
            ("location", "Location of event: "),
            ("persons", "Who did you attend the event with?: "),
            ("highlight", "What were the highlights?: "),
            ("rating", "What do you rate the experience out of 5?: "),
            ("recurring", "Is this a recurring event (often) or pop up event (yearly, etc.)?: "),
            ("event_again", "Would you do this again? (yes/no): "),
        ]
    }

    boolean_fields = {
        "visit_again", "study_work_friendly", "running", 
        "pet", "quietness", "event_again", "seating_availability"
    }

    if category not in category_prompts:
        print("Invalid category! Please choose a valid experience category.")
        return
    else:
        new_entry = {}
        prompts = category_prompts[category]

        for field, message in prompts:
            if field in boolean_fields:
                response = input(f"{message}").strip().lower()
                new_entry[field] = response == "yes"
            else:
                new_entry[field] = input(f"{message}")

    if category not in data:
        data[category] = []

    data[category].append(new_entry)

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
    
    click.echo("New entry added successfully!")
