import requests
from datetime import datetime

def list_repos(username):
    repos = []
    url = f"https://hub.docker.com/v2/repositories/{username}/?page_size=100"
    while url:
        resp = requests.get(url)
        data = resp.json()
        repos.extend([repo["name"] for repo in data["results"]])
        url = data.get("next")
    return repos

if __name__ == "__main__":
    username = "library"
    day = datetime.now().day
    is_odd_day = day % 2 == 1
    repos = [repo for repo in list_repos(username) if repo != "signatures"]
    for idx, repo in enumerate(repos, start=1):
        if (idx % 2 == 1 and is_odd_day) or (idx % 2 == 0 and not is_odd_day):
            print(f"{repo}:latest: registry.cn-beijing.aliyuncs.com/docker-library-mirror/{repo}:latest")