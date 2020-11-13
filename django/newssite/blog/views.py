from django.shortcuts import render
from django.utils import timezone
from datetime import datetime,timedelta
from .models import Post, Resume, Vacancy
from .forms import ResumeForm, VacancyForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from django.db.models import F
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from itertools import chain
import os, time
from os import path


def homePageView(request):
    return render(request, 'blog/worker.html', )


@csrf_exempt
def python_developer(request):
    if datetime.today().day == 1:
        month = datetime.today().month - 2
        vacancy = Vacancy.objects.filter(published_date__day__lt=month)
        vacancy.delete()
    worker_list = Vacancy.objects.filter(position__icontains="python")
    file_date = datetime.fromtimestamp(path.getmtime('/django/newssite/blog/json/cache_python.txt'))
    delta_time = (datetime.now() - file_date).days
    if delta_time > 0:
        url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
        for page in range(1, 6):
            data = {
    	    "keywords": "python developer",
    	    "page": str(page)}
            payload = requests.post(url, json=data)
            vacancies = payload.json()["jobs"]
            if page == 1:
                vacancies_list = vacancies
            vacancies_list += vacancies
        with open('/django/newssite/blog/json/cache_python.txt', 'w') as f:
              f.write(json.dumps(vacancies_list))
    with open('/django/newssite/blog/json/cache_python.txt', 'r') as f:
         vacancies_lists = json.load(f)
    vacancies_list = list(chain(worker_list, vacancies_lists))
    paginator = Paginator(vacancies_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/vacancies_list.html', context)


@csrf_exempt
def java_developer(request):
    if datetime.today().day == 1:
        month = datetime.today().month - 2
        vacancy = Vacancy.objects.filter(published_date__day__lt=month)
        vacancy.delete()
    worker_list = Vacancy.objects.filter(position__icontains="java")
    file_date = datetime.fromtimestamp(path.getmtime('/django/newssite/blog/json/cache_java.txt'))
    delta_time = (datetime.now() - file_date).days
    if delta_time > 0:
        url = "https://ru.jooble.org/api/46f8fbb2-41ac-4877-aa20-4b2479feb675"
        for page in range(1, 6):
            data = {"keywords": "java developer",
    	           "page": str(page)}
            payload = requests.post(url, json=data)
            vacancies = payload.json()["jobs"]
            if page == 1:
                vacancies_list = vacancies
            vacancies_list += vacancies
        with open('/django/newssite/blog/json/cache_java.txt', 'w') as f:
              f.write(json.dumps(vacancies_list))
    with open('/django/newssite/blog/json/cache_java.txt', 'r') as f:
         vacancies_lists = json.load(f)
    vacancies_list = list(chain(worker_list, vacancies_lists))
    paginator = Paginator(vacancies_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/vacancies_list.html', context)


def create_resume(request):
    form = ResumeForm()
    context = {'form': form}
    return render(request, 'blog/create_resume.html', context)


def create_vacancy(request):
    form = VacancyForm()
    context = {'form': form}
    return render(request, 'blog/create_vacancy.html', context)


def manage_resume(request):
    user = authenticate(username=request.POST['email'],password= request.POST['password'],)
    if user is None:
        try:
            user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        except:
            return render(request, 'blog/create_user.html')
    request.session["user"] = user.id
    form = ResumeForm(request.POST)
    if form.is_valid():
        pk = form.save().id
    resume = Resume.objects.get(pk=pk)
    resume.user = user
    resume.save()
    context = {'resume': resume}
    return render(request, 'blog/resume.html', context)


def manage_vacancy(request):
    user = authenticate(username=request.POST['email'],password= request.POST['password'])
    if user is None:
        try:
            user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        except:
            return render(request, 'blog/create_user.html')
    request.session["user"] = user.id
    form = VacancyForm(request.POST)
    if form.is_valid():
        pk  = form.save().id
    vacancy = Vacancy.objects.get(pk=pk)
    vacancy.user = user
    vacancy.save()
    context = {'vacancy': vacancy}
    return render(request, 'blog/vacancy.html', context)


def resume_list(request):
    if datetime.today().day == 1:
        month = datetime.today().month - 2
        resumes = Resume.objects.filter(published_date__day__lt=month)
        resumes.delete()
    resume_list =Resume.objects.all().order_by("-published_date")


    paginator = Paginator(resume_list, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/resume_list.html', context)


def cabinet(request):
    user_id= request.session.get("user", "red")
    if user_id != 'red':
        resumes = Resume.objects.filter(user=user_id).order_by("-published_date")
        vacancies = Vacancy.objects.filter(user=user_id).order_by("-published_date")
        cabinet_list = list(chain(resumes, vacancies))
    else:
        return render(request, "blog/create_user.html")
    paginator = Paginator(cabinet_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}
    return render(request, 'blog/cabinet.html', context)


def enter(request):
    user = authenticate(username=request.POST['email'],password=request.POST['password'])
    if user:
        request.session["user"] = user.id
        return redirect('blog:cabinet')
    return render(request, "blog/create_user.html")


def create_user(request):
    user = authenticate(username=request.POST['email'],password=request.POST['password'])
    if user:
        request.session["user"] = user.id
        return redirect('blog:cabinet')
    context = {"user": user}
    return render(request, 'blog/create_user.html', context)


def change_resume(request, pk):
    resume = get_object_or_404(Resume,pk=pk)
    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        form.save()
        resume.published_date = timezone.now()
        resume.save()
        context = {'resume': resume }
        return render(request, 'blog/resume.html', context)
    else:
        form_resume = ResumeForm(instance=resume)
        context = {"form_resume":form_resume}
    return render(request, 'blog/change_resume_vacancy.html', context)

def change_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        form.save()
        vacancy.published_date = timezone.now()
        vacancy.save()
        context = {'vacancy': vacancy}
        return render(request, 'blog/vacancy.html', context)
    else:
        form = VacancyForm(instance=vacancy)
        context = {"form":form}
    return render(request, 'blog/change_resume_vacancy.html', context)


def update_resume(request, pk):
    resume = get_object_or_404(Resume,pk=pk)
    resume.published_date = timezone.now()
    resume.save()
    return redirect('blog:cabinet')


def update_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy,pk=pk)
    vacancy.published_date = timezone.now()
    vacancy.save()
    return redirect('blog:cabinet')


def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request, 'blog/resume.html', context)


def vacancy_detail(request, pk):
    vacancy= Vacancy.objects.get(pk=pk)
    context = {'vacancy': vacancy}
    return render(request, 'blog/vacancy.html', context)
