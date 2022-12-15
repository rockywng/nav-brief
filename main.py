import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

def findSpeci(code, count = 1):
    response = requests.get("https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi?NoSession=NS_Inconnu&format=dcd&Langue=anglais&Region=can&Stations=" + code + "%20" + code)
    soup = str(BeautifulSoup(response.text, 'html.parser'))
    soup = soup.split("\n")
    for row in soup:
        if row.startswith("SPECI") or row.startswith("METAR"):
            print(row)
            return row
    return "Failure"

#code = input("What code hoe?")
#code = str(code)
#full = findSpeci(code)

@app.get("/nav-brief")
def get(code: str):
    return {findSpeci(code)}