import urllib.request as req
import json, subprocess

id = "130010" # 東京
url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=" + id 
savename = "weather-info.json"
req.urlretrieve(url, savename)

data = json.load(open(savename, "r", encoding="utf-8"))
# print(data)
text = data['description']['text']
text = text.replace("\n", "")

def exec(cmd):
    r = subprocess.check_output(cmd, shell=True)
    return r.decode("utf-8").strip()

lines = text.split("。")
for s in lines:
    if s == "": continue
    print(s)
    exec('./jtalk.sh "' + s + '"')
