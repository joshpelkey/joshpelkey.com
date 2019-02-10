from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):

	return render(request, 'welcome.html')

def anna_gray_college(request):

	return render(request, 'anna-gray-college.html')
