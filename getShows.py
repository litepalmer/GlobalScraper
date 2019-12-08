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
    
def download_url_list(urls_to_download, downloadPath, fileName):
    import requests
    count=0
    for n in urls_to_download:
        count = count+1
        myfile=requests.get(n)
        open(downloadPath+fileName+str(count)+'.m4a','wb').write(myfile.content)
        print('file downloaded')
        
def download_show(url, showName, downloadPath, fileName):
    import getShows as gs
    radioX_url = url

    radioX_showInfo = gs.get_all_shows(radioX_url)

    chris_id = gs.get_show_id(radioX_showInfo, showName)
    
    chris_url = radioX_url+chris_id

    show_list = gs.get_show_list(chris_url)

    url_list = gs.list_of_urls(show_list)

    gs.download_url_list(url_list, downloadPath, fileName)
    