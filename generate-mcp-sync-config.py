import requests

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
    username = "mcp"
    for repo in list_repos(username):
        if repo == "signatures":
            continue
        print(f"mcp/{repo}:latest: registry.cn-beijing.aliyuncs.com/mcp-mirror/{repo}:latest")