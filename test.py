
URL = "https://www.globalplayer.com/catchup/radiox/uk/"
SHOW = "Toby Tarrant"


import requests
import json

splash_html = requests.get(URL).content.decode() # Grab the raw html of the above URL

station_json = json.loads(splash_html[splash_html.find('type="application/json">')+24:splash_html.index('}}<')+2]) # Remove end of the html string and only keep the json object

station_shows = station_json['props']['pageProps']['catchupInfo'] # Remove higher levels of the json object that are needed and only keep the level which contains the shows 
station_name = station_json['props']['pageProps']['stationInfo']['brandName']



show_id = next(item for item in station_shows if item["title"] == SHOW)['id']

show_url = URL + show_id





show_splash_html = requests.get(show_url).content.decode() # Grab the raw html of the above URL

episode_json = json.loads(show_splash_html[show_splash_html.find('type="application/json">')+24:show_splash_html.index('}}<')+2]) # Remove end of the html string and only keep the json object

episode_information = episode_json['props']['pageProps']['catchupInfo']['episodes']



url_list = [i["streamUrl"] for i in episode_information]


date_list = [i['startDate'][:-15] for i in episode_information]



def set_description(filename, artist, title, album, sortTitle):
    from mutagen.mp4 import MP4
    tags = MP4(filename)
    tags['\xa9ART'] = artist #Artist - i.e. Radio Station
    tags['\xa9alb'] = album #Album Title - i.e. Presenter of Show
    tags['\xa9nam'] = title #Title - Date of Show
    tags['\xa9gen'] = "Radio" #Genre - i.e. Radio
    tags['sonm'] = sortTitle #Sort Title - Value to sort alphabetically on
    tags['aART'] = artist #Album Artist - i.e. Radio Station
    tags['cpil'] = True 
    tags.save(filename)


import requests
import datetime
import os.path





for i in range(len(date_list)):
    date = date_list[i]

    print("Downloading "+date)

    day = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%A')
    fullDate = date + " " + day
    titleDate = datetime.datetime.strptime(date, '%Y-%m-%d').strftime(day + ' %d %b %Y')
    showPath = "/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a'
    
    if os.path.isfile(showPath):
        print('file exists')
    else:
        myfile=requests.get(url_list[i])
        open("/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a','wb').write(myfile.content)
        set_description(showPath, albumName, titleDate, showName, fullDate)
        print('File Downloaded')   


date = date_list[0]

print("Downloading "+date)

day = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%A')
fullDate = date + " " + day
titleDate = datetime.datetime.strptime(date, '%Y-%m-%d')
titleDate = titleDate.strftime(day + ' %d %b %Y')
showPath = "/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a'

if os.path.isfile(showPath):
    print('file exists')
else:
    myfile=requests.get(url_list[0])
    open("/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a','wb').write(myfile.content)
    set_description(showPath, albumName, titleDate, showName, fullDate)
    print('File Downloaded') 




import getShows as gs

station_showInfo, station_name = gs.get_show_information("https://www.globalplayer.com/catchup/radiox/uk/")

show_id = gs.get_show_id(station_showInfo, "Toby Tarrant")

show_url = "https://www.globalplayer.com/catchup/radiox/uk/"+show_id

show_list = gs.get_show_list(show_url)

url_list = gs.list_of_urls(show_list)

dates = gs.get_showDates(show_list)

gs.download_url_list(url_list, downloadPath, showName, dates, station_name)