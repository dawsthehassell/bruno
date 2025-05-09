# Bruno - Your Personal Experience Logger
**Bruno**, aptly named on the creative Manchester United midfielder, is customizable command-line tool to assist you in tracking experiences like restaurants, coffee shops, parks, events, and more. Bruno helps you log, search, and reflect on your outings with ease and flexibility.

### FEATURES
- Log experiences by category with tailored prompts
- Search your entire log or by keyword/filter by category
- Edit or delete specific entries
- Export your logs to .txt or .csv for easy viewing
- Fully unit tested and ready for use!

### SETUP INSTRUCTIONS
Running on Python 3.7 or newer is recommended.

1. **Clone the repository:**
    git clone https://github.com/dawsthehassell/bruno.git\n
    cd bruno

2. **Create a virtual enviornment (optional, but recommended):**
    python3 -m venv venv\n
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
    pip install click setuptools

4. **Install the package locally in editable mode:**
    pip install -e .

This will install the bruno CLI command and link it to your local development files so changes are reflected immediately.

### CORE FUNCTIONALITY & FEATURES
Bruno has six primary commands:\n

    bruno new         # Add a new entry\n
    bruno search      # Search entries\n
    bruno edit        # Edit an existing entry\n
    bruno delete      # Delete an entry\n
    bruno clear-all   # Clear entire entry log\n
    bruno export      # Export logs to .txt or .csv\n

### EXAMPLE USAGE
    python3 bruno new
    python3 bruno search --category restaurant
    python3 bruno export --format csv
    python3 bruno clear-all --dry-run

### MAIN PROJECT STRUCTURE
    bruno/
    ├── main.py           # CLI group
    ├── new_entry.py
    ├── search_entries.py
    ├── delete_entry.py
    ├── edit_entry.py
    ├── export.py
    ├── clear_log.py
    tests/
    └── test_*.py         # Unit tests
    data/
    └── entry_logs.json   # Stored log

### LISENCE
This project is licensed under the MIT License.