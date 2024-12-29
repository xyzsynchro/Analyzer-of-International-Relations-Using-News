import tkinter
from tkinter import *
from tkinter import messagebox
#from descartes import PolygonPatch
import matplotlib.pyplot as plt
import geopandas
import numpy as np
import pandas as pd

window = Tk()
window.title("Relationships and News")

header = Label(window, text="ANALYSIS OF RELATIONS BETWEEN COUNTRIES BY NEWS ARTICLES")
header.grid(column=0, row=0)


selectCountry = Label(window, text="Select the country to get relations result.")
selectCountry.grid(column=0, row=2)

countrySelection = StringVar()
radCA = Radiobutton(window, text='Canada', value='CA', variable=countrySelection)
radCA.grid(column=0, row=3)
radCN = Radiobutton(window, text='China', value='CN', variable=countrySelection)
radCN.grid(column=0, row=4)
radDE = Radiobutton(window, text='Germany', value='DE', variable=countrySelection)
radDE.grid(column=0, row=5)
radFR = Radiobutton(window, text='France', value='FR', variable=countrySelection)
radFR.grid(column=0, row=6)
radIR = Radiobutton(window, text='Iran', value='IR', variable=countrySelection)
radIR.grid(column=0, row=7)
radIT = Radiobutton(window, text='Italy', value='IT', variable=countrySelection)
radIT.grid(column=0, row=8)
radJP = Radiobutton(window, text='Japan', value='JP', variable=countrySelection)
radJP.grid(column=0, row=9)
radRU = Radiobutton(window, text='Russia', value='RU', variable=countrySelection)
radRU.grid(column=0, row=10)
radUK = Radiobutton(window, text='United Kingdom', value='UK', variable=countrySelection)
radUK.grid(column=0, row=11)
radUS = Radiobutton(window, text='United States', value='US', variable=countrySelection)
radUS.grid(column=0, row=12)

selectTimeRange = Label(window, text="Select the time range.")
selectTimeRange.grid(column=0, row=13)

timeSelection = IntVar()
rad6Mo = Radiobutton(window, text="Last 6 Months.", value=1, variable=timeSelection)
rad6Mo.grid(column=0, row=14)
radAllTime = Radiobutton(window, text="All the data.", value=2, variable=timeSelection)
radAllTime.grid(column=0, row=15)

selectFromOrTo = Label(window, text="Select the situation")
selectFromOrTo.grid(column=0, row=16)

fromOrToSelection = IntVar()
radFrom = Radiobutton(window, text="Selected country's vision for others", value=1, variable=fromOrToSelection)
radFrom.grid(column=0, row=17)
radTo = Radiobutton(window, text="Other countries' vision for selected country", value=2, variable=fromOrToSelection)
radTo.grid(column=0, row=18)


def getData():
    legendString = ""
    US = 4
    RU = 18
    FR = 43
    IR = 107
    DE = 121
    CN = 139
    IT = 141
    UK = 143
    JP = 155
    CA = 3
    timeVal = timeSelection.get()
    countryVal = countrySelection.get()
    fromVal = fromOrToSelection.get()
    if timeVal == 0 or countryVal == "" or fromVal == 0:
        messagebox.showinfo('Oh No.', 'At least one of the required value is missing.')
        return
    if fromVal == 1:
        legendString = legendString + "'s vision of other countries."
    else:
        legendString = legendString + " as other countries' vision."

    world_filepath = geopandas.datasets.get_path('naturalearth_lowres')
    world = geopandas.read_file(world_filepath)
    world['relationships'] = np.nan

    if countryVal == 'CA':
        countryName = "Canada"
        legendString = "Canada" + legendString
        selectedIndex = 0
    elif countryVal == 'CN':
        countryName = "China"
        legendString = "China" + legendString
        selectedIndex = 1
    elif countryVal == 'DE':
        countryName = "Germany"
        legendString = "Germany" + legendString
        selectedIndex = 2
    elif countryVal == 'FR':
        countryName = "France"
        legendString = "France" + legendString
        selectedIndex = 3
    elif countryVal == 'IR':
        countryName = "Iran"
        legendString = "Iran" + legendString
        selectedIndex = 4
    elif countryVal == 'IT':
        countryName = "Italy"
        legendString = "Italy" + legendString
        selectedIndex = 5
    elif countryVal == 'JP':
        countryName = "Japan"
        legendString = "Japan" + legendString
        selectedIndex = 6
    elif countryVal == 'RU':
        countryName = "Russia"
        legendString = "Russia" + legendString
        selectedIndex = 7
    elif countryVal == 'UK':
        countryName = "United Kingdom"
        legendString = "United Kingdom" + legendString
        selectedIndex = 8
    elif countryVal == 'US':
        countryName = "United States of America"
        legendString = "United States" + legendString
        selectedIndex = 9

    if timeVal == 2:
        df = pd.read_excel('averagescores_final_tokenized_subjectcorrected.xlsx')
    elif timeVal == 1:
        df = pd.read_excel('averagescores_last6_tokenized_subjectcorrected.xlsx')
    avg_sc_all = df.iloc[:, 1:].to_numpy()

    if fromVal == 1:
        world.loc[US:US, 'relationships'] = avg_sc_all[selectedIndex][9]
        world.loc[CN:CN, 'relationships'] = avg_sc_all[selectedIndex][1]
        world.loc[CA:CA, 'relationships'] = avg_sc_all[selectedIndex][0]
        world.loc[JP:JP, 'relationships'] = avg_sc_all[selectedIndex][6]
        world.loc[UK:UK, 'relationships'] = avg_sc_all[selectedIndex][8]
        world.loc[DE:DE, 'relationships'] = avg_sc_all[selectedIndex][2]
        world.loc[FR:FR, 'relationships'] = avg_sc_all[selectedIndex][3]
        world.loc[IT:IT, 'relationships'] = avg_sc_all[selectedIndex][5]
        world.loc[IR:IR, 'relationships'] = avg_sc_all[selectedIndex][4]
        world.loc[RU:RU, 'relationships'] = avg_sc_all[selectedIndex][7]
    else:
        world.loc[US:US, 'relationships'] = avg_sc_all[9][selectedIndex]
        world.loc[CN:CN, 'relationships'] = avg_sc_all[1][selectedIndex]
        world.loc[CA:CA, 'relationships'] = avg_sc_all[0][selectedIndex]
        world.loc[JP:JP, 'relationships'] = avg_sc_all[6][selectedIndex]
        world.loc[UK:UK, 'relationships'] = avg_sc_all[8][selectedIndex]
        world.loc[DE:DE, 'relationships'] = avg_sc_all[2][selectedIndex]
        world.loc[FR:FR, 'relationships'] = avg_sc_all[3][selectedIndex]
        world.loc[IT:IT, 'relationships'] = avg_sc_all[5][selectedIndex]
        world.loc[IR:IR, 'relationships'] = avg_sc_all[4][selectedIndex]
        world.loc[RU:RU, 'relationships'] = avg_sc_all[7][selectedIndex]

    axes = world.plot(column='relationships', legend=True,
               missing_kwds={'color': 'darkgrey', 'label' : 'No Data'},
               legend_kwds={'label': legendString, 'orientation': "horizontal"})
    nami = world[world.name == countryName]
    namigm = nami.__geo_interface__['features']  # geopandas's geo_interface
    namig0 = {'type': namigm[0]['geometry']['type'],
              'coordinates': namigm[0]['geometry']['coordinates']}
    #axes.add_patch(PolygonPatch(namig0, fc='red'))
    plt.show()


showRelationsButton = Button(window, text="Show Relations", command=getData)
showRelationsButton.grid(column=0, row=19)

window.geometry('500x500')
window.mainloop()

