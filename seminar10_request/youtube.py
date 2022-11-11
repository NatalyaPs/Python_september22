from pytube import YouTube

# функция для видео из Ютуба в Телеграм
def yt_do(url):
    yt = YouTube(url)
    yt.streams.filter(res="360p".first().download(filename=f'name.mp4'))


yt_do(input('https://www.youtube.com/watch?v=sn6mhLTj5Ts')) # Слэйд
yt_do(input('https://www.youtube.com/watch?v=YYVR5lO9Ouo')) # Сонни и Шер



# # или вариант без функции:
# yt = YouTube('https://www.youtube.com/watch?v=YYVR5lO9Ouo')
# yt.streams.filter(res="360p".first().download(filename=f'name.mp.4'))
# print(yt.title)