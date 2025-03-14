
import requests
import asyncio
import argparse


def fetch_github_user_activity(username: str):
    """Fetch recent GitHub activity of a user using the GitHub API."""
    try:
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if not data:  # Handle users with no recent activity
                print(f"No recent activity found for GitHub user: {username}")
                return None
            return data
        elif response.status_code == 404:
            print(f"Error: GitHub user '{username}' not found.")
        elif response.status_code == 403:
            print("Error: API rate limit exceeded. Try again later.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return None
    except ValueError:
        print(f"Sorry, some error occured")
        return None




async def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity CLI")

    parser.add_argument("username", type=str, help="GitHub username to fetch activity for")
    args = parser.parse_args()

    print(f"Fetching activity for GitHub user: {args.username}...\n")
    activity = await asyncio.to_thread(fetch_github_user_activity, args.username)

    if activity:
        print("\nRecent Activity:")
        for event in activity[:5]:  # Show only the first 5 events
            event_type = event.get("type", "Unknown Event")
            repo_name = event.get("repo", {}).get("name", "Unknown Repo")
            print(f"- {event_type} in {repo_name}")


if __name__ == "__main__":
    asyncio.run(main())
