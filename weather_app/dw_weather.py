from pprint import pprint

import requests


def get_weather_dict(lat: float, lon: float) -> dict:
    """
    возвращает словарь с данными о погоде на семь дней
    :param lat:  широта
    :param lon:  долгота
    :return:  словарь с данными о погоде
    """
    try:
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true" \
                      f"&hourly=temperature_2m," \
                      f"relativehumidity_2m,dewpoint_2m,apparent_temperature,surface_pressure,precipitation," \
                      f"weathercode,snow_depth,cloudcover,shortwave_radiation,windspeed_10m,winddirection_10m," \
                      f"windgusts_10m,soil_temperature_6cm,soil_temperature_18cm," \
                      f"soil_moisture_3_9cm&daily=weathercode,temperature_2m_max,temperature_2m_min," \
                      f"apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum," \
                      f"precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant," \
                      f"shortwave_radiation_sum&timeformat=unixtime&timezone=Europe%2FMoscow&windspeed_unit=ms" \
                      f"&past_days=0"
        resp = requests.get(weather_url)
        return resp.json()
    except Exception as ex:
        print(ex)


def loc_to_coord(city_name: str) -> requests.models.Response:
    """
    делает запрос по названию города и возвращает list
    с данными городов с похожими названиями
    :param city_name:
    :return:
    """
    location_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&language=ru"
    resp = requests.get(location_url)
    print('resp_type', type(resp))
    return resp
