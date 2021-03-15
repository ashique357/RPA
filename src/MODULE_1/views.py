from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
import os
import time
import datetime

@api_view()
def file_manipulation(request):
    dir_path = os.path.join(settings.FILES_DIR)
    file_list=os.scandir(dir_path)
    
    count=len(os.listdir(dir_path))
    today=datetime.datetime.now()

    for single_file in file_list:
        get_time=time.ctime(os.path.getmtime(single_file))
        converted_time=datetime.datetime.strptime(get_time, "%c")
        file_name=single_file.name
        dif=abs(today-converted_time) > datetime.timedelta(minutes=200)
        if(dif):
            try:
                os.remove(dir_path+'/'+file_name)
                return Response (
                {
                    "Total Files" : "count",
                    "Info" : "get_time",
                    "file-name": "file_name",
                    "today" : "today",
                    "dif" : "dif",
                    "Deleted":"YES"
                }
                )
                
            except:
                return Response('Access Denied')
                    
        else:
            return Response (
                {
                    "Total Files" : "count",
                    "Info" : "get_time",
                    "file-name": "file_name",
                    "today" : "today",
                    "dif" : "dif",
                    "Deleted": "NO"
                }
                )
            