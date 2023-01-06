import requests
from bs4 import BeautifulSoup


class Scraper():
    def findSpeci(self, code):
        try:
            response = requests.get("https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi?NoSession=NS_Inconnu&format=dcd&Langue=anglais&Region=can&Stations=" + code + "%20" + code)
            soup = str(BeautifulSoup(response.text, 'html.parser'))
            soup = soup.split("\n")
        except:
            return {"success": False, "payload": "An error has occurred.", "error": {"code": 500, "message": "An error was encountered when attempting to obtain navcanada data."}}
        for row in soup:
            if row.startswith("SPECI") or row.startswith("METAR"):
                return {"success": True, "payload": row}
        return {"success": False, "payload": "An error has occurred.", "error": {"code": 404, "message": "There is no data on an airport with the given code."}}

