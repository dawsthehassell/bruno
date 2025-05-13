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

To install Bruno globally and use it as a command-line tool, follow these steps:

1. **Clone the repository:**
    ```
    git clone https://github.com/dawsthehassell/bruno.git
    cd bruno
2. **Install pipx (if you don't have it already):**
    ```
    brew install pipx  # On MacOS using Homebrew
    python3 -m pip install --user pipx  # For other systems
3. **Install Bruno globally using pipx:**
    ```
    pipx install .
This will install the Bruno in an isolated enviorment, and you'll be able to run any Bruno command globally! Bruno's Entry Log will be saved in the user's main/home directory (/Users/yourusername/.bruno/entry_logs.json)

### DEVELOPING BRUNO WITH pipx (editable mode)
If you'd like to actively develop Bruno and want changes to reflect immediately without constant reinstallation, use the following command:
    ```
    pipx install --editable .
    ```
This command will install Bruno in editable mode, so changes will be reflected immediately. 

### UNINSTALLING BRUNO
To uninstall Bruno, it's as simple as:
    ```
    pipx uninstall bruno
    ```

### CORE FUNCTIONALITY & FEATURES
Bruno has six primary commands:

    bruno new         # Add a new entry
    bruno search      # Search entries
    bruno edit        # Edit an existing entry
    bruno delete      # Delete an entry
    bruno clear-all   # Clear entire entry log
    bruno export      # Export logs to .txt or .csv

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
    ├── config.py         # Sets data path
    tests/
    └── test_*.py         # Unit tests
    

### LISENCE
This project is licensed under the MIT License.