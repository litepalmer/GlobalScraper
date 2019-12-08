import requests
 
# The url of the page where all the catchup shows are hosted
radiox_splash_url = "https://www.globalplayer.com/catchup/radiox/uk/"

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

show_titles = [i["title"] for i in show_info]
show_ids = [i["id"] for i in show_info]



for item in show_info:
    if item.get('title') in ('Communion Presents'):
        communion = item['id']
        
def grab_id(title, variableLocation):
    for item in show_info:
        if item.get('title') in (title):
            variableLocation = item['id']
 
    
    
grab_id('Communion Presents', communion)    
grab_id('Dan Gasser', gasser)    
grab_id("Dan O'Connell", oconnell)           
        


def get_shows(url):
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
    
shows = get_shows("https://www.globalplayer.com/catchup/radiox/uk/")
