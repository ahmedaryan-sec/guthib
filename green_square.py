import os
from datetime import datetime, timedelta

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

days_back = 365
commits_per_day = 4
start_date = datetime.now() - timedelta(days=days_back)

for i in range(days_back + 1):
    current_date = start_date + timedelta(days=i)
    formatted_date = current_date.strftime("%Y-%m-%dT12:00:00")
    
    for c in range(commits_per_day):
        cmd = f'GIT_COMMITTER_DATE="{formatted_date}" GIT_AUTHOR_DATE="{formatted_date}" git commit --allow-empty -m "Commit {c} for {formatted_date}"'
        os.system(cmd)
        
    print(f"{GREEN}✅ Fake Green Square planted for: {formatted_date}{RESET}")

print(f"\n{RED}🔥 All commits staged! Push to GitHub now!{RESET}")
