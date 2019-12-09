def get_all_shows(url):
    import requests
    # The url of the page where all the catchup shows are hosted
    radiox_splash_url = url
    # Grab the raw html of the above URL
    radiox_splash_html = requests.get(radiox_splash_url)
    # Remove the html content from the above object into its own variable
    radiox_splash_htmlContent = radiox_splash_html.content
    # Turn the variable into a string to allow indexing and location of embedded json
    radiox_splash_htmlContent = radiox_splash_htmlContent.decode()
    # String to identify the start of the embedded json object within the html string
    start_of_json = 'type="application/json">'
    # Numeric location of the start of the json object
    json_location = radiox_splash_htmlContent.find(start_of_json)
    json_location = json_location+24 
    # Remove the start of the html string up to the start of the json object
    removed = radiox_splash_htmlContent[json_location:]
    # Numeric location of the end of the json object
    end_json_location = removed.index('}}<')
    end_json_location = end_json_location+2
    # Remove end of the html string and only keep the json object
    final_json = removed[:end_json_location]
    import json
    # Turn the json object into a dictionary
    splash_json = json.loads(final_json)
    # Remove higher levels of the json object that are needed and only keep the 
    # level which contains the shows 
    show_info = splash_json['props']['pageProps']['catchupInfo']
    return(show_info)
    
def get_show_id(show_dict, request_show):
    import pandas as pd
    x = pd.DataFrame.from_dict(show_dict)
    y = x[x['title'].str.match(request_show)]
    show_id = y.iloc[0]['id']
    return(show_id)
    
def get_show_list(url):
    import requests
    show_html = requests.get(url)

    show_html_content = show_html.content.decode()
    start_of_json = 'type="application/json">'
    json_location = show_html_content.find(start_of_json)
    json_location = json_location + 24

    removed = show_html_content[json_location:]

    end_json_location = removed.index('}}<')
    end_json_location = end_json_location+2

    final_json = removed[:end_json_location]

    import json

    show_json = json.loads(final_json)

    show_info = show_json['props']['pageProps']['catchupInfo']['episodes']
    return(show_info)

def list_of_urls(list_of_shows):
    url_list = [i["streamUrl"] for i in list_of_shows]
    return(url_list)
    
def download_url_list(urls_to_download, 
                      downloadPath, 
                      showName, 
                      datesOfShows,
                      albumName,
                      genre):
    import requests
    import datetime
    for i in range(len(datesOfShows)):
        date = datesOfShows[i]
        print("Downloading "+date)
        myfile=requests.get(urls_to_download[i])
        final_url = downloadPath+showName+" "+str(date+'.m4a')
        day = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%A')
        fullDate = date + " " + day
        titleDate = datetime.datetime.strptime(date, '%Y-%m-%d')
        titleDate = titleDate.strftime(day + ' %d %b %Y')
        open(downloadPath+showName+" "+str(date)+'.m4a','wb').write(myfile.content)
        set_description(final_url, albumName, titleDate, showName, genre, fullDate)
        print('File Downloaded')
        
def get_showDates(listOfShows):
    import pandas as pd
    x = pd.DataFrame.from_dict(listOfShows)

    startDates = x.iloc[0:,[5]]
    startDates = startDates.values.tolist()
    startDates = [str(i) for i in startDates]

    startDates = [x[:-17] for x in startDates]
    startDates = [x[2:] for x in startDates]
    return(startDates)
    
def set_description(filename, artist, title, album, genre, sortTitle):
    from mutagen.mp4 import MP4
    tags = MP4(filename)
    tags['\xa9ART'] = artist
    tags['\xa9nam'] = title
    tags['\xa9alb'] = album
    tags['\xa9gen'] = genre
    tags['sonm'] = sortTitle
    tags.save(filename)
    

        
def download_show(url, showName, downloadPath, albumName, genre):
    radiox = "https://www.globalplayer.com/catchup/radiox/uk/"
    gold = "https://www.globalplayer.com/catchup/gold/uk/"
    classicfm = "https://www.globalplayer.com/catchup/classicfm/uk/"
    lbcnews = "https://www.globalplayer.com/catchup/lbcnews/uk/"
    lbc = "https://www.globalplayer.com/catchup/lbc/uk/"
    capital = "https://www.globalplayer.com/catchup/capital/uk/"
    capitalxtra = "https://www.globalplayer.com/catchup/capitalxtra/uk/"
    capitalxtrareloaded = "https://www.globalplayer.com/catchup/capitalxtrareloaded/uk/"
    heart = "https://www.globalplayer.com/catchup/heart/uk/"
    heart70s = "https://www.globalplayer.com/catchup/heart70s/uk/"
    heart80s = "https://www.globalplayer.com/catchup/heart80s/uk/"
    heart90s = "https://www.globalplayer.com/catchup/heart90s/uk/"
    heartdance = "https://www.globalplayer.com/catchup/heartdance/uk/"
    heartxtraxmas = "https://www.globalplayer.com/catchup/heartextra/uk/"
    smooth = "https://www.globalplayer.com/catchup/smooth/uk/"
    smoothchill = "https://www.globalplayer.com/catchup/smoothchill/uk/"
    smoothcountry = "https://www.globalplayer.com/catchup/smoothcountry/uk/"

    
    if url == 'radiox':
        radioX_url = radiox
    elif url == 'gold':
        radioX_url = gold
    elif url == 'classicfm':
        radioX_url = classicfm
    elif url == 'lbcnews':
        radioX_url = lbcnews
    elif url == 'capital':
        radioX_url = capital
    elif url == 'capitalxtra':
        radioX_url = capitalxtra
    elif url == 'capitalxtrareloaded':
        radioX_url = capitalxtrareloaded
    elif url == 'heart':
        radioX_url = heart
    elif url == 'heart70s':
        radioX_url = heart70s
    elif url == 'heart80s':
        radioX_url = heart80s
    elif url == 'heart90s':
        radioX_url = heart90s
    elif url == 'heartdance':
        radioX_url = heartdance
    elif url == 'heartxtraxmas':
        radioX_url = heartxtraxmas
    elif url == 'smooth':
        radioX_url = smooth
    elif url == 'smoothchill':
        radioX_url = smoothchill
    elif url == 'smoothcountry':
        radioX_url = smoothcountry
    elif url == 'lbc':
        radioX_url = lbc
    else:
        radioX_url == "https://www.globalplayer.com/catchup/smoothextra/uk/"
    
    import getShows as gs

    radioX_showInfo = gs.get_all_shows(radioX_url)

    chris_id = gs.get_show_id(radioX_showInfo, showName)
    
    chris_url = radioX_url+chris_id

    show_list = gs.get_show_list(chris_url)

    url_list = gs.list_of_urls(show_list)
    
    dates = gs.get_showDates(show_list)

    gs.download_url_list(url_list, downloadPath, showName, dates, albumName, genre)
    