import os
import csv
import sys
import base64
import requests
from datetime import datetime
from dotenv import load_dotenv
from typing import Mapping

load_dotenv()

# Configuration
CF_HANDLE = os.getenv("CF_HANDLE")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
FILE_PATH = os.getenv("FILE_PATH")

headers: Mapping[str, str | bytes] = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_existing_problems():
    """Fetch history.csv from GitHub and extract already solved problem identifiers."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url, headers=headers) # type: ignore

    if response.status_code == 404:
        return set(), "", ""  # File doesn't exist yet
    elif response.status_code == 200:
        data = response.json()
        sha = data["sha"]
        content = base64.b64decode(data["content"]).decode("utf-8")

        existing = set()
        reader = csv.reader(content.splitlines())
        next(reader, None)  # skip header
        for row in reader:
            if len(row) > 2:
                existing.add(row[2])  # "problem" column index
        return existing, content, sha
    else:
        print(f"Error fetching CSV: {response.text}")
        exit(1)

def get_absolute_latest_cf_solve(existing_problems):
    """Fetch only the single latest submission from Codeforces API."""
    url = f"https://codeforces.com/api/user.status?handle={CF_HANDLE}&from=1&count=1"
    try:
        response = requests.get(url).json()
    except Exception:
        print("Network error tracking Codeforces.")
        return None

    if response["status"] != "OK" or not response["result"]:
        return None

    submission = response["result"][0]
    if submission.get("verdict") != "OK":
        print(f"Latest CF submission status is '{submission.get('verdict')}', not 'OK'.")
        return None

    prob = submission["problem"]
    prob_id = f"{prob.get('contestId')}{prob.get('index')}"
    full_prob_identifier = f"{prob_id} - {prob.get('name')}"

    if full_prob_identifier in existing_problems:
        print(f"Latest problem '{full_prob_identifier}' is already tracked in GitHub.")
        return None

    return {
        "date": datetime.fromtimestamp(submission["creationTimeSeconds"]).strftime('%Y-%m-%d'),
        "site": "Codeforces",
        "problem": full_prob_identifier,
        "rating": prob.get("rating", "N/A"),
        "topics": ", ".join(prob.get("tags", [])),
        "result": "AC"
    }

def push_to_github(updated_content, sha):
    """Pushes the updated CSV back to GitHub."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    encoded_content = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

    payload = {
        "message": "Automated log: Added single solved CP problem",
        "content": encoded_content,
        "sha": sha
    }

    res = requests.put(url, json=payload, headers=headers) # type: ignore
    if res.status_code in [200, 201]:
        print("Successfully updated history.csv on GitHub!")
    else:
        print(f"Failed to update GitHub: {res.text}")

def main():
    # 1. Parse Command Line Arguments if provided
    time_min = None
    difficulty = None

    if len(sys.argv) >= 3:
        time_min = sys.argv[1]
        difficulty = sys.argv[2]
        # Validate 1-10 range if it's a digit
        if difficulty.isdigit() and not (1 <= int(difficulty) <= 10):
            print("Warning: Difficulty scale should be between 1 and 10.")

    # 2. Fetch remote status
    print("Fetching tracked history from GitHub...")
    existing_problems, current_csv_text, sha = get_existing_problems()

    # 3. Try to automatically find the latest CF submission
    print("Checking Codeforces for your latest AC submission...")
    latest_solve = get_absolute_latest_cf_solve(existing_problems)

    # 4. Fallback manual creation if CF didn't yield a new problem (or if you are using AtCoder/LeetCode)
    if not latest_solve:
        print("\nCould not automatically fetch a brand new Codeforces solve.")
        choice = input("Would you like to manually log a problem from another site? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting.")
            return

        # Manual entry properties for multi-site flexibility
        site = input("Enter Site Name (e.g., AtCoder, LeetCode, CodeChef): ").strip()
        prob_name = input("Enter Problem Name/ID (e.g., ABC300A - Slot Strategy): ").strip()
        rating = input("Enter Problem Rating/Difficulty level (or N/A): ").strip()
        topics = input("Enter Topics/Tags (comma separated): ").strip()

        latest_solve = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "site": site,
            "problem": prob_name,
            "rating": rating,
            "topics": topics,
            "result": "AC"
        }

    # 5. Handle inputs if they weren't passed as command-line arguments
    print(f"\n--- Logging Problem: {latest_solve['problem']} ({latest_solve['site']}) ---")
    if not time_min:
        time_min = input("Enter time spent in minutes: ").strip()
    if not difficulty:
        while True:
            difficulty = input("Enter difficulty while solving (Scale 1-10): ").strip()
            if difficulty.isdigit() and 1 <= int(difficulty) <= 10:
                break
            print("Please enter a valid number between 1 and 10.")

    new_row = [
        latest_solve["date"],
        latest_solve["site"],
        latest_solve["problem"],
        latest_solve["rating"],
        latest_solve["topics"],
        latest_solve["result"],
        time_min,
        difficulty
    ]

    # Reconstruct and format the CSV text block
    import io
    output = io.StringIO()
    writer = csv.writer(output, lineterminator='\n')

    if not current_csv_text:
        writer.writerow(["date", "site", "problem", "rating", "topics", "result", "time_minutes", "difficulty_while_solving"])
        current_csv_text = output.getvalue()
        output.seek(0)
        output.truncate(0)

    writer.writerow(new_row)
    updated_csv_text = current_csv_text + output.getvalue()

    # 6. Ship back to GitHub
    push_to_github(updated_csv_text, sha)

if __name__ == "__main__":
    main()
