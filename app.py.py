
from pyjstat import pyjstat
import requests
from flask import render_template
from flask import Flask
import pandas as pd


app = Flask(__name__)
@app.route("/")

def get_table():

    POST_URL = 'https://data.ssb.no/api/v0/no/table/09588/'
    #API query
    payload = {
    "query": [
        {
        "code": "Region",
        "selection": {
            "filter": "vs:Kommune",
            "values": [
            "3007",
            "3038",
            "3047",
            "3053"
            ]
        }
        },
        {
        "code": "ContentsCode",
        "selection": {
            "filter": "item",
            "values": [
            "Netto"
            ]
        }
        },
        {
        "code": "Tid",
        "selection": {
            "filter": "item",
            "values": [
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021"
            ]
        }
        }
    ],
    "response": {
        "format": "json-stat2"
    }
    }
    response = requests.post(POST_URL,json=payload)
   
    ds1 = pyjstat.Dataset.read(response.text)
    df1 = ds1.write('dataframe')
    
    year=list(df1['år'])
    
    val_ringerike=list(df1.loc[0:17,'value'])
    val_hole=list(df1.loc[18:34,'value'])
    val_modum=list(df1.loc[35:53,'value'])
    val_jevnaker=list(df1.loc[54:72,'value'])

    return render_template ("htmlfinal.html",year=year,val_ringerike=val_ringerike,val_hole=val_hole,val_modum=val_modum,val_jevnaker=val_jevnaker )



if __name__ == '__main__':
    app.run()
    


          