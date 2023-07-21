import datetime
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from . import emailing as em

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "recognizer/credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("attendance").sheet1

#max_intime = '23:59:00'


def enroll_person_to_sheet(name, email, roll_no):
    nrows = len(sheet.col_values(1))
    sheet.update_cell(nrows+1, 1, name)
    sheet.update_cell(nrows+1, 2, email)
    sheet.update_cell(nrows+1, 3, roll_no)
    em.email_rollno(email, roll_no)


def mark_all_absent():
    now = datetime.datetime.now()
    date = now.strftime('%m/%d/%Y').replace('/0', '/')
    if (date[0] == '0'):
        date = date[1:]
    datecell = sheet.find(date)
    nrows = len(sheet.col_values(1))
    for row in range(2, nrows+1):
        sheet.update_cell(row, datecell.col, 'absent')


def write_to_sheet(name):
    now = datetime.datetime.now()
    date = now.strftime('%m/%d/%Y').replace('/0', '/')
    if (date[0] == '0'):
        date = date[1:]
    time = now.strftime('%H:%M:%S')
    namecell = sheet.find(name)
    datecell = sheet.find(date)

    if (sheet.cell(namecell.row, datecell.col).value == None):
        #if (time < max_intime):
        sheet.update_cell(namecell.row, datecell.col, 'present')
        print('recorded')
        em.send_email(sheet.cell(namecell.row, 2).value, "present")

        #else:
            # sheet.update_cell(namecell.row,datecell.col,'late')
            #print('late')
            #em.send_email(sheet.cell(namecell.row, 2).value, "absent")
    elif (sheet.cell(namecell.row, datecell.col).value == 'present') or (sheet.cell(namecell.row, datecell.col).value == 'absent'):
        print(' attendance already recorded')