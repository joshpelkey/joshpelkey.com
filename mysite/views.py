from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):

	return render(request, 'welcome.html')

def eighteen_playlist(request):

	return render(request, '18playlist.html')

def welcome_college(request):

	return render(request, 'welcome-college.html')

def anna_gray_college(request):

	return render(request, 'anna-gray-college.html')

def clara_jayne_college(request):

	return render(request, 'clara-jayne-college.html')
