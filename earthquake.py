import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

# Initialize the library to keep track of earthquake IDs
library = []

def fetch_earthquakes():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    new_data = []
    for i, row in enumerate(rows[:10]):
        cells = row.find_all("td")

        if cells:
            location = cells[6].text.strip()
            magnitude = cells[5].text.strip()
            longitude = cells[3].text.strip()
            date = cells[0].text.strip()
            earthquake_id = cells[7].text.strip()
            
            magnitude_control = float(magnitude)
         
            if earthquake_id not in library and magnitude_control > 2:
                formatted_entry = f"{date} - {location} - Magnitude: {magnitude} - Depth: {longitude} km\n"
                new_data.append(formatted_entry)
                library.append(earthquake_id)
    
    return new_data

def update_display():
    new_earthquakes = fetch_earthquakes()
    if new_earthquakes:
        for earthquake in new_earthquakes:
            earthquake_display.insert(tk.END, earthquake)
    root.after(10000, update_display)  # Update every 10 seconds

# Setup the Tkinter window
root = tk.Tk()
root.title("Earthquake Monitor")
root.geometry("600x400")

# Create a scrolled text widget
earthquake_display = scrolledtext.ScrolledText(root, height=20, width=75)
earthquake_display.pack(pady=20)

# Start the periodic update
update_display()

# Start the Tkinter event loop
root.mainloop()
