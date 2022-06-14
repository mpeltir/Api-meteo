import requests
while True :
    cityName = input("Nom de la ville : ")
    langage = "fr"
    clef = 'be1736317b2be96e299b0c357a52b390'


    apiLien = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={clef}&lang={langage}"
    lien = f"https://api.openweathermap.org/data/2.5/weather?q=Paris&appid={clef}"
    lien2 = f"http://api.openweathermap.org/geo/1.0/direct?q={cityName}&limit=1&appid={clef}"

    json = requests.get(apiLien).json()
    JSON = []
    print(json)
    JSON = json['weather'][0]['description']
    image = f"http://openweathermap.org/img/w/{json['weather'][0]['icon']}.png"
    print(JSON)
    print(image)

