import os
import random
import subprocess
from datetime import datetime, timedelta

def make_commit(date, repo_path, filename, message="Learning and Growing!"):
    filepath = os.path.join(repo_path, filename)
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env)

def generate_historical_commits(repo_path, filename):
    # Year 2022: Beginner phase (60-100 commits)
    # Randomly pick 4-6 months, few commits in those months
    print("Generating commits for 2022...")
    commits_2022 = random.randint(60, 100)
    months_2022 = random.sample(range(1, 13), 6) # Active in 6 random months
    for _ in range(commits_2022):
        month = random.choice(months_2022)
        day = random.randint(1, 28)
        hour = random.randint(9, 21)
        commit_date = datetime(2022, month, day, hour, random.randint(0, 59))
        make_commit(commit_date, repo_path, filename, "2022: Learning basics")

    # Year 2023: Progressing (70-100 commits)
    print("Generating commits for 2023...")
    commits_2023 = random.randint(70, 100)
    months_2023 = random.sample(range(1, 13), 8) # Active in 8 months
    for _ in range(commits_2023):
        month = random.choice(months_2023)
        day = random.randint(1, 28)
        commit_date = datetime(2023, month, day, random.randint(9, 22))
        make_commit(commit_date, repo_path, filename, "2023: Project updates")

    # Year 2024: Growing (80-100 commits)
    print("Generating commits for 2024...")
    commits_2024 = random.randint(80, 100)
    for _ in range(commits_2024):
        month = random.randint(1, 12) # Active throughout the year
        day = random.randint(1, 28)
        commit_date = datetime(2024, month, day, random.randint(8, 23))
        make_commit(commit_date, repo_path, filename, "2024: Advanced features")

def generate_nearby_commits(repo_path, filename):
    # 2025: 100+ commits
    print("Generating 2025 commits for nearbyhiring-demo...")
    for i in range(120):
        # 2025 activity spread
        month = (i // 10) + 1
        day = (i % 28) + 1
        if month > 12: month = 12
        commit_date = datetime(2025, month, day, random.randint(9, 20))
        make_commit(commit_date, repo_path, filename, "NearbyHiring: Feature development")

    # 2026: Daily 5-6 commits for 120 days
    print("Generating 2026 daily commits for nearbyhiring-demo...")
    start_date = datetime(2026, 1, 1)
    for d in range(120):
        current_day = start_date + timedelta(days=d)
        num_today = random.randint(5, 6)
        for _ in range(num_today):
            commit_time = current_day.replace(hour=random.randint(9, 21), minute=random.randint(0, 59))
            make_commit(commit_time, repo_path, filename, "NearbyHiring: Daily Progress")

def main():
    # Repo 1: project-green-box (Historical)
    green_box_path = r"C:\Users\user\OneDrive\Desktop\project-green-box"
    generate_historical_commits(green_box_path, "history.txt")
    print("Pushing historical commits...")
    subprocess.run(["git", "push"], cwd=green_box_path)

    # Repo 2: nearbyhiring-demo (Intense)
    nearby_path = r"C:\Users\user\OneDrive\Desktop\nearbyhiring-demo"
    # Ensure local config is set to pranavsahu005 to avoid account mixup
    subprocess.run(["git", "config", "user.name", "Pranav Sahu"], cwd=nearby_path)
    subprocess.run(["git", "config", "user.email", "pranavsahu005@gmail.com"], cwd=nearby_path)
    
    generate_nearby_commits(nearby_path, "activity_log.txt")
    print("Pushing NearbyHiring commits...")
    subprocess.run(["git", "push"], cwd=nearby_path)

if __name__ == "__main__":
    main()
