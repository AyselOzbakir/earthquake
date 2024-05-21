## Overview
 This Python script tracks recent earthquakes using data from the Afad Earthquake Database.
 It retrieves earthquake information from the database and prints details about earthquakes
 with a magnitude greater than 2 on the Richter scale.

## Prerequisites
 To use this script, you need to have Python installed on your system. You also need to
install the following libraries:
 - requests
 - beautifulsoup4

# You can install these libraries using pip:
pip install requests beautifulsoup4 pywebview


## Usage
 1. Clone the repository to your local machine or download the `earthquake_tracker.py` script.
 2. Navigate to the directory where the script is located.
 3. Run the script using Python:
 python earthquake_tracker.py
The script will continuously track earthquakes and display information about those with a magnitude greater than 2. It will also show the exact location of the earthquake within a Tkinter window with a button to open Google Maps.
