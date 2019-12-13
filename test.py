import getShows as gs

station_showInfo, station_name = gs.get_show_information("https://www.globalplayer.com/catchup/radiox/uk/")

def listOfShows(station_information):
    shows = []
    for i in range(len(station_information)):
        shows.append((station_information[i]['title']))
     
    return shows


def funcname(parameter_list):
    pass

showList = listOfShows(station_showInfo)



show_id = gs.get_show_id(station_showInfo, showList[1])

print(station_showInfo[])