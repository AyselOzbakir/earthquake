import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
import webbrowser

library = []

def fetch_earthquakes():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")[1:]  

    new_data = []
    for row in rows[:10]:  
        cells = row.find_all("td")

        if len(cells) >= 8:
            date = cells[0].text.strip()
            latitude = cells[1].text.strip()
            longitude = cells[2].text.strip()
            depth = cells[3].text.strip()
            magnitude = cells[5].text.strip()
            location = cells[6].text.strip()
            earthquake_id = cells[7].text.strip()

            try:
                magnitude_control = float(magnitude)
            except ValueError:
                continue  

            if earthquake_id not in library and magnitude_control > 2:
                formatted_entry = {
                    "text": f"{date} - {location} - Magnitude: {magnitude} - Depth: {depth} km",
                    "latitude": latitude,
                    "longitude": longitude
                }
                new_data.append(formatted_entry)
                library.append(earthquake_id)  

    return new_data

def open_google_maps(latitude, longitude):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    webbrowser.open(maps_url)

def update_display():
    new_earthquakes = fetch_earthquakes()
    if new_earthquakes:
        for earthquake in new_earthquakes:
            earthquake_display.insert(tk.END, earthquake["text"] + "\n")
            open_maps_button = tk.Button(earthquake_display, text="Open in Google Maps", command=lambda lat=earthquake["latitude"], lon=earthquake["longitude"]: open_google_maps(lat, lon))
            earthquake_display.window_create(tk.END, window=open_maps_button)
            earthquake_display.insert(tk.END, "\n")

    root.after(10000, update_display)  

root = tk.Tk()
root.title("Earthquake Map")
root.geometry("500x300")

earthquake_display = scrolledtext.ScrolledText(root, height=20, width=70)
earthquake_display.pack(pady=8)

update_display()
root.mainloop()
