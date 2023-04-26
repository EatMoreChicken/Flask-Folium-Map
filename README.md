# 🌍 Flask-Folium Map

This is a simple Flask web application that displays a map of locations stored in a CSV file. The application uses the Folium library to create the map and display markers for each location on the map.

## 🚀 Getting Started

To run this application on your local machine, you'll need to have Python 3 and Flask installed.

1. 👯‍♂️ Clone or download this repository to your local machine.
2. 🚶‍♂️ Navigate to the repository directory in your terminal/command prompt.
3. 📦 Install the required Python packages by running `pip install -r requirements.txt`.
4. 🏃‍♀️ Run the application by executing `python main.py` in your terminal/command prompt.
5. 🌐 Open your web browser, and navigate to `http://localhost:5000` to view the map.

## 🗺️ Using the Map

This map is designed to show the locations around the world. The locations are stored in the `locations.csv` file, which contains the latitude, longitude, name, and category.

The categories are defined in the `config.ini` file, which also specifies the marker color for each category. By default, if a category is not defined in `config.ini`, the marker color will be gray.

To add more locations to the map, simply add new rows to the `locations.csv` file, with the latitude, longitude, name, and category. Then restart the script.

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - A micro web framework for Python
- [Folium](https://python-visualization.github.io/folium/) - A Python library used for creating maps