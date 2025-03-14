# TMDB CLI Tool

## Overview
The **TMDB CLI Tool** is a command-line interface (CLI) application that interacts with [The Movie Database (TMDB) API](https://www.themoviedb.org/) to fetch and display movie information directly in the terminal. Users can query different categories of movies using command-line arguments.

## Repository
GitHub Repository: [TMDB CLI](https://github.com/shetty456/python-backend/tree/main/tmdb-cli)

## Features
- Fetches movie information from the TMDB API.
- Displays movies in an organized format in the terminal.
- Supports filtering movies by predefined categories:
  - Now Playing
  - Popular
  - Top Rated
  - Upcoming
- Handles API failures, network issues, and invalid user inputs gracefully.

## Installation
### Prerequisites
- Python 3.7+
- TMDB API Key ([Get one here](https://developer.themoviedb.org/docs/getting-started))

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shetty456/python-backend.git
   cd python-backend/tmdb-cli
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file in the project root and add your TMDB API key:
   ```
   TMDB_TOKEN=your_tmdb_api_key
   ```

## Usage
Run the CLI tool with the following command-line arguments:
```bash
python tmdb_app.py --type "popular"
```
Available options for `--type`:
- `playing`   → Now Playing
- `popular`   → Popular Movies
- `top`       → Top Rated Movies
- `upcoming`  → Upcoming Movies

### Example Commands
Fetch popular movies:
```bash
python tmdb_app.py --type "popular"
```
Fetch top-rated movies:
```bash
python tmdb_app.py --type "top"
```

## Error Handling
- **Invalid API Key:** Displays a user-friendly message if the API key is missing or incorrect.
- **Network Issues:** Handles connection errors and timeouts.
- **Invalid Input:** Provides feedback if the user inputs an unsupported category.

## Technical Details
- **Programming Language:** Python
- **Dependencies:**
  - `requests` for API calls
  - `argparse` for CLI argument handling
  - `dotenv` for loading environment variables
- **API Endpoint:** `https://api.themoviedb.org/3/movie/{category}`


## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, feel free to open an issue or submit a pull request on GitHub!

---

Happy coding! 🎬🚀

