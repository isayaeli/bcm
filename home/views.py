from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def exchange(request):
	return render(request, 'home/exchange.html')

def about(request):
	return render(request, 'home/about.html')

def contacts(request):
	return render(request, 'home/contacts.html')

def register(request):
	return render(request, 'home/register.html')

def fee(request):
	return render(request, 'home/fee_schedule.html')

def faq(request):
	return render(request, 'home/faq.html')


def beginer(request):
	return render(request, 'home/beginer.html')

def terms(request):
	return render(request, 'home/terms.html')

def policy(request):
	return render(request, 'home/terms.html')