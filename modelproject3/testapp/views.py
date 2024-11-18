from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    student_list = Student.objects.all()
    my_dict = {'student_list':student_list}
    return render(request,'testapp/std.html',my_dict)