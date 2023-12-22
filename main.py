import requests
from threading import Thread
import concurrent.futures

def get_status(url):
    return requests.get(url=url, headers={"Accept": "application/json", "authorization": f"Bearer YOUR_API_KEY"}).json()

def get_urls(urls):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_status, url=url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results
        
def get_clans_history(tag):
    req = requests.get(f'https://api.clashofstats.com/players/{tag}/history/clans').json()
    if req.get('error'):
        return {"success": False, "error": "clan history is private"}
    clan_tags = [f'https://api.clashofclans.com/v1/clans/%23{tag[1:]}' for tag in req['clansMap'].keys()]        
    clans_result = get_urls(clan_tags)
    # Extract relevant information from clans_result (modify as needed)
    clans_info = [{"name": clan.get("name"), "location": clan.get("location", {}).get("name")} for clan in clans_result]
    return {"clans_info": clans_info}
    
print(get_clans_history('2PP'))
