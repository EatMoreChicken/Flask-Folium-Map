from flask import Flask, render_template
import pandas as pd
import folium
import configparser

app = Flask(__name__)

# Define a function that maps a category to a marker color
def get_marker_color(category):
    # Read the configuration file each time this function is called
    config = configparser.ConfigParser()
    config.read('config.ini')

    return config.get('colors', category, fallback='gray')

# Function to create map and add markers based on location data
def create_map(df, config):
    # Create the map object
    my_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)

    # Iterate over the dataframe and add markers to the map
    for index, row in df.iterrows():
        # Get the marker color based on the category using the get_marker_color function
        color = get_marker_color(row['Category'])
        # Add the marker to the map
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name'], icon=folium.Icon(color=color)).add_to(my_map)

    return my_map

@app.route('/')
def index():
    # Read the CSV file
    df = pd.read_csv('locations.csv')

    # Create the map and add markers based on location data
    my_map = create_map(df, config)

    # Render the HTML template with the map
    map_html = my_map._repr_html_()
    return render_template('index.html', map_html=map_html)

@app.route("/refresh")
def refresh_data():
    # Reload the CSV file
    df = pd.read_csv("locations.csv")

    # Create the map and add markers based on location data and updated color values
    my_map = create_map(df, config)

    # Get the HTML representation of the updated map
    map_html = my_map._repr_html_()

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    app.run()