'''
Created on Oct 13, 2018

@author: brandon guo
'''
from datetime import datetime
from datetime import timedelta
from ocr  import detect_handwritten_ocr_uri

def createReminder(service, uri):
    now = datetime.now()# 'Z' indicates UTC time
    print(now)
    x = detect_handwritten_ocr_uri(uri)
    y = int(x[1])/int(x[0])
    print("days")
    print(y)
    td = timedelta(days=y)
    mydate = now + td
    print(mydate)
    Mydate = mydate.isoformat()
    td1 = timedelta(hours=1)
    mydate1 = mydate + td1
    Mydate1 = mydate1.isoformat()
    event = {
      'summary': 'Calvin is dumbester',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': Mydate,
        'timeZone': 'America/New_York',
      },
      'end': {
        'dateTime': Mydate1,
        'timeZone': 'America/New_York',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print("finished")

