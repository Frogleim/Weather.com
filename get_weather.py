import requests
from get_coordinates import get_latitude_longitude


def get_weather(latitude, longitude):
    url = 'https://weather.com/api/v1/p/redux-dal'

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "speedpin=4G; usprivacy=1---; ab.storage.deviceId.93cb108c-fa32-4edb-b34c-53500de65387=%7B%22g%22%3A"
                  "%22f1975b4f-e8f5-5f53-3320-f854558b9b1c%22%2C%22c%22%3A1689081788700%2C%22l%22%3A1689081788700%7D; "
                  "mdLogger=false; kampyle_userid=71fc-6c3d-db83-99b1-9a85-54cf-30df-f4a0; "
                  "trc_cookie_storage=taboola%2520global%253Auser-id%3D07b4d324-b7e4-44bb-b31e-5f417b85cc15"
                  "-tuctb3bf51a; "
                  "fv=-1; kampyleUserSession=1689082690032; kampyleUserSessionsCount=7; "
                  "kampyleUserPercentile=57.12453861720115; "
                  "wxu-metrics-session=4442213f-a0e9-4a34-b248-7bf8cd50a104:1689081787916:17; "
                  "ab.storage.sessionId.93cb108c-fa32-4edb-b34c-53500de65387=%7B%22g%22%3A%22d82405ee-3450-fb15-e6de"
                  "-6a15b081a2c4%22%2C%22e%22%3A1689084608417%2C%22c%22%3A1689081788698%2C%22l%22%3A1689082808417%7D; "
                  "cto_bundle"
                  "=0p27VF9uMEFXWlI0"
                  "QTBScWNxM0tRVDlZc2kxbHp6cGZRV00weWVRNTJIczlTQzUlMkZuQVdYR0xma1ZNaWdRSVJuWTBYVWUyclZTQlBTZE9"
                  "VJTJGbEVnRWI "
                  "2MDFvRmJjNXUwcWFLW "
                  "UwxNUFLJTJGSDBVMnNXQnVUTU9oR1JiSlAxc2dvOUxpeVV4V1pPWWxad05Ra1JTckRBTm44QVQ4WGclM0QlM0Q; "
                  "wxu-user-poll=skip; kampyleSessionPageCounter=5; "
                  "RT=\"z=1&dm=weather.com&si=5d0a2a9d-7493-4a37-b117-2f154de7b9c0&ss=ljybom6l&sl=a&tt=53p&obo=7&rl=1"
                  "&ld "
                  "=mjok&r=16u0y5oiq&ul=mjol&hd=mjur\"; "
                  "ci=TWC-Connection-Speed=4G&TWC-Locale-Group=US&TWC-Device-Class=desktop&X-Origin-Hint=Prod-IBM"
                  "-script "
                  "-service&TWC-Network-Type=wifi&TWC- "
                  "GeoIP-Country=AM&TWC-GeoIP-Lat=40.18&TWC-GeoIP-Long=44.50&Akamai-Connection-Speed=1000+&TWC-Privacy"
                  "=exempt&TWC-GeoIP-DMA=&TWC-GeoIP "
                  "-City=EREVAN&TWC-GeoIP-Region=",
        "Referer": "https://weather.com/",
        "Referrer-Policy": "origin"
    }

    body = [{"name": "getSunWeatherAlertHeadlinesUrlConfig",
             "params": {"geocode": f"{latitude},{longitude}", "units": "e"}},
            {"name": "getSunV3CurrentObservationsUrlConfig",
             "params": {"geocode": f"{latitude},{longitude}", "units": "e"}},
            {"name": "getSunV3DailyForecastWithHeadersUrlConfig",
             "params": {"duration": "7day", "geocode": f"{latitude},{longitude}", "units": "e"}},
            {"name": "getSunIndexPollenDaypartUrlConfig",
             "params": {"duration": "3day", "geocode": f"{latitude},{longitude}",
                        "units": "e"}}]
    try:
        r = requests.post(url=url, headers=headers, json=body)
        data = r.json()['dal']['getSunV3CurrentObservationsUrlConfig'][f'geocode:{latitude},{longitude};units:e'][
            'data']
        temperature_now = round((data['temperature'] - 32) * 5 / 9, 2)
        max24hours = round((data['temperatureMax24Hour'] - 32) * 5 / 9, 2)
        min24hours = round((data['temperatureMin24Hour'] - 32) * 5 / 9, 2)
        wind_speed = round(data['windSpeed'] * 1.60934, 2)
        humidity = data['relativeHumidity']

        print(f'Today at Moscow Right now: {temperature_now}°, Max: {max24hours}°,Min: {min24hours}°\n'
              f'Wind Speed: {wind_speed}kmh, Humidity: {humidity}%')

    except Exception as e:
        print(f'Something went wrong!\n {e}')


if __name__ == "__main__":
    city = input("Enter city: ")
    lat, long = get_latitude_longitude(city)
    get_weather(latitude=lat, longitude=long)
