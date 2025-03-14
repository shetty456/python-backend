import asyncio
import requests
import argparse
import json
from enum import Enum
from dotenv import load_dotenv
import os

# TODO: add env file to save the token locally and use dotenv to load it here

# load variables from env
load_dotenv()

tmdb_token = os.getenv('TMDB_TOKEN')

class MovieType(Enum):
    playing = "now_playing"
    popular = "popular"
    top = "top_rated"
    upcoming = "upcoming"

def fetch_tmdb_movies(movie_type: str):
    """Fetch movies based on the TMDB API"""
    try:
        # Validate TMDB token
        if not tmdb_token:
            raise ValueError("TMDB_TOKEN is missing. Set it in the .env file.")

        # Change URL endpoint based on movie type
        url = f"https://api.themoviedb.org/3/movie/{movie_type}?language=en-US&page=1"
        print(f"Fetching data from: {url}")

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {tmdb_token}"
        }

        print(headers)

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from TMDB: {e}")
        return None  # Return None or an empty dict {} if you prefer

    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None


async def main():
    parser = argparse.ArgumentParser(description="TMDB CLI")
    parser.add_argument("--type", type=str, 
                        choices=[e.name for e in MovieType],
                        required=True,  
                        help="TMDB movie type (playing, popular, top, upcoming)",
                        )
    args = parser.parse_args()

    # Convert input to Enum to fetch correct API value
    movie_type_enum = MovieType[args.type]
    
    print(f"Fetching movies for movie type: {args.type} ({movie_type_enum.value})...\n")

    fetched_movies = await asyncio.to_thread(fetch_tmdb_movies, movie_type_enum.value)
    print(json.dumps(fetched_movies, indent=4))
    

if __name__ == "__main__":
    asyncio.run(main())