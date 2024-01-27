from django.shortcuts import render,HttpResponse, redirect
from website.form import std
from website.models import student_info
from website.models import  employee_info
import sweetify

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def store_data(request):
    # For django default form
    form = std()
    if request.method == 'POST':
        form = std(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'store.html',{'form': form}) 

def show_data(request):
    # For django default form
    std_info = student_info.objects.all()
    context = {
        'std_info' : std_info
    }
    return render(request,'store_data_show.html', context)


def insert(request):
    if request.method == 'POST' and request.FILES:
        x = request.POST.get('emp_name')
        y = request.POST.get('emp_email')
        z = request.FILES['emp_pic']
        
        employee_insert = employee_info(
            emp_name = x,
            emp_email = y,
            emp_pic = z
        )
        employee_insert.save()
        # sweetify.success(request, 'You did it', text='Your Form has been Updated',persistent='Hell yeah')
        sweetify.toast(request, "Successful Update")

    return render(request,'insert.html')


def insert_show(request):
    # insert_data_show =employee_info.objects.all()
    insert_data_show =employee_info.objects.filter(is_delete = 0)
    return render(request,'insert_data_show.html', {'insert_data_show': insert_data_show})

def emp_edit(request, id):
    emp_info = employee_info.objects.filter(id=id)
    return render(request, 'emp_edit.html', {'emp_info': emp_info})

def emp_update(request, id):
    if request.method == 'POST' and request.FILES:
        x = request.POST.get('emp_name')
        y = request.POST.get('emp_email')
        z = request.FILES['emp_pic']
        
        employee_insert = employee_info.objects.filter(id=id)
        employee_insert = employee_info(
            id = id,
            emp_name = x,
            emp_email = y,
            emp_pic = z
        )
        employee_insert.save()
    else:
        x = request.POST.get('emp_name')
        y = request.POST.get('emp_email')
        z = request.POST.get('emp_pic_1')
        
        
        employee_insert = employee_info.objects.filter(id=id)
        employee_insert = employee_info(
            id = id,
            emp_name = x,
            emp_email = y,
            emp_pic = z
        )
        employee_insert.save()
    return redirect('insert_show')

# def emp_delete(request, id):
#     emp_del = employee_info.objects.filter(id=id)
#     emp_del.delete()
#     return redirect('insert_show')

def emp_delete(request, id):
    emp_del = employee_info.objects.get(id=id)
    emp_del.is_delete = True
    emp_del.save()
    return redirect('insert_show')

def del_trush(request):
    insert_data_show =employee_info.objects.filter(is_delete = 1)
    return render(request,'trush.html', {'insert_data_show': insert_data_show})

def emp_restore(request, id):
    emp_del = employee_info.objects.get(id=id)
    emp_del.is_delete = False
    emp_del.save()
    return redirect('insert_show')

def emp_trush_delete(request, id):
    emp_del = employee_info.objects.filter(id=id)
    emp_del.delete()
    return redirect('trush')

def delete_all(request):
    del_emp = request.POST.getlist('del_emp')

    for i in del_emp:
        employee_del = employee_info(
            id = i
        )
        employee_del.delete()
    return redirect('trush')