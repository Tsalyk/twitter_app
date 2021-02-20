import folium
from geopy.geocoders import Nominatim
import twitter_friends
geolocator = Nominatim(user_agent="FriendsMap")


def launch(nick: str):
    """
    Main function, launch creation of map
    """
    friends = twitter_friends.parse_data(nick)
    coordinates = find_coordinates(friends)
    gen_map(coordinates)


def find_coordinates(friends: dict) -> set:
    """
    Returns set with coordinates of location
    and names of friends
    """
    coordinates = set()

    for name, city in friends.items():
        location = geolocator.geocode(city)

        if location is not None:
            coordinates.update(list([(name,
                                float(location.latitude),
                                float(location.longitude))]))
    return coordinates


def gen_map(coordinates: set):
    """
    Generates map
    """
    webmap = folium.Map(tiles="Stamen Terrain", zoom_start=18)
    fg = folium.FeatureGroup(name="Friends Map", zoom_start=18)


    for name, lt, ln, in coordinates:
        fg.add_child(folium.Marker(location=[lt, ln],
                                    popup=name,
                                    icon=folium.Icon()))
    webmap.add_child(fg)
    webmap.save('templates/webmap.html')