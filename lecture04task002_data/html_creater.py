from cgitb import html
from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

# для html используются спец.библиотеки, но мы сделаем вручную

def create(device = 1):
    style = 'style="font-size:30px;"' 
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} c</p>\n'\
            .format(style, temperature_view(device))
    html += '   <p {}>Wind_speed: {} c</p>\n'\
            .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} c</p>\n'\
            .format(style, pressure_view(device))

    with open('index.html', 'w') as page: # создаем файл
        page.write(html) # сохраняем файл

    return html


# дополнительно. без этого метода уже все работает
    def new_create(data, device = 1):
        t, p, w = data # разбили на отдельные переменные
        style = 'style="font-size:30px;"' 
        html = '<html>\n <head></head>\n <body>\n'
        html += '   <p {}>Temperature: {} c</p>\n'\
                 .format(style, t)
        html += '   <p {}>Wind_speed: {} c</p>\n'\
                 .format(style, w)
        html += '   <p {}>Pressure: {} c</p>\n'\
                 .format(style, p)

        with open('new_index.html', 'w') as page: # создаем файл
                page.write(html) # сохраняем файл

        return html