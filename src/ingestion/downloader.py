import requests

def download_file(year: int, month: int, base_url: str):
    filename = f"{year}{month:02d}-divvy-tripdata.zip"
    url = f"{base_url}/{filename}"
    res = requests.get(url, timeout=20)
    res.raise_for_status()
    return res.content