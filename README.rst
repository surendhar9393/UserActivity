To Install the requirement run the following command

go to project folder and type
   pip install -r requirement.txt

To start the server
   python manage.py runserver

For login use the below end point:
   http://13.59.165.181:8000/login/ (POST Method)

   request Json:
      {
          "email": "surendhar.raj2@gmail.com",
          "password": "S98765432"
        }

   Sample response:
      {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN1cmVuZGhhci5yYWoyQGdtYWlsLmNvbSIsImV4cCI6MTU5Mzg4NDAxNSwiZW1haWwiOiJzdXJlbmRoYXIucmFqMkBnbWFpbC5jb20ifQ.0YAo_RPyN42QvG9J8Bzzbseq3jWxcqGAGFoBoH76f-A"
            "user_name": "Egon Spengler"
      }

Use This token for getting User Activity (Token based DRF):

   http://13.59.165.181:8000/user/detail   (GET Method)

   Pass Token on Header (token"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN1cmVuZGhhci5yYWoyQGdtYWlsLmNvbSIsImV4cCI6MTU5Mzg4NDAxNSwiZW1haWwiOiJzdXJlbmRoYXIucmFqMkBnbWFpbC5jb20ifQ.0YAo_RPyN42QvG9J8Bzzbseq3jWxcqGAGFoBoH76f-A")

  Sample response:
    {
    "ok": true,
    "members": [
        {
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "Jul 04 2020 04:03AM",
                    "end_time": "Jul 04 2020 07:03AM"
                },
                {
                    "start_time": "Jul 03 2020 04:04AM",
                    "end_time": "Jul 03 2020 07:04AM"
                }
            ]
        },
        {
            "id": "W07QCRPA4",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "Jul 03 2020 13:27PM",
                    "end_time": "Jul 03 2020 17:27PM"
                },
                {
                    "start_time": "Jul 04 2020 14:28PM",
                    "end_time": "Jul 04 2020 17:28PM"
                }
            ]
        }
    ]
}


