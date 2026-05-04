from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/{username}")
def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    
    try:
        resp = requests.get(url, timeout=10)
    except Exception as e:
        return {"error": str(e)}
    
    if resp.status_code != 200:
        return {"error": "User not found"}
    
    gists = resp.json()
    result = []
    for gist in gists:
        result.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"]
        })
    return result
