import requests

def get_holidays(api_key, country, year):
    holidays_url = "https://back.holidaylist.io/api/v1/holidays/"
    params = {"country": country, "year": year, "key": api_key}
    
    response = requests.get(holidays_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch holidays. Status code: {response.status_code}"}
