from django.shortcuts import render
from quizapp.models import Exams

def examonline(request):
    results=Exam.objects.all()
    return render(request, 'Index.html', {"Exams":results})