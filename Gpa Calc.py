import flet as ft
from flet import TextField,ElevatedButton,Text,Row,Column,Page
from flet_core.control_event import ControlEvent
from flet import RouteChangeEvent,ViewPopEvent, CrossAxisAlignment,MainAxisAlignment
i=0

def main(page:ft.page)->None:
    page.title = "Gpa Calcualtor"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_aligment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 600
    page.window_height = 600
    page.window_resizeable=True
    page.update()
    #Setup fields
    text_Course =TextField(label="Course Name",text_align=ft.TextAlign.CENTER,width=200)
    text_Grade =TextField(label="Grade",text_align=ft.TextAlign.CENTER,width=200)
    text_Credit =TextField(label="Credit",text_align=ft.TextAlign.CENTER,width=200)
    page.add(ft.Row(
        controls=[
         text_Course
        ],alignment=ft.MainAxisAlignment.CENTER
    ))
    page.add(ft.Row(
        controls=[
         text_Grade
        ],alignment=ft.MainAxisAlignment.CENTER
    ))
    page.add(ft.Row(
        controls=[
         text_Credit
        ],alignment=ft.MainAxisAlignment.CENTER
    ))
    Grades = {}

    #Function for Add button 
    def add(e):
      global i
      course = text_Course.value
      grade= text_Grade.value
      credit = int(text_Credit.value)
      Grades[i]={ "course":course,
       "grade":grade,"credit":credit}
      i+=1
      page.clean()
      page.add(ft.Row(
        controls=[
         text_Course
        ],alignment=ft.MainAxisAlignment.CENTER
      ))
      page.add(ft.Row(
        controls=[
         text_Grade
        ],alignment=ft.MainAxisAlignment.CENTER
     ))
      page.add(ft.Row(
        controls=[
         text_Credit
        ],alignment=ft.MainAxisAlignment.CENTER
     ))
      page.add(ft.Row(
        controls=[
         button_Add,button_Calc
        ],alignment=ft.MainAxisAlignment.CENTER
     ))
      page.update()
      print(Grades)

    #Function for Calc button 
    def Calc(e):
      page.clean()
      page.add(ft.Row(
        controls=[
         ft.Text(str(Calculate_Gpa(Grades,len(Grades))))
        ],alignment=ft.MainAxisAlignment.CENTER
     ))
      page.update()
      


    button_Add = ElevatedButton(text="Add",width=200,on_click=add)
    button_Calc = ElevatedButton(text="Gpa",width=200,on_click=Calc)

    page.add(ft.Row(
        controls=[
         button_Add,button_Calc
        ],alignment=ft.MainAxisAlignment.CENTER
     ))
    page.update()
    





def Calculate_Gpa(Grades, Courses_num):
    # Verifying variables for Gpa and hours
    Total_Credits_per_Hours = 0
    Total_Grade_Points = 0

    # Translating Grade into points
    for i in range(Courses_num):
        if Grades[i]['grade'] == 'A':
            grade_points = 4.0
        elif Grades[i]['grade'] == 'A-':
            grade_points = 3.7
        elif Grades[i]['grade'] == 'B+':
            grade_points = 3.3
        elif Grades[i]['grade'] == 'B':
            grade_points = 3.0
        elif Grades[i]['grade'] == 'B-':
            grade_points = 2.7
        elif Grades[i]['grade'] == 'C+':
            grade_points = 2.3
        elif Grades[i]['grade'] == 'C':
            grade_points = 2.0
        elif Grades[i]['grade'] == 'C-':
            grade_points = 1.7
        elif Grades[i]['grade'] == 'D+':
            grade_points = 1.3
        elif Grades[i]['grade'] == 'D':
            grade_points = 1.0
        elif Grades[i]['grade'] == 'F':
            grade_points = 0.0
        else:
            # If there is a problem in grade, return the course for the user
            print(f"Invalid grade for course {Grades[i]['course']}: {Grades[i]['grade']}")
            continue

        # Calculating the Total of Grade and credits to use in the last func
        Total_Grade_Points += grade_points*Grades[i]['credit']
        Total_Credits_per_Hours += Grades[i]['credit']

    if Total_Credits_per_Hours == 0:
        return 0
    else:
        Gpa = Total_Grade_Points / Total_Credits_per_Hours
        return round(Gpa, 2)


ft.app(main)