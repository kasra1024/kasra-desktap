from django.shortcuts import render , redirect
from student.models import students , Course
from student.forms import StudentForm
from django.views import View 
from student.forms import CourseStudentForm
# Create your views here.



def student_view (request) : 
    form = StudentForm()
    html_file = "student/all_student.html" 
    if request.method == 'GET' : 
 
        all_students = students.objects.all() 
        context = {"studentss" : all_students , "form": form}
        
        return render(request , html_file , context)
    
    elif request.method == 'POST' : 
        data = request.POST
        fullname1 = data['full_name'] 
        username1 = data['name'] 
        phone1 = data['phone_number'] 
        students.objects.create(full_name = fullname1 , name = username1 , phone_number = phone1 , score = 0)
        return render (request , html_file , {"form" : form})


# ---------------------------------------------------------------------

def courses_view (request) : 
    all_courses = Course.objects.all()
    context = {"course" : all_courses}
    return render (request , 'student/courses.html ', context)

# ---------------------------------------------------------------------

class CreateStudent (View) : 
    form = StudentForm() 
    template = "student/create_student.html"

    def get (self , request) : 
        return render (request , self.template , {"form" : self.form})

    def post (self , request) : 
        st_form = StudentForm(request.POST)
        if st_form.is_valid() :  
            new_student = st_form.save()
            # new_student = students.objects.create(
                # full_name = request.POST["full_name"] , name = request.POST["name"] , phone_number= request.POST["phone_number"])
            if new_student :
                return redirect ("account: user_register")
        return render (request , self.template , {"form" : self.form , "message" : "input is valid"})
    

# ----------------------------------------------------------------------------------------------------------------------------- 

# 3


def AddCourse (request) : 
    
    template = "Course/add_course.html"

    if request.method == "GET" :
        form = CourseStudentForm()
        all_course = Course.objects.all() 
        return render (request , template , {"form" : form , "courses" : all_course}) 
    
    elif request.method == "POST" : 
        co_form = CourseStudentForm(request.POST)
        if co_form.is_valid () : 
            co_form.save() 
            return redirect ("account: user_register")
        
        else : 
            all_course = Course.objects.all() 
            
    
    return render (request , template , {"form" : form ,"courses" : all_course, "message" : "input is valid!!"}) 

# ----------------------------------------------------------------------------------------------------------------------------------

# 4

def course_list (request) : 
    all_courses = Course.objects.all()
    context = {"all_courses" : all_courses}
    template = "student/courses_list_new.html"
    return render (request , template , context) 
