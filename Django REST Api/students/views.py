from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
        },
          {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
        },
          {
            'id': 2,
            'name': 'Yo Hassan',
            'age': 21,
        },
          {
            'id': 3,
            'name': 'Doe',
            'age': 23,
        },

    ]
    return HttpResponse(students)