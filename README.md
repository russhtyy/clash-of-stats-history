# Clash of Clans Clan History Scraper

**Overview:**
This Python script uses Clash of Stats and Clash of Clans APIs to retrieve detailed historical clan information for a player. The script now extracts both locations and additional details about each clan in the player's history.

**Dependencies:**
- `requests`: For making HTTP requests to the Clash of Stats and Clash of Clans APIs.
- `threading` and `concurrent.futures`: For concurrent execution of HTTP requests.

**Usage:**
```python
print(get_clans_history('2PP'))```

**Note:**
- Replace ‘2PP’ with the desired player tag to retrieve clan history.
- If player's Clash of Stats clan history is private, an error message indicates that it’s not accessible.
- The script extracts clan infos and country local from historical data.

**Important:**
- Replace ‘YOUR_API_KEY’ with your actual Clash of Clans API key for proper authentication.
- Adhere to the terms of service of Clash of Stats and Clash of Clans APIs.
