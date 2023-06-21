from django.shortcuts import render
from django.http import JsonResponse
from course.tasks import CourseTask
# Create your views here.


def do(request):
    print('into do...')
    CourseTask().delay() 
    print('goto do...')
    return JsonResponse({'result': "ok"})
