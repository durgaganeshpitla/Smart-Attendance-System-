'''import yagmail
import os

receiver = "pitladurgaganesh333@gmail.com"  # receiver email address
body = "Attendence File"  
attendance_send = "Attendance"+os.sep+"Attendance_2020-08-29_17-05-04.csv" 

yag = yagmail.SMTP("pitladurgaganesh333@gmail.com", "jqdy seku qxje bykk")

yag.send(
    to=receiver,
    subject="Attendance Report", 
    contents=body, 
    attachments=filename, 
)
import yagmail
import os

receiver = "pitladurgaganesh333@gmail.com"
body = "Attendance File"

attendance_folder = "Attendance"
files = os.listdir(attendance_folder)
csv_files = [f for f in files if f.endswith('.csv')]

# This gets the newest CSV attendance file
latest_csv = max(csv_files, key=lambda f: os.path.getctime(os.path.join(attendance_folder, f)))
filename = os.path.join(attendance_folder, latest_csv)

yag = yagmail.SMTP("pitladurgaganesh333@gmail.com", "jqdy seku qxje bykk")

yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=filename,
)'''
import os
import yagmail

receiver = "pitladurgaganesh333@gmail.com"
body = "Attendance Files"

attendance_folder = "Attendance"
# Get all CSV files in the Attendance folder
files = os.listdir(attendance_folder)
csv_files = [os.path.join(attendance_folder, f) for f in files if f.endswith('Attendance_send.csv')]

yag = yagmail.SMTP("pitladurgaganesh333@gmail.com", "jqdy seku qxje bykk")

yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=csv_files,  # Attach all found CSV files
)
