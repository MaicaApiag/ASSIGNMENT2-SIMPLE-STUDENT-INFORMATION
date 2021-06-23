<<<<<<< HEAD
"""
CSC151N ASSIGNMENT2: SIMPLE STUDENT INFORMATION SYSTEM
         MAICA A. APIAG    BS-STATISTICS 
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import os
import sqlite3

root = Tk()
root.geometry("1360x720")
root.title('SSIS - Maica A. Apiag')
root.resizable(False, False)
positionRight = int((root.winfo_screenwidth()/2 - 688))
positionDown = int((root.winfo_screenheight()/2 - 386))
root.geometry("+{}+{}".format(positionRight, positionDown))

StdID = StringVar()
Name = StringVar()
Gender = StringVar()
Course = StringVar()
YearLevel = StringVar()

mainFrame = LabelFrame(root, bg="#eaebeb", highlightbackground="#104c70",highlightthickness=4)
mainFrame.place(x=468,y=100,height=575,width=885)

mainFrame2 = LabelFrame(root, bg="#104c70")
mainFrame2.place(x=8,y=100,height=575,width=450)

Label(root, text="STUDENT INFORMATION SYSTEM", font = ('Palatino Linotype', 50, 'bold'),fg="#dcdcdc", width=32).grid(row=0,column=0)    
Label(mainFrame, text="STUDENTS", font = ('Palatino Linotype', 30, 'bold'),fg="#104c70",bg="#eaebeb", width=34).grid(row=0,column=0, columnspan=6)
Label(mainFrame2, text="COURSES", font = ('Palatino Linotype', 30, 'bold'),fg="white",bg="#104c70", width=10).grid(row=0,column=0, columnspan=5)

mydb = sqlite3.connect('SSIS.db')
mycursor = mydb.cursor()

mydb.execute("PRAGMA foreign_keys = ON;"); 

mycursor.execute("""CREATE TABLE IF NOT EXISTS COURSE_INFO(
        course_number integer PRIMARY KEY,
        course_code text varchar(10),
        course_name text
        )""")


mycursor.execute("""CREATE TABLE IF NOT EXISTS STUD_INFO_SYS(
        ID_number text PRIMARY KEY,
        name text,
        course_number integer,
        year_level text,
        gender text,
        FOREIGN KEY (course_number)
            REFERENCES COURSE_INFO(course_number)
                ON DELETE CASCADE
        )""")

mydb.commit()

def makeList():
    global listStudents
    mycursor.execute("SELECT * FROM STUD_INFO_SYS")
    listStudents = mycursor.fetchall()
    global listCourse
    mycursor.execute("SELECT * FROM COURSE_INFO")
    listCourse = mycursor.fetchall()

def clicked(*args):
    this = treeSec.selection()

    if len(this) != 0 or there == True:
        def add():
            top=Toplevel()
            top.title('ADD STUDENTS')
            top.geometry("540x363")
            top.resizable(0,0)
            top.geometry("+{}+{}".format(positionRight+400, positionDown+190))
            
            MainFrame = Frame(top, bg="#eaebeb")
            MainFrame.grid()
            
            DataFrame = Frame(MainFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
            DataFrame.pack(side=BOTTOM)
            
            StudInf=LabelFrame(DataFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
            StudInf.pack(side=LEFT)
            
            StdID.set("")
            Name.set("")
            Course.set("")
            
            SILabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
            SILabel.grid(row=0, column=0, sticky=W)
            ID = Entry(StudInf, font=('Palatino Linotype',13),textvariable=StdID, width=39)
            ID.grid(row=0, column=1, pady=8)
            
            FLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Name", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            FLabel.grid(row=1, column=0, sticky=W)
            name = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Name, width=39)
            name.grid(row=1, column=1, pady=8)
            
            CLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            CLabel.grid(row=2, column=0, sticky=W)
            course = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Course, width=39)
            course.grid(row=2, column=1, pady=8)
            
            YLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            YLabel.grid(row=3, column=0, sticky=W)
            ylevel = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
            ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year','5th Year')
            ylevel.current(0)
            ylevel.grid(row=3, column=1, pady=8)

            GLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            GLabel.grid(row=4, column=0, sticky=W)
            gender = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
            gender['values']=('','Female','Male')
            gender.current(0)
            gender.grid(row=4, column=1, pady=8)
            
            def addData():
                if  ID.get() == "" or name.get() == "" or gender.get() == "" or course.get() == "" or ylevel.get()== "":
                    messagebox.showinfo("Student Information System","Please Fill In the Box")
                else:
                    for student in listStudents:                        
                            if student[0] == ID.get() or student[1] == name.get():
                                messagebox.showinfo("Student Information System","ID Number Already Exists")
                                return
                    x = StdID.get()
                    id_list = []
                    for i in x:
                        id_list.append(i)
                    if "-" in id_list:
                        y = x.split("-")
                        year = y[0]
                        number = y[1]
                        cournum=""
                        if year.isdigit() == False or number.isdigit() == False:
                            messagebox.showerror("SSIS","Invalid ID")
                        else:
                            for cour in listCourse:
                                if cour[2] == course.get():
                                    if cour[2] == course.get():
                                        cournum = cour[0]
                                    else:
                                        messagebox.showinfo("Student Information System","Course Not Found")
                            mycursor.execute("INSERT INTO STUD_INFO_SYS(ID_number,name,course_number,year_level,gender)VALUES(?,?,?,?,?)",
                                             (ID.get(),name.get(),cournum,ylevel.get(),gender.get()))
                            messagebox.showinfo("Student Information System","Student Recorded Successfully")
                            top.destroy()
                            mydb.commit()
                            viewList()
                            viewCourseList()
                        
                    else:
                        messagebox.showerror("SSIS","Invalid ID")
                    
            submit=Button(StudInf, text="SUBMIT",command=addData, font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
            submit.grid(row=5, column=0, columnspan=3,pady=8)
            
        def viewList():
            makeList()
            for i in tree.get_children():
                tree.delete(i)
            
            counter = 0
            mycursor.execute("SELECT * FROM STUD_INFO_SYS")
            listStudents = mycursor.fetchall()
            for student in listStudents:
                if listStudents != []:
                    for cour in listCourse:
                        if cour[0] == student[2]:
                            courname = cour[2]
                    
                    if there == True or len(this) == 0:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                    
                    elif courname == treeSec.item(treeSec.focus(),"values")[1]:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                counter += 1   
                    
        def search():
            for i in tree.get_children():
                tree.delete(i)
            search = searchbar.get()
            counter = 0
            for student in listStudents:
                if student[0].startswith(search):
                    for cour in listCourse:
                        if cour[0] == student[2]:
                            courname = cour[2]
                    if len(this) == 0:
                        tree.insert(parent='',  index='end', iid=counter,
                                    values=(student[0],student[1],courname,student[3],student[4]))
                    elif courname == treeSec.item(treeSec.focus(),"values")[1]:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                counter += 1
                
        def delete():
            messageDeleteStud = messagebox.askyesno("SSIS", "Do you want to permanently delete this record?")
            if messageDeleteStud > 0:
                selected = tree.selection()[0]
                uid = tree.item(selected)['values'][0]
                mycursor.execute("DELETE FROM STUD_INFO_SYS WHERE ID_number=?",(uid,))
                mydb.commit()
                tree.delete(selected)
                viewList()
                viewCourseList()
            
        def update(index):
            def thisUpdate(studentInfo):
                select = tree.selection()
                for selected in select:
                    
                    mycursor.execute("UPDATE STUD_INFO_SYS SET ID_number=?,name=?,course_number=?,year_level=?,gender=?\
                                     WHERE ID_number=?", (ID.get(),name.get(),course.get(),ylevel.get(),gender.get(),\
                                        tree.set(selected,'#1')))
                    mydb.commit()
                    messagebox.showinfo("Student Information System","Student updated successfully")
                    viewList()
                    viewCourseList()
                
            infoItem = tree.focus()
            values = tree.item(infoItem,"values")
            
            topUpS=Toplevel()
            topUpS.title('UPDATE STUDENTS')
            topUpS.geometry("540x363")
            topUpS.resizable(0,0)
            topUpS.geometry("+{}+{}".format(positionRight+400, positionDown+190))
            
            studentInfo = tree.item(index)['values']
            
            MainFrame2 = Frame(topUpS, bg="#eaebeb")
            MainFrame2.grid()
                    
            DataFrame2 = Frame(MainFrame2,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
            DataFrame2.pack(side=BOTTOM)
                    
            DataAdd2=LabelFrame(DataFrame2, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
            DataAdd2.pack(side=LEFT)
                    
            SILable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
            SILable.grid(row=0, column=0, sticky=W)
            ID = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=StdID, width=39)
            ID.grid(row=0, column=1, pady=8)
                    
            FLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Name  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            FLable.grid(row=1, column=0, sticky=W)
            name = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Name, width=39)
            name.grid(row=1, column=1, pady=8)
                    
            CLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            CLable.grid(row=2, column=0, sticky=W)
            course = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Course, width=39)
            course.grid(row=2, column=1, pady=8)
                    
            YLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            YLable.grid(row=3, column=0, sticky=W)
            ylevel = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
            ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year')
            ylevel.current(0)
            ylevel.grid(row=3, column=1, pady=8) 

            GLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            GLable.grid(row=4, column=0, sticky=W)
            gender = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
            gender['values']=('','Female','Male')
            gender.current(0)
            gender.grid(row=4, column=1, pady=8)

            submit=Button(DataAdd2, text="UPDATE", command=lambda:thisUpdate(studentInfo), font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
            submit.grid(row=5, column=0, columnspan=3,pady=8)

            StdID.set(values[0])
            ID.config(state=DISABLED)
            Name.set(values[1])
            Course.set(values[2])
            if studentInfo[3] == "1st Year":
                ylevel.current(1)
            elif studentInfo[3] == "2nd Year":
                ylevel.current(2)
            elif studentInfo[3] == "3rd Year":
                ylevel.current(3)
            elif studentInfo[3] == "4th Year":
                ylevel.current(4)
            if studentInfo[4] == "Female":
                gender.current(1)
            elif studentInfo[4] == "Male":
                gender.current(2)
                
        def viewAll():
            for item in treeSec.selection():
                treeSec.selection_remove(item)
            global there
            there=True
            viewList()
            there=False
            
        searchbar = Entry(mainFrame,font=('Palatino Linotype',12), width=30)
        searchbar.grid(row=1, column=0, padx=6, pady=5)
        searchbutton = Button(mainFrame, text="SEARCH",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=search)
        searchbutton.grid(row=1, column=1, padx=6, pady=5)
            
        viewButton = Button(mainFrame, text="VIEW ALL", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=13, command=viewAll)
        viewButton.grid(row=1, column=2, padx=6, pady=5)

        addButton = Button(mainFrame, text="ADD STUDENTS", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=16, command=add)
        addButton.grid(row=1, column=3, padx=6, pady=5)
            
        edit = Button(mainFrame, text="EDIT",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=lambda:update(int(tree.focus())))
        edit.grid(row=1, column=4, padx=6, pady=5)
            
        delete = Button(mainFrame, text="DELETE",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=delete)
        delete.grid(row=1, column=5, padx=6, pady=5)

        tree = ttk.Treeview(mainFrame, height=20)
        tree.grid(row=2, column=0, columnspan=7, padx=12, pady=10)
            
        s = ttk.Style(root)
        s.configure("Treeview.Heading", font=('Palatino Linotype',11,'bold'))
        s.configure(".", font=('Palatino Linotype',12))
                
        tree['columns'] = ("ID number", "Name","Course","Year Level","Gender")

        tree.column('#0',width=0, stretch=NO)
        tree.column("ID number", anchor=CENTER, width=125)
        tree.column("Name", anchor=W, width=250)
        tree.column("Course", anchor=W, width=250)
        tree.column("Year Level", anchor=W, width=130)
        tree.column("Gender", anchor=W, width=100)

        tree.heading("ID number", text="ID number", anchor=CENTER)
        tree.heading("Name", text="Name", anchor=CENTER)
        tree.heading("Course", text="Course", anchor=CENTER)
        tree.heading("Year Level", text="Year Level", anchor=CENTER)
        tree.heading("Gender", text="Gender", anchor=CENTER)

        tree.place(x=9,y=110,height=450)
        viewList()

def addCourse():
    top=Toplevel()
    top.title('ADD COURSE')
    top.geometry("556x230")
    top.resizable(0,0)
    top.geometry("+{}+{}".format(positionRight+400, positionDown+230))
    
    SecondFrame = Frame(top, bg="#eaebeb")
    SecondFrame.grid()
    
    SecDataFrame = Frame(SecondFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    SecDataFrame.pack(side=BOTTOM)
    
    CourseInf=LabelFrame(SecDataFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Course Information", fg="#104c70")
    CourseInf.pack(side=LEFT)
    
    Cno.set("")
    Cname.set("")
    
    Ccode = Label(CourseInf, font=('Palatino Linotype',13, 'bold'),text="Course Code ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    Ccode.grid(row=1, column=0, sticky=W)
    code = Entry(CourseInf, font=('Palatino Linotype',13),textvariable=Ccode, width=39)
    code.grid(row=1, column=1, pady=8)
    
    CName = Label(CourseInf, font=('Palatino Linotype',13, 'bold'),text="Course Name ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CName.grid(row=2, column=0, sticky=W)
    coursename = Entry(CourseInf, font=('Palatino Linotype',13),textvariable=Cname, width=39)
    coursename.grid(row=2, column=1, pady=8)

    def addCourseData():
        if  code.get() == "" or coursename.get() == "":
            messagebox.showinfo("Student Information System","Please Fill In the Box")
        else:
            mycursor.execute("INSERT INTO COURSE_INFO(course_code,course_name)VALUES(?,?)",
                                     (code.get(),coursename.get()))
            messagebox.showinfo("Student Information System","Course Recorded Successfully")
            top.destroy()
            mydb.commit()
            viewCourseList()
            viewList()
            
    AddCourse=Button(CourseInf, text="ADD COURSE", command=addCourseData,font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    AddCourse.grid(row=3, column=0, columnspan=3,pady=8)
    
def viewCourseList():
    makeList()
    for i in treeSec.get_children():
        treeSec.delete(i)
    counter = 0
    for course in listCourse:
        treeSec.insert(parent='',  index='end', iid=counter,
                        values=(course[1],course[2]))
        counter += 1
        
def searchCourse():
    for i in treeSec.get_children():
        treeSec.delete(i)
    
    search2 = searchbar2.get()
    counter = 0
    for course in listCourse:
        if course[1].startswith(search2):
            treeSec.insert(parent='',  index='end', iid=counter,
                        values=(course[1],course[2]))
        counter += 1
        
def deleteCourse():
    messageDeleteCour = messagebox.askyesno("SSIS", "Do you want to permanently remove this course?")
    if messageDeleteCour > 0:
        selectedCourse = treeSec.selection()[0]
        cnum = treeSec.item(selectedCourse)['values'][0]
        for course in listCourse:
            if cnum == course[1]:
                cnum =course[0]
                break
        mycursor.execute("DELETE FROM COURSE_INFO WHERE course_number=?",(cnum,))
        mydb.commit()
        treeSec.delete(selectedCourse)
        viewList()
        viewCourseList()

def updateCourse(index):
    def thisUpdateCourse(CourseInfo):
        Cselect = treeSec.selection()
        for i in Cselect:
            mycursor.execute("UPDATE COURSE_INFO SET course_name=?\
                             WHERE course_code=?", (Cname.get(),Ccode.get(),))
            mydb.commit()
            messagebox.showinfo("Student Information System","Course updated successfully")
            viewCourseList()
            viewList()
        
    CinfoItem = treeSec.focus()
    values = treeSec.item(CinfoItem,"values")
    
    topUpC=Toplevel()
    topUpC.title('UPDATE COURSE')
    topUpC.geometry("556x230")
    topUpC.resizable(0,0)
    topUpC.geometry("+{}+{}".format(positionRight+400, positionDown+230))
    
    CourseInfo = treeSec.item(index)['values']
    
    CourseFrame = Frame(topUpC, bg="#eaebeb")
    CourseFrame.grid()
            
    DataCFrame = Frame(CourseFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    DataCFrame.pack(side=BOTTOM)
            
    DataCAdd=LabelFrame(DataCFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Course Information", fg="#104c70")
    DataCAdd.pack(side=LEFT)
            
    CCode = Label(DataCAdd, font=('Palatino Linotype',13, 'bold'),text="Course Code  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CCode.grid(row=1, column=0, sticky=W)
    code = Entry(DataCAdd, font=('Palatino Linotype',13),textvariable=Ccode, width=39)
    code.grid(row=1, column=1, pady=8)
            
    CName = Label(DataCAdd, font=('Palatino Linotype',13, 'bold'),text="Course Name ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CName.grid(row=2, column=0, sticky=W)
    courseN = Entry(DataCAdd, font=('Palatino Linotype',13),textvariable=Cname, width=39)
    courseN.grid(row=2, column=1, pady=8)

    CourseSubmit=Button(DataCAdd, text="UPDATE", command=lambda:thisUpdateCourse(CourseInfo), font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    CourseSubmit.grid(row=5, column=0, columnspan=3,pady=8)
    
    Ccode.set(values[0])
    code.config(state=DISABLED)
    Cname.set(values[1])

Cno = IntVar()
Ccode = StringVar()
Cname = StringVar()

searchbar2 = Entry(mainFrame2,font=('Palatino Linotype',12), width=40)
searchbar2.grid(row=1, column=0,columnspan=4, padx=6, pady=5)
searchbutton2 = Button(mainFrame2, text="SEARCH",bg="#eaebeb", fg="#104c70", font=('Palatino Linotype',9,'bold'), width=12,command=searchCourse)
searchbutton2.grid(row=1, column=4, padx=6, pady=5)
    
viewButton2 = Button(mainFrame2, text="VIEW ALL", command=viewCourseList,bg="#eaebeb", fg="#104c70", font=('Palatino Linotype',9,'bold'),width=12)
viewButton2.grid(row=2, column=0, padx=6, pady=5)

addButton2 = Button(mainFrame2, text="ADD COURSE", bg="#eaebeb", fg="#104c70", font=('Palatino Linotype',9,'bold'),width=16,command=addCourse)
addButton2.grid(row=2, column=2, padx=6, pady=5)
    
edit2 = Button(mainFrame2, text="EDIT",bg="#eaebeb", fg="#104c70", font=('Palatino Linotype',9,'bold'), width=11, command=lambda:updateCourse(int(treeSec.focus())))
edit2.grid(row=2, column=3, padx=6, pady=5)
    
delete2 = Button(mainFrame2, text="DELETE",bg="#eaebeb", fg="#104c70", font=('Palatino Linotype',9,'bold'), width=12,command=deleteCourse)
delete2.grid(row=2, column=4, padx=6, pady=5)


treeSec = ttk.Treeview(mainFrame2, height=20)
treeSec.grid(row=3, column=0, columnspan=6, padx=12, pady=10)
    
sSec = ttk.Style(mainFrame2)
sSec.configure("Treeview.Heading", font=('Palatino Linotype',11,'bold'))
sSec.configure(".", font=('Palatino Linotype',12))
        
treeSec['columns'] = ("Course Code","Course Name")

treeSec.column('#0',width=0, stretch=NO)
treeSec.column("Course Code", anchor=W, width=30)
treeSec.column("Course Name", anchor=W, width=210)

treeSec.heading("Course Code", text="Course Code", anchor=CENTER)
treeSec.heading("Course Name", text="Course Name", anchor=CENTER)

treeSec.place(x=8,y=150, height=410, width=430)

viewCourseList()
global there
there=True
clicked()
there=False

treeSec.bind("<ButtonRelease-1>", clicked)
root.mainloop()
=======
"""
CSC151N ASSIGNMENT2: SIMPLE STUDENT INFORMATION SYSTEM
         MAICA A. APIAG    BS-STATISTICS 
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import os
import sqlite3

root = Tk()
root.geometry("1360x720")
root.title('SSIS - Maica A. Apiag')
root.resizable(False, False)
positionRight = int((root.winfo_screenwidth()/2 - 688))
positionDown = int((root.winfo_screenheight()/2 - 386))
root.geometry("+{}+{}".format(positionRight, positionDown))

StdID = StringVar()
Name = StringVar()
Gender = StringVar()
Course = StringVar()
YearLevel = StringVar()

mainFrame = LabelFrame(root, bg="#eaebeb")
mainFrame.place(x=460,y=100,height=575)
#mainFrame.pack(side=RIGHT, padx=20, pady=20)

mainFrame2 = LabelFrame(root, bg="#eaebeb")
mainFrame2.place(x=25,y=100,height=575)

Label(root, text="STUDENT INFORMATION SYSTEM", font = ('Palatino Linotype', 50, 'bold'),fg="#dcdcdc", width=32).grid(row=0,column=0)    
Label(mainFrame, text="STUDENTS", font = ('Palatino Linotype', 30, 'bold'),fg="#104c70",bg="#eaebeb", width=35).grid(row=0,column=0, columnspan=6)
Label(mainFrame2, text="COURSES", font = ('Palatino Linotype', 30, 'bold'),fg="#104c70",bg="#eaebeb", width=10).grid(row=0,column=0, columnspan=5)

mydb = sqlite3.connect('SSIS.db')
mycursor = mydb.cursor()

mydb.execute("PRAGMA foreign_keys = ON;"); 

mycursor.execute("""CREATE TABLE IF NOT EXISTS COURSE_INFO(
        course_number integer PRIMARY KEY,
        course_code text varchar(10),
        course_name text
        )""")


mycursor.execute("""CREATE TABLE IF NOT EXISTS STUD_INFO_SYS(
        ID_number text PRIMARY KEY,
        name text,
        course_number integer,
        year_level text,
        gender text,
        FOREIGN KEY (course_number)
            REFERENCES COURSE_INFO(course_number)
                ON DELETE CASCADE
        )""")

mydb.commit()

def makeList():
    global listStudents
    mycursor.execute("SELECT * FROM STUD_INFO_SYS")
    listStudents = mycursor.fetchall()
    global listCourse
    mycursor.execute("SELECT * FROM COURSE_INFO")
    listCourse = mycursor.fetchall()
    print(listStudents)
    print(listCourse)

def clicked(*args):
    this = treeSec.selection()
    

    if len(this) != 0 or karonLang == True:
        print("here")
        def add():
            top=Toplevel()
            top.title('ADD STUDENTS')
            top.geometry("540x363")
            top.resizable(0,0)
            top.geometry("+{}+{}".format(positionRight+400, positionDown+190))
            
            MainFrame = Frame(top, bg="#eaebeb")
            MainFrame.grid()
            
            DataFrame = Frame(MainFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
            DataFrame.pack(side=BOTTOM)
            
            StudInf=LabelFrame(DataFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
            StudInf.pack(side=LEFT)
            
            StdID.set("")
            Name.set("")
            Course.set("")
            
            SILabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
            SILabel.grid(row=0, column=0, sticky=W)
            ID = Entry(StudInf, font=('Palatino Linotype',13),textvariable=StdID, width=39)
            ID.grid(row=0, column=1, pady=8)
            
            FLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Name", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            FLabel.grid(row=1, column=0, sticky=W)
            name = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Name, width=39)
            name.grid(row=1, column=1, pady=8)
            
            CLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            CLabel.grid(row=2, column=0, sticky=W)
            course = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Course, width=39)
            course.grid(row=2, column=1, pady=8)
            
            YLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            YLabel.grid(row=3, column=0, sticky=W)
            ylevel = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
            ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year','5th Year')
            ylevel.current(0)
            ylevel.grid(row=3, column=1, pady=8)

            GLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            GLabel.grid(row=4, column=0, sticky=W)
            gender = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
            gender['values']=('','Female','Male')
            gender.current(0)
            gender.grid(row=4, column=1, pady=8)
            
            def addData():
                if  ID.get() == "" or name.get() == "" or gender.get() == "" or course.get() == "" or ylevel.get()== "":
                    messagebox.showinfo("Student Information System","Please Fill In the Box")
                else:
                    for student in listStudents:                        
                            if student[0] == ID.get() or student[1] == name.get():
                                messagebox.showinfo("Student Information System","ID Number Already Exists")
                                return
                    x = StdID.get()
                    id_list = []
                    for i in x:
                        id_list.append(i)
                    if "-" in id_list:
                        y = x.split("-")
                        year = y[0]
                        number = y[1]
                        cournum=""
                        if year.isdigit() == False or number.isdigit() == False:
                            messagebox.showerror("SSIS","Invalid ID")
                        else:
                            for cour in listCourse:
                                if cour[2] == course.get():
                                    cournum = cour[0]
                                else:
                                    messagebox.showinfo("Student Information System","Course Not Found")
                            mycursor.execute("INSERT INTO STUD_INFO_SYS(ID_number,name,course_number,year_level,gender)VALUES(?,?,?,?,?)",
                                             (ID.get(),name.get(),cournum,ylevel.get(),gender.get()))
                            messagebox.showinfo("Student Information System","Student Recorded Successfully")
                            top.destroy()
                            mydb.commit()
                            viewList()
                            viewCourseList()
                        
                    else:
                        messagebox.showerror("SSIS","Invalid ID")
                    
            submit=Button(StudInf, text="SUBMIT",command=addData, font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
            submit.grid(row=5, column=0, columnspan=3,pady=8)
            
        def viewList():
            makeList()
            for i in tree.get_children():
                tree.delete(i)
            
            counter = 0
            mycursor.execute("SELECT * FROM STUD_INFO_SYS")
            listStudents = mycursor.fetchall()
            for student in listStudents:
                if listStudents != []:
                    for cour in listCourse:
                        if cour[0] == student[2]:
                            courname = cour[2]
                    #print(treeSec.selection()[1])
                    if karonLang == True or len(this) == 0:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                    
                    elif courname == treeSec.item(treeSec.focus(),"values")[1]:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                counter += 1   
                    
        def search():
            #Deletes the current nodes in the treeview in order to refresh list
            for i in tree.get_children():
                tree.delete(i)
            search = searchbar.get()
            counter = 0
            for student in listStudents:
                if student[0].startswith(search):
                    for cour in listCourse:
                        if cour[0] == student[2]:
                            courname = cour[2]
                    if len(this) == 0:
                        tree.insert(parent='',  index='end', iid=counter,
                                    values=(student[0],student[1],courname,student[3],student[4]))
                    elif courname == treeSec.item(treeSec.focus(),"values")[1]:
                        tree.insert(parent='',  index='end', iid=counter,
                                        values=(student[0],student[1],courname,student[3],student[4]))
                counter += 1
                
        def delete():
            
            selected = tree.selection()[0]
            uid = tree.item(selected)['values'][0]
            mycursor.execute("DELETE FROM STUD_INFO_SYS WHERE ID_number=?",(uid,))
            mydb.commit()
            tree.delete(selected)
            viewList()
            viewCourseList()
            
        def update(index):
            def thisUpdate(studentInfo):
                select = tree.selection()
                for selected in select:
                    
                    mycursor.execute("UPDATE STUD_INFO_SYS SET ID_number=?,name=?,course_number=?,year_level=?,gender=?\
                                     WHERE ID_number=?", (ID.get(),name.get(),course.get(),ylevel.get(),gender.get(),\
                                        tree.set(selected,'#1')))
                    mydb.commit()
                    messagebox.showinfo("Student Information System","Student updated successfully")
                    viewList()
                    viewCourseList()
                
            infoItem = tree.focus()
            values = tree.item(infoItem,"values")
            
            topUpS=Toplevel()
            topUpS.title('UPDATE STUDENTS')
            topUpS.geometry("540x363")
            topUpS.resizable(0,0)
            topUpS.geometry("+{}+{}".format(positionRight+400, positionDown+190))
            
            studentInfo = tree.item(index)['values']
            
            MainFrame2 = Frame(topUpS, bg="#eaebeb")
            MainFrame2.grid()
                    
            DataFrame2 = Frame(MainFrame2,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
            DataFrame2.pack(side=BOTTOM)
                    
            DataAdd2=LabelFrame(DataFrame2, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
            DataAdd2.pack(side=LEFT)
                    
            SILable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
            SILable.grid(row=0, column=0, sticky=W)
            ID = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=StdID, width=39)
            ID.grid(row=0, column=1, pady=8)
                    
            FLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Name  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            FLable.grid(row=1, column=0, sticky=W)
            name = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Name, width=39)
            name.grid(row=1, column=1, pady=8)
                    
            CLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            CLable.grid(row=2, column=0, sticky=W)
            course = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Course, width=39)
            course.grid(row=2, column=1, pady=8)
                    
            YLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            YLable.grid(row=3, column=0, sticky=W)
            ylevel = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
            ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year')
            ylevel.current(0)
            ylevel.grid(row=3, column=1, pady=8) 

            GLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
            GLable.grid(row=4, column=0, sticky=W)
            gender = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
            gender['values']=('','Female','Male')
            gender.current(0)
            gender.grid(row=4, column=1, pady=8)

            submit=Button(DataAdd2, text="UPDATE", command=lambda:thisUpdate(studentInfo), font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
            submit.grid(row=5, column=0, columnspan=3,pady=8)

            StdID.set(values[0])
            ID.config(state=DISABLED)
            Name.set(values[1])
            Course.set(values[2])
            if studentInfo[3] == "1st Year":
                ylevel.current(1)
            elif studentInfo[3] == "2nd Year":
                ylevel.current(2)
            elif studentInfo[3] == "3rd Year":
                ylevel.current(3)
            elif studentInfo[3] == "4th Year":
                ylevel.current(4)
            if studentInfo[4] == "Female":
                gender.current(1)
            elif studentInfo[4] == "Male":
                gender.current(2)
        def viewAll():
            treeSec.selection_clear()
            for item in treeSec.selection():
                treeSec.selection_remove(item)
            kaniLang=True        #print("heressss")
            viewList()
            kaniLang=False
            
        searchbar = Entry(mainFrame,font=('Palatino Linotype',12), width=30)
        searchbar.grid(row=1, column=0, padx=6, pady=5)
        searchbutton = Button(mainFrame, text="SEARCH",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=search)
        searchbutton.grid(row=1, column=1, padx=6, pady=5)
            
        viewButton = Button(mainFrame, text="VIEW ALL", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=13, command=viewAll)
        viewButton.grid(row=1, column=2, padx=6, pady=5)

        addButton = Button(mainFrame, text="ADD STUDENTS", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=16, command=add)
        addButton.grid(row=1, column=3, padx=6, pady=5)
            
        edit = Button(mainFrame, text="EDIT",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=lambda:update(int(tree.focus())))
        edit.grid(row=1, column=4, padx=6, pady=5)
            
        delete = Button(mainFrame, text="DELETE",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=13, command=delete)
        delete.grid(row=1, column=5, padx=6, pady=5)



        tree = ttk.Treeview(mainFrame, height=20)
        tree.grid(row=2, column=0, columnspan=7, padx=12, pady=10)
            
        s = ttk.Style(root)
        s.configure("Treeview.Heading", font=('Palatino Linotype',11,'bold'))
        s.configure(".", font=('Palatino Linotype',12))
                
        tree['columns'] = ("ID number", "Name","Course","Year Level","Gender")

        tree.column('#0',width=0, stretch=NO)
        tree.column("ID number", anchor=CENTER, width=125)
        tree.column("Name", anchor=W, width=250)
        tree.column("Course", anchor=W, width=250)
        tree.column("Year Level", anchor=W, width=130)
        tree.column("Gender", anchor=W, width=100)

        tree.heading("ID number", text="ID number", anchor=CENTER)
        tree.heading("Name", text="Name", anchor=CENTER)
        tree.heading("Course", text="Course", anchor=CENTER)
        tree.heading("Year Level", text="Year Level", anchor=CENTER)
        tree.heading("Gender", text="Gender", anchor=CENTER)

        tree.place(x=9,y=110,height=450)
             
        viewList()

        
def addCourse():
    top=Toplevel()
    top.title('ADD COURSE')
    top.geometry("556x275")
    top.resizable(0,0)
    top.geometry("+{}+{}".format(positionRight+400, positionDown+190))
    
    SecondFrame = Frame(top, bg="#eaebeb")
    SecondFrame.grid()
    
    SecDataFrame = Frame(SecondFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    SecDataFrame.pack(side=BOTTOM)
    
    CourseInf=LabelFrame(SecDataFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Course Information", fg="#104c70")
    CourseInf.pack(side=LEFT)
    
    Cno.set("")
    Cname.set("")
    
    Ccode = Label(CourseInf, font=('Palatino Linotype',13, 'bold'),text="Course Code ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    Ccode.grid(row=1, column=0, sticky=W)
    code = Entry(CourseInf, font=('Palatino Linotype',13),textvariable=Ccode, width=39)
    code.grid(row=1, column=1, pady=8)
    
    CName = Label(CourseInf, font=('Palatino Linotype',13, 'bold'),text="Course Name ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CName.grid(row=2, column=0, sticky=W)
    coursename = Entry(CourseInf, font=('Palatino Linotype',13),textvariable=Cname, width=39)
    coursename.grid(row=2, column=1, pady=8)

    def addCourseData():
        if  code.get() == "" or coursename.get() == "":
            messagebox.showinfo("Student Information System","Please Fill In the Box")
        else:
            mycursor.execute("INSERT INTO COURSE_INFO(course_code,course_name)VALUES(?,?)",
                                     (code.get(),coursename.get()))
            messagebox.showinfo("Student Information System","Course Recorded Successfully")
            top.destroy()
            mydb.commit()
            viewCourseList()
            viewList()
            
    AddCourse=Button(CourseInf, text="ADD COURSE", command=addCourseData,font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    AddCourse.grid(row=3, column=0, columnspan=3,pady=8)
    
def viewCourseList():
    
    makeList()
    for i in treeSec.get_children():
        treeSec.delete(i)
    counter = 0
    for course in listCourse:
        treeSec.insert(parent='',  index='end', iid=counter,
                        values=(course[1],course[2]))
        counter += 1
        
        
def searchCourse():
    #Deletes the current nodes in the treeview in order to refresh list
    for i in treeSec.get_children():
        treeSec.delete(i)
    
    search2 = searchbar2.get()
    counter = 0
    for course in listCourse:
        if course[1].startswith(search2):
            treeSec.insert(parent='',  index='end', iid=counter,
                        values=(course[1],course[2]))
        counter += 1
        
def deleteCourse():
    selectedCourse = treeSec.selection()[0]
    cnum = treeSec.item(selectedCourse)['values'][0]
    for course in listCourse:
        if cnum == course[1]:
            cnum =course[0]
            print("here")
            break
    mycursor.execute("DELETE FROM COURSE_INFO WHERE course_number=?",(cnum,))
    mydb.commit()
    treeSec.delete(selectedCourse)
    viewList()
    viewCourseList()

def updateCourse(index):
    def thisUpdateCourse(CourseInfo):#(CourseInfo):
        Cselect = treeSec.selection()
        for i in Cselect:
            mycursor.execute("UPDATE COURSE_INFO SET course_name=?\
                             WHERE course_code=?", (Cname.get(),Ccode.get(),))
            mydb.commit()
            messagebox.showinfo("Student Information System","Course updated successfully")
            viewCourseList()
            viewList()
        
    CinfoItem = treeSec.focus()
    values = treeSec.item(CinfoItem,"values")
    print(values)
    
    topUpC=Toplevel()
    topUpC.title('UPDATE COURSE')
    topUpC.geometry("556x275")
    topUpC.resizable(0,0)
    topUpC.geometry("+{}+{}".format(positionRight+400, positionDown+190))
    
    CourseInfo = treeSec.item(index)['values']
    
    CourseFrame = Frame(topUpC, bg="#eaebeb")
    CourseFrame.grid()
            
    DataCFrame = Frame(CourseFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    DataCFrame.pack(side=BOTTOM)
            
    DataCAdd=LabelFrame(DataCFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Course Information", fg="#104c70")
    DataCAdd.pack(side=LEFT)
            
    CCode = Label(DataCAdd, font=('Palatino Linotype',13, 'bold'),text="Course Code  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CCode.grid(row=1, column=0, sticky=W)
    code = Entry(DataCAdd, font=('Palatino Linotype',13),textvariable=Ccode, width=39)
    code.grid(row=1, column=1, pady=8)
            
    CName = Label(DataCAdd, font=('Palatino Linotype',13, 'bold'),text="Course Name ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CName.grid(row=2, column=0, sticky=W)
    courseN = Entry(DataCAdd, font=('Palatino Linotype',13),textvariable=Cname, width=39)
    courseN.grid(row=2, column=1, pady=8)

    CourseSubmit=Button(DataCAdd, text="UPDATE", command=lambda:thisUpdateCourse(CourseInfo), font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    CourseSubmit.grid(row=5, column=0, columnspan=3,pady=8)
    
    #ID.config(state=DISABLED)
    Ccode.set(values[0])
    code.config(state=DISABLED)
    Cname.set(values[1])
    
"""
def updateCourse(index2):
    def thisUpdateCourse(courseInfo):
        selectcourse = treeSec.selection()
        for selected in selectcourse:
            mydb = sqlite3.connect('SSIS.db')
            mycursor = mydb.cursor()
            
            mycursor.execute("UPDATE COURSE_INFO SET course_number=?,course_code=?,course_name=?\
                             WHERE course_number=?", (No.get(),CourseCo.get(),CourseN.get(),\
                                treeSec.set(selected,'#1')))
            mydb.commit()
            messagebox.showinfo("Student Information System","Course updated successfully")
            viewCourseList()
            mydb.close
            
        
    courseItem = treeSec.focus()
    values = treeSec.item(courseItem,"values")
    
    top=Toplevel()
    top.title('UPDATE COURSE')
    top.geometry("556x275")
    top.resizable(0,0)
    top.geometry("+{}+{}".format(positionRight+400, positionDown+190))
    
    courseInfo = treeSec.item(index)['values']
    
    CourseFrame = Frame(top, bg="#eaebeb")
    CourseFrame.grid()
            
    DataFrame2 = Frame(CourseFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    DataFrame2.pack(side=BOTTOM)
            
    DataAdd2=LabelFrame(DataFrame2, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Course Information", fg="#104c70")
    DataAdd2.pack(side=LEFT)
            
    CourseNum = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course No  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
    CourseNum.grid(row=0, column=0, sticky=W)
    No = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Cno, width=39)
    No.grid(row=0, column=1, pady=8)
            
    CourseCode = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course Code  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CourseCode.grid(row=1, column=0, sticky=W)
    CourseCo = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Ccode, width=39)
    CourseCo.grid(row=1, column=1, pady=8)
            
    CourseName = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course Name ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CourseName.grid(row=2, column=0, sticky=W)
    CourseN = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Cname, width=39)
    CourseN.grid(row=2, column=1, pady=8)

    submit=Button(DataAdd2, text="UPDATE",  font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    submit.grid(row=5, column=0, columnspan=3,pady=8)
    
    No.insert(0, studentInfo[0])
    CourseCo.insert(0, studentInfo[1])
    CourseN.insert(0, studentInfo[2])
    """

Cno = IntVar()
Ccode = StringVar()
Cname = StringVar()

searchbar2 = Entry(mainFrame2,font=('Palatino Linotype',12), width=37)
searchbar2.grid(row=1, column=0,columnspan=4, padx=6, pady=5)
searchbutton2 = Button(mainFrame2, text="SEARCH",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=10,command=searchCourse)
searchbutton2.grid(row=1, column=4, padx=6, pady=5)
    
viewButton2 = Button(mainFrame2, text="VIEW ALL", command=viewCourseList, bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=10)
viewButton2.grid(row=2, column=0, padx=6, pady=5)

addButton2 = Button(mainFrame2, text="ADD COURSE", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=15,command=addCourse)
addButton2.grid(row=2, column=2, padx=6, pady=5)
    
edit2 = Button(mainFrame2, text="EDIT",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=10, command=lambda:updateCourse(int(treeSec.focus())))
edit2.grid(row=2, column=3, padx=6, pady=5)
    
delete2 = Button(mainFrame2, text="DELETE",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=10,command=deleteCourse)
delete2.grid(row=2, column=4, padx=6, pady=5)


treeSec = ttk.Treeview(mainFrame2, height=20)
treeSec.grid(row=3, column=0, columnspan=6, padx=12, pady=10)
    
sSec = ttk.Style(mainFrame2)
sSec.configure("Treeview.Heading", font=('Palatino Linotype',11,'bold'))
sSec.configure(".", font=('Palatino Linotype',12))
        
treeSec['columns'] = ("Course Code","Course Name")

treeSec.column('#0',width=0, stretch=NO)
treeSec.column("Course Code", anchor=W, width=125)
treeSec.column("Course Name", anchor=W, width=210)

treeSec.heading("Course Code", text="Course Code", anchor=CENTER)
treeSec.heading("Course Name", text="Course Name", anchor=CENTER)

treeSec.place(x=8,y=150, height=410)
"""
def clickedcourse(*args):
    edit['state'] = NORMAL
    delete['state'] = NORMAL
    
treeSec.bind("<Button-1>", clickedcourse)
"""
viewCourseList()
karonLang=True
clicked()
karonLang=False

treeSec.bind("<ButtonRelease-1>", clicked)
#print()
root.mainloop()

>>>>>>> efaae4437dcd449154c89044f5b1075db6fd9740
