import bs4, mechanize
url = "https://sisstudent.fcps.edu"
br = mechanize.Browser()
login_info = open("SIS_DATA.txt", "r") #So that y'all don't know my information
login_info = login_info.readlines()
username = login_info[0].strip() #cuts of unnecessary stuff
password = login_info[1].strip()

def display_info(p, c, r, t, g):
    BUFFER_SIZE = 18
    print "Period".ljust(BUFFER_SIZE)+ "|" + "Course".ljust(BUFFER_SIZE) + "|" + "Room".ljust(BUFFER_SIZE-9) + "|" + "Teacher".ljust(BUFFER_SIZE) + "|Grade" #Room is shorter because it doesn't need all those
    print "-"*75                                                                                                                                             #Characters and I needed to save space
    for i in range(len(p)): #They should all be the same length
        print p[i].ljust(BUFFER_SIZE) + "|" + c[i].ljust(BUFFER_SIZE) + "|" + r[i].ljust(BUFFER_SIZE-9) + "|" + t[i].ljust(BUFFER_SIZE) + "|" + g[i].ljust(BUFFER_SIZE)

def save_grades(grades): #To see if any are updated later on
    open("grades.txt", "w").close() #Make sure the file is empty
    for index, grade in enumerate(grades):
        if grade[0] == "*":
            grades[index] = grades[index][1:]
    target = open("grades.txt", "w")
    for grade in grades:
        target.write(grade + "\n")

def load_grades():
    return open("grades.txt", "r").readlines()

def main():
    period, courses, room_numbers, teachers, grade = [], [], [], [], []
    br.open(url)
    br.select_form(name="Form1")
    br.form["username"] = username #Gotten from file saved locally
    br.form["password"] = password
    req = br.submit()
    grade_book = br.follow_link(text_regex=r"Grade Book") #This is the text for the link to the grades
    parsed = bs4.BeautifulSoup(grade_book.read(), 'lxml')
    rows = parsed.select("table.info_tbl")[0].find_all("tr") #List of all the rows that contain information
    ignore = False
    try:
        old_grades = [i.strip() for i in load_grades()]
    except: #Didn't find any grades
        ignore = True
    for row_num, row in enumerate(rows[1:]): #First row is just the table headers, unneeded info
        for index, td in enumerate(row.find_all("td")):
            if index in [2, 6, 7]:
                continue
            if index==0:
                period.append(td.text)
            if index==1:
                courses.append(' '.join(td.text.split()[:-1]))
            if index==3:
                room_numbers.append(td.text)
            if index==4:
                teachers.append(td.text)
            if index==5:
                if ignore:
                    grade.append(td.text)
                else:
                    if old_grades[row_num] != td.text:
                        grade.append("*"+td.text)
                    else:
                        grade.append(td.text)
    display_info(period, courses, room_numbers, teachers, grade)
    save_grades(grade)

if __name__ == "__main__":
    main()
