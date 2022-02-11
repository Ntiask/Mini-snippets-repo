import pandas as pd
import re
import numpy as np
from google.cloud import storage
import os
from flask import escape
from flask import send_file
import functions_framework
from cmath import e
from werkzeug.utils import secure_filename
import glob
import xlsxwriter
import tempfile
import zipfile
import sys
import linecache

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

def parse_multipart(request):

    try:
        allzips = []
        files = request.files.to_dict()
        text = request.args.to_dict()
        text2 = request.form['Date']

        filepath=tempfile.gettempdir()
        
        for file_name, file in files.items():
            file.save(os.path.join(filepath, file_name))
            print('Processed file: %s' % file_name)
        
        allzips = os.listdir(filepath)
        print(allzips)

        with zipfile.ZipFile(filepath+"/"+allzips[0]) as x:
                    with x.open("pvu_sub_capacity.csv") as f:
                        try:
                            subcapd = pd.read_csv(f)
                        except:
                            subcapd = pd.read_csv(f, encoding='latin-1')

        licentd = pd.read_excel(filepath+"/"+allzips[1])

        search = []

        for values in subcapd['Imported Part Numbers']:
            try:
                search.append(re.search(r'E0.....', values).group())
            except:
                pass

        subcapd['PartE'] = pd.Series(search)

        newdf=subcapd.merge(licentd, left_on='PartE', right_on='Part Number', how='left')

        newdf['Licenses Oqned'] = newdf['Qty Purchased']
        newdf['License Delta'] = newdf['Licenses Oqned'] - newdf['Metric Quantity']
        newdf['Month'] = text2
        newdf2 = newdf[["Month", "Publisher", "Imported Part Numbers", 
        "Product Name", "License Delta","Licenses Oqned", "Metric Quantity", 
        "Metric Peak Value Time", "Recalculation Needed", "Server Name", "Processor", 
        "Processor Brand String", "PVU Per Core", "Changed PVU Per Core", 
        "Physical Server CPU Core Subcapacity Limit", "Physical Server CPU Core Subcapacity", 
        "Physical Server PVU Subcapacity Limit", "Physical Server PVU Subcapacity", "Comment", 
        "Partition Cores", "Virtualization Layer ID", "Computer", "Computer Deleted", "OS", 
        "IP Address", "Product Release","Component", "Path", "Unconfirmed Product Instance", 
        "Computer Last Seen","Exclusion Comment"
        ]]

        consumptionurl = filepath+"/consumption.csv"
        newdf2.to_csv(consumptionurl, index=False)
        return send_file(consumptionurl)

    except Exception as error:
        return r"""
                <!DOCTYPE html>
                <head>
                <title>Returning Error</title>
                </head>
                <body>
                <h1>There seems to be a problem :(</h1>
                <br/>
                <br/>
                Please check your data.
                <br/>
                Following Error Occurred:{}
                <br/>
                </body>
                """.format(PrintException())
    finally:
        for i in allzips:
            os.remove(filepath+"/"+i)

