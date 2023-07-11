from geopy.geocoders import Nominatim


def get_latitude_longitude(city_name):
    try:
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(city_name)
        lat = location.latitude
        long = location.longitude
        return lat, long
    except Exception:
        print('Something went wrong!')


if __name__ == '__main__':
    city = input("Enter city: ")
    get_latitude_longitude(city)
