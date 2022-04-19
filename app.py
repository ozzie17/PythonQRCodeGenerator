
import pyqrcode
import pandas as pd


def createQRCode():

    df = pd.read_csv("airtravel.csv")

    for index, values in df.iterrows():

        month = values["Month"]
        yearOne = values["1958"]
        secondYear = values["1959"]
        thirdYear = values["1960"]

        data = f'''

        Month: {month} \n
        1958: {yearOne} \n
        1959: {secondYear} \n 
        1960: {thirdYear} \n 
        '''
        image = pyqrcode.create(data)
        image.svg(f"{month}.svg", scale="5")


createQRCode()
