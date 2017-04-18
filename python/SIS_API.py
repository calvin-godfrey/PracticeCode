import bs4, mechanize, sys, argparse, getpass, os.path

url = "https://sisstudent.fcps.edu"
br = mechanize.Browser()
parser = argparse.ArgumentParser(description="Will display user's grade book information from SIS")
parser.add_argument('-g', '--grade', help="Table without the grades column", action="store_true")
parser.add_argument('-p', '--period', help="Table without the periods column", action="store_true")
parser.add_argument('-c', '--course', help="Table without the courses column", action="store_true")
parser.add_argument('-t', '--teacher', help="Table without the teachers column", action="store_true")
parser.add_argument('-r', '--room', help="Table without the room number column", action="store_true")

def display_info(p, p_show, c, c_show, r, r_show, t, t_show, g, g_show):
    BUFFER_SIZE = 18
    print "Period".ljust(BUFFER_SIZE)*int(p_show)+ "|Course".ljust(BUFFER_SIZE)*int(c_show) + "|Room".ljust(BUFFER_SIZE-9)*int(r_show) + "|Teacher".ljust(BUFFER_SIZE)*int(t_show) + "|Grade"*int(g_show)
    print "-"*75
    for i in range(len(p)): #They should all be the same length
        print (p[i].ljust(BUFFER_SIZE))*int(p_show) + ("|"+ c[i].ljust(BUFFER_SIZE))*int(c_show) + ("|" + r[i].ljust(BUFFER_SIZE-9))*int(r_show) + ("|" + t[i].ljust(BUFFER_SIZE))*int(t_show) + ("|" + g[i].ljust(BUFFER_SIZE))*int(g_show)

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

def main(disp_p, disp_c, disp_r, disp_t, disp_g):
    if os.path.isfile("SIS_DATA.txt"): #Cause I don't want to type in my password every time
        login_info = open("SIS_DATA.txt", "r").readlines()
        username = login_info[0].strip()
        password = login_info[1].strip()
    else:
        username = raw_input("Type in your username:\n> ")
        print "Now enter your password: "
        password = getpass.getpass()
    period, courses, room_numbers, teachers, grade = [], [], [], [], []
    br.open(url)
    br.select_form(name="Form1")
    br.form["username"] = username #Gotten from file saved locally
    br.form["password"] = password
    req = br.submit()
    try:
        grade_book = br.follow_link(text_regex=r"Grade Book") #This is the text for the link to the grades
    except:
        raise ValueError("Username/Password Combo Unsuccessful")
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
    display_info(period, disp_p, courses, disp_c, room_numbers, disp_r, teachers, disp_t, grade, disp_g)
    save_grades(grade)

if __name__ == "__main__":
    args = parser.parse_args()
    r = (args.room)
    g = (args.grade)
    p = (args.period)
    c = (args.course)
    t = (args.teacher)
    main(p, c, r, t, g)
