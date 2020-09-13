import requests, json, time

corbett = "14109"
lakeland = "12841"
south_cougar = "15877"

sensors = [lakeland, south_cougar]

while True:
    data = requests.get("https://www.purpleair.com/json?show={}".format("|".join(sensors))).json()
    results = ""
    key25 = "pm2_5_atm"
    key10 = "pm10_0_atm"

    for key in [key25, key10]:
        results += '''# TYPE {} gauge
    '''.format(key)
        for sensor in data["results"]:
            label = sensor["Label"].replace(" ", "_")
            reading = sensor[key]
            results += '''{}{{location="{}"}} {}
    '''.format(key, label, reading)
            
    print(results)
    push_body = requests.post("http://mushroom.home.gaffo.org:9091/metrics/job/purple_air", data=results)
    print(push_body.text)
    time.sleep(15)