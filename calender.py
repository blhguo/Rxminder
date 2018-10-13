from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from ocr  import detect_handwritten_ocr_uri
from ParseLabel  import createReminder

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.events'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #print(now)

    createReminder(service, "gs://rxminder_bucket1/prescrptions-label.png")
    
    #event = service.events().insert(calendarId='primary', body=event).execute()
    #print('Event created: %s' % (event.get('htmlLink')))

    #detect_handwritten_ocr_uri("gs://rxminder_bucket1/prescrptions-label.png")

if __name__ == '__main__':
    main()