from pymongo import MongoClient
import pandas as pd

from migrate.models import SectorsClass, GeoClass

client = MongoClient(host='15.206.53.223',
                     port=27072, 
                     username='travis', 
                     password='you_talking_to_me!?',
                    authSource="admin")
db = client['travis_test']

sectors_df = pd.DataFrame(list(db.sectors.find()))
sectors_df = sectors_df.fillna('')
geo_df = pd.DataFrame(list(db.geo.find()))
geo_df = geo_df.fillna('')

for row in range(len(sectors_df)):
    values = sectors_df.iloc[row]
    sector = SectorsClass()
    sector.sectorName = values['sectorName']
    sector.sector_id = str(values['_id'])
    sector.subsectors = str(values['subSectors'])
    sector.save()

for row in range(len(geo_df)):
    values = geo_df.iloc[row]
    geo = GeoClass()
    geo.countryName = str(values['countryName'])
    geo.cities = str(values['cities'])
    geo.countryCode = str(values['countryCode'])
    geo.geo_id = str(values['_id'])
    geo.countryCurrency = str(values['countryCurrency'])
    geo.save()