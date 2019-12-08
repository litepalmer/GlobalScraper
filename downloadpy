import getShows as gs


radioX_url = "https://www.globalplayer.com/catchup/radiox/uk/"

radioX_showInfo = gs.get_all_shows(radioX_url)

chris_id = gs.get_show_id(radioX_showInfo, 'The Chris Moyles Show')

chris_url = radioX_url+chris_id

show_list = gs.get_show_list(chris_url)

url_list = gs.list_of_urls(show_list)

gs.download_url_list(url_list, '/Users/elliottpalmer/Downloads/', 'Chris')