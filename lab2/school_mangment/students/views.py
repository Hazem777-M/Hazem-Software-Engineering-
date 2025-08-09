from django.shortcuts import render, redirect

# تعريف قائمة الطلاب مرة واحدة فقط
students_list = [
    {'id': 1, 'first_name': 'محمد', 'last_name': 'علي', 'age': 20, 'gender': 'ذكر', 'university_level': 'ثاني', 'is_regular': 'نعم'},
    {'id': 2, 'first_name': 'فاطمة', 'last_name': 'أحمد', 'age': 19, 'gender': 'أنثى', 'university_level': 'ثالث', 'is_regular': 'نعم'},
    {'id': 3, 'first_name': 'خالد', 'last_name': 'سعد', 'age': 22, 'gender': 'ذكر', 'university_level': 'رابع', 'is_regular': 'لا'},
]

# دالة للصفحة الرئيسية (home)
def home(request):
    return render(request, 'students/home.html')

def index(request):
    context = {'students': students_list}
    return render(request, 'students/index.html', context)

def delete_student(request):
    return render(request, 'students/delete_student.html')

def update_student(request):
    return render(request, 'students/update_student.html')

def Show(request):
    Students = {
        "name": "Hazem",
        "marks": [90, 85, 90],
        "M": {"image processing": 90, "AI": 85, "ML": 96}
    }
    return render(request, 'students/show.html', Students)

def show_fillters(request):
    name = {"fname": "Hazem Hazam"}
    return render(request, 'students/show_fillters.html', name)

def check_age(request, id):
    student = next((s for s in students_list if s['id'] == id), None)

    if student:
        is_older_than_20 = student['age'] > 20
        context = {'is_older_than_20': is_older_than_20, 'student_name': student['first_name']}
        return render(request, 'students/check_age.html', context)
    else:
        return redirect('index')