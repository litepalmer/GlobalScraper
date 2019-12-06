import requests
 
radiox_splash_url = "https://www.globalplayer.com/catchup/radiox/uk/"

radiox_splash_html = requests.get(radiox_splash_url)
radiox_splash_htmlContent = radiox_splash_html.content
radiox_splash_htmlContent = radiox_splash_htmlContent.decode()

start_of_json = 'type="application/json">'

json_location = radiox_splash_htmlContent.find(start_of_json)
json_location = json_location+24

removed = radiox_splash_htmlContent[json_location:]

end_json_location = removed.index('}}<')
end_json_location = end_json_location+2

final_json = removed[:end_json_location]

import json
 
splash_json = json.loads(final_json)

show_info = splash_json['props']['pageProps']['catchupInfo']

print(2)