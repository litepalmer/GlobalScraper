import getShows as gs

shows = gs.get_all_shows("https://www.globalplayer.com/catchup/radiox/uk/")
chris_id = gs.get_show_id(shows, "The Chris Moyles Show")
chris_url = "https://www.globalplayer.com/catchup/radiox/uk/"+chris_id
show_list = gs.get_show_list(chris_url)
dates = gs.get_showDates(show_list)
downloadURLS = gs.list_of_urls(show_list)


import requests
for n in downloadURLS:
    myfile=requests.get(n)
    for i in range(len(dates)):
        date = dates[i]
        open("/Users/elliottpalmer/Downloads/"+"toby"+date+'.m4a','wb').write(myfile.content)
        print('file downloaded')


