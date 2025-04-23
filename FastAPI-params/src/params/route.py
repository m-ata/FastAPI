from datetime import date, datetime , time , timedelta
from uuid import UUID
import fastapi

router = fastapi.APIRouter()

@router.get("/")
def home():
    return {
        "message":"Welcome"
    }
    
@router.post("/items/{item_id}")
def getItemsUUID(item_id : UUID):
    return {
        "message" : {item_id}
    }
    
# 2008-09-15 14:23:55.003
@router.post("/date/{dateTime}")
def getDateTime(dateTime: datetime):
    return {
        "message" : dateTime
    }

# 2008-09-15 
@router.post("/dateOnly/{date}")
def getDateOnly(date : date):
    return {
        "message" : date
    }
    
    
# 14:23:55.003
@router.post("/alarms/{alarm_time}")
def set_alarm(alarm_time: time):
    return {"alarm_set_for": alarm_time}


@router.post("/timeout/{duration}")
def timeout(duration: timedelta):
    return {"duration_in_seconds": duration.total_seconds(), 
            "duration_in_seconds": duration.resolution,
            "duration_in_seconds": duration.min,
            "duration_in_seconds": duration.max}