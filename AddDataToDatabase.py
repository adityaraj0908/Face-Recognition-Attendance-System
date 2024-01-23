import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

ref = db.reference('Student')

data = {
    "1DS22CS016":
        {
            "Name": "Aditya Raj",
            "Branch": "CS",
            "Joining": 2022,
            "Total Attendance": 0,
            "Semester": 2,
            "Standing": "G",
            "Last Attendance Time": "2023-10-11 17:25:12"

        },
    "1DS22CS000":
        {
            "Name": "Elon Musk",
            "Branch": "CS",
            "Joining": 1985,
            "Total Attendance": 0,
            "Semester": "N/A",
            "Standing": "G",
            "Last Attendance Time": "2023-08-24 13:46:21"

        },
    "1DS22CD045":
        {
            "Name": "Shivam Poddar",
            "Branch": "DataScience",
            "Joining": 2022,
            "Total Attendance": 0,
            "Semester": 2,
            "Standing": "G",
            "Last Attendance Time": "2023-08-24 04:29:16"

        },
    "1DS22CS131":
        {
            "Name": "Mritunjay Singh",
            "Branch": "CS",
            "Joining": 2022,
            "Total Attendance": 0,
            "Semester": 2,
            "Standing": "G",
            "Last Attendance Time": "2023-08-24 04:29:16"

        },
    "DSCE-Teacher":
        {
            "Name": "Prof. Sunanda",
            "Branch": "CS",
            "Joining": 2022,
            "Total Attendance": 0,
            "Semester": "N/A",
            "Standing": "G",
            "Last Attendance Time": "2023-08-24 04:29:16"

        },
    "1DS22CS102":
        {
            "Name": "Karthikeya T",
            "Branch": "CS",
            "Joining": 2022,
            "Total Attendance": 0,
            "Semester": 2,
            "Standing": "G",
            "Last Attendance Time": "2023-08-24 04:29:16"
        }

    #     },
    # "1DS22CS142":
    #     {
    #         "Name": "Nitish Y N",
    #         "Branch": "CS",
    #         "Joining": 2022,
    #         "Total Attendance": 0,
    #         "Semester": 2,
    #         "Standing": "G",
    #         "Last Attendance Time": "2023-08-24 04:29:16"
    #
    #     }

}

for key, value in data.items():
    ref.child(key).set(value)
