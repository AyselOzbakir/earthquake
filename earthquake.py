import requests
from bs4 import BeautifulSoup
import time

library = []  

while True:
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    for i, row in enumerate(rows[:10]):
        cells = row.find_all("td")

        if cells:
            location = cells[6].text.strip()
            magnitude = cells[5].text.strip()
            longitude = cells[3].text.strip()
            date = cells[0].text.strip()
            earthquake_id = cells[7].text.strip()
            
            magnitudecontrol = float(magnitude)
         
            if earthquake_id in library:
                continue
            else:
                if magnitudecontrol > 2:
                    print(location + " Location")
                    print(magnitude +  " Magnitude ")
                    print(longitude + "km deep")
                    print(date)
                    print("\n")     
                    library.append(earthquake_id)

    time.sleep(3)
