# GitHub User Activity CLI

## Overview
The **GitHub User Activity CLI** is a command-line tool that fetches and displays the recent activity of a GitHub user. It interacts with the GitHub API to retrieve user events and presents them in a readable format within the terminal.

## Features
- Fetch recent GitHub activity for any user.
- Display structured and user-friendly output.
- Handle errors gracefully (e.g., invalid usernames, API failures).

## Installation
### Prerequisites
- Python 3.x installed on your system.
- A GitHub account (optional for authenticated API requests).

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/shetty456/python-backend.git
   cd python-backend/github-activity-cli
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the CLI tool with a GitHub username:
```sh
python main.py <github_username>
```
Example:
```sh
python main.py torvalds
```
### Output Example
```
Fetching activity for GitHub user: torvalds...

Recent Activity:
- Pushed 3 commits to torvalds/linux
- Opened a new issue in torvalds/linux
- Starred torvalds/linux
```

## Error Handling
If the username is invalid or there is an API error, the tool will return an appropriate message:
```
Error: Invalid GitHub username provided.
Error: Unable to fetch data from GitHub. Please try again later.
```

## API Endpoint
The CLI fetches data from the following GitHub API endpoint:
```
https://api.github.com/users/<username>/events
```
(Replace `<username>` with the actual GitHub username.)

## Technical Details
- **Programming Language:** Python
- **API:** GitHub REST API (`https://api.github.com/users/<username>/events`)
- **Dependencies:** `requests` (for API requests)

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. Please open an issue first for any changes or feature requests.

## Author
Sunil Hanamshetty(https://github.com/shetty456)

