
# Gets both the shows operated by a specific radiostation and returns then as a dictionary within a list
# Also returns the show name as a string to be used by a later function
def get_show_information(url):
    import requests
    import json

    splash_html = requests.get(url).content.decode() # Grab the raw html of the above URL

    station_json = json.loads(splash_html[splash_html.find('type="application/json">')+24:splash_html.index('}}<')+2]) # Remove end of the html string and only keep the json object

    station_shows = station_json['props']['pageProps']['catchupInfo'] # Remove higher levels of the json object that are needed and only keep the level which contains the shows 
    station_name = station_json['props']['pageProps']['stationInfo']['brandName']

    return(station_shows, station_name)

 
def get_show_id(show_dict, request_show):
    show_id = next(item for item in show_dict if item["title"] == request_show)['id']
    return(show_id)
    
def get_show_list(show_url):
    import requests
    import json

    show_splash_html = requests.get(show_url).content.decode() # Grab the raw html of the above URL

    episode_json = json.loads(show_splash_html[show_splash_html.find('type="application/json">')+24:show_splash_html.index('}}<')+2]) # Remove end of the html string and only keep the json object

    episode_information = episode_json['props']['pageProps']['catchupInfo']['episodes']
    return(episode_information)


def list_of_urls(list_of_shows):
    url_list = [i["streamUrl"] for i in list_of_shows]
    return(url_list)
    
def download_url_list(urls_to_download, 
                      downloadPath, 
                      showName, 
                      datesOfShows,
                      albumName):
    import requests
    import datetime
    import os.path
    for i in range(len(datesOfShows)):

    

        fullDate = datesOfShows[i] + " " + datetime.datetime.strptime(datesOfShows[i],'%Y-%m-%d').strftime('%A')
        titleDate = datetime.datetime.strptime(datesOfShows[i], '%Y-%m-%d').strftime(datetime.datetime.strptime(datesOfShows[i],'%Y-%m-%d').strftime('%A') + ' %d %b %Y')
        showPath = "/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a'
        
        if os.path.isfile(showPath):
            print('file exists')
        else:
            print("Downloading "+fullDate)
            myfile=requests.get(urls_to_download[i])
            open("/Volumes/Public/Media/Radio/Radio X/Toby Tarrant/"+fullDate+'.m4a','wb').write(myfile.content)
            set_description(showPath, albumName, titleDate, showName, fullDate)
            print('File Downloaded')             
        
def get_showDates(listOfShows):
    date_list = [i['startDate'][:-15] for i in listOfShows]
    return(date_list)
    
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

def listOfShows(station_information):
    shows = []
    for i in range(len(station_information)):
        shows.append((station_information[i]['title']))
     
    return(shows)
           
def download_show(station_name, showName, downloadPath):
    stations = {
        "radiox" : "https://www.globalplayer.com/catchup/radiox/uk/",
        "gold" : "https://www.globalplayer.com/catchup/gold/uk/",
        "classicfm" : "https://www.globalplayer.com/catchup/classicfm/uk/",
        "lbcnews" : "https://www.globalplayer.com/catchup/lbcnews/uk/",
        "lbc" : "https://www.globalplayer.com/catchup/lbc/uk/",
        "capital" : "https://www.globalplayer.com/catchup/capital/uk/",
        "capitalxtra" : "https://www.globalplayer.com/catchup/capitalxtra/uk/",
        "capitalxtrareloaded" : "https://www.globalplayer.com/catchup/capitalxtrareloaded/uk/",
        "heart" : "https://www.globalplayer.com/catchup/heart/uk/",
        "heart70s" : "https://www.globalplayer.com/catchup/heart70s/uk/",
        "heart80s" : "https://www.globalplayer.com/catchup/heart80s/uk/",
        "heart90s" : "https://www.globalplayer.com/catchup/heart90s/uk/",
        "heartdance" : "https://www.globalplayer.com/catchup/heartdance/uk/",
        "heartxtraxmas" : "https://www.globalplayer.com/catchup/heartextra/uk/",
        "smooth" : "https://www.globalplayer.com/catchup/smooth/uk/",
        "smoothchill" : "https://www.globalplayer.com/catchup/smoothchill/uk/",
        "smoothcountry" : "https://www.globalplayer.com/catchup/smoothcountry/uk/",
        "smoothextra" : "https://www.globalplayer.com/catchup/smoothextra/uk/"
    }
    
    station_url = stations[station_name]
    
    import getShows as gs

    station_showInfo, station_name = gs.get_show_information(station_url)

    show_id = gs.get_show_id(station_showInfo, showName)
    
    show_url = station_url+show_id

    show_list = gs.get_show_list(show_url)

    url_list = gs.list_of_urls(show_list)
    
    dates = gs.get_showDates(show_list)

    gs.download_url_list(url_list, downloadPath, showName, dates, station_name)
    