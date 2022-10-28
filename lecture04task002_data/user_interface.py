# три кнопочки

import data_provider as prov
import logger as log

def temperature_view(sensor):
    data = prov.get_temperature(sensor) # получение данных от провайдера (передаются значения sensor)
    log.temperature_logger(data) # записываем информацию в log (журнал)
    return data # возвращаем значения, которые получили

def pressure_view(sensor):
    data = prov.get_pressure(sensor) # получение данных от провайдера (передаются значения sensor)
    log.pressure_logger(data) # записываем информацию в log (журнал)
    return data # возвращаем значения, которые получили

def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor) # получение данных от провайдера (передаются значения sensor)
    log.wind_speed_logger(data) # записываем информацию в log (журнал)
    return data # возвращаем значения, которые получили




