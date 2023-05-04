import requests
import csv
from io import StringIO


class Info(object):
    def __init__(self,restid,name,address,phone,mobile,latitude,longitude,city):
        super().__init__()
        self.restid = restid
        self.name = name
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.latitude = latitude
        self.longitude = longitude
        self.city = city

class GreenRestaurant(object):
    @classmethod
    def greenRestaurantInfo(cls) -> list:
        response=requests.get(f'https://data.epa.gov.tw/api/v2/gis_p_11?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=CSV')
        if response.ok:
            file = StringIO(response.text,newline="")
            csvReader = csv.reader(file)
            next(csvReader)
            datalist = []
            for item in csvReader:
                infolist = Info(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
                datalist.append(infolist)
            return datalist
            
        else:
            raise Exception("下載失敗")