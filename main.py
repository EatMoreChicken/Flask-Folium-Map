"""
Flask app that displays a map of locations and supports refreshing the data.
"""

import configparser
from flask import Flask, render_template
import pandas as pd
import folium

app = Flask(__name__)

def get_marker_color(category):
    """
    Maps a category to a marker color from the config file.
    """
    # Read the configuration file each time this function is called
    config = configparser.ConfigParser()
    config.read('config.ini')

    return config.get('colors', category, fallback='gray')

def create_map(data_frame, config_parser):
    """
    Creates a Folium map object and adds markers based on location data.
    """
    # Create the map object
    my_map = folium.Map(location=[data_frame['Latitude'].mean(), data_frame['Longitude'].mean()], zoom_start=5)

    # Iterate over the dataframe and add markers to the map
    for _, row in data_frame.iterrows():
        # Get the marker color based on the category using the get_marker_color function
        color = get_marker_color(row['Category'])
        # Add the marker to the map
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name'], icon=folium.Icon(color=color)).add_to(my_map)

    return my_map

@app.route('/')
def index():
    """
    Renders the index.html template with the map.
    """
    # Read the CSV file
    data_frame = pd.read_csv('locations.csv')

    # Create the map and add markers based on location data
    my_map = create_map(data_frame, config_parser)

    # Render the updated map for the index.html template
    return render_template('index.html', map_html=my_map._repr_html_())

@app.route("/refresh")
def refresh_data():
    """
    Reloads the CSV file, recreates the map with updated data, and renders the updated map in the index.html template.
    """
    # Reload the CSV file
    data_frame = pd.read_csv("locations.csv")

    # Create the map with updated data and add markers based on location data and updated color values
    my_map = create_map(data_frame, config_parser)

    # Render the updated map for the index.html template
    return render_template('index.html', map_html=my_map._repr_html_())

if __name__ == '__main__':
    # Read the configuration file
    config_parser = configparser.ConfigParser()
    config_parser.read('config.ini')

    app.run()
