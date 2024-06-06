from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from app.models import Customers
from app.forms import CustomersForm, AddressForm
from django.db.models import Q

def index(request):
    customers = Customers.objects.all()
    peginator = Paginator(customers,10) # bunda ekranga nechta user chiqishini ko'rsatadi per_page: 5 bunda ekranga 5 ta malumot chiqadi
    page_number = request.GET.get("page")
    page_obj = peginator.get_page(page_number)

    search_query = request.GET.get('search','')
    if search_query:
        page_obj = Customers.objects.filter(Q(first_name__search=search_query) | Q(email__search=search_query))
    context = {
        # 'customers': customers
        'page_obj': page_obj
    }
    return render(request, 'app/index.html', context)

def detail(requsest, pk):
    customers = Customers.objects.get(id=pk)
    context = {
        'customers': customers

    }
    return render(requsest,'app/deatil.html', context)

def add_customers(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomersForm()
        context = {
            'form': form
        }
        return render(request,'app/add-customer.html', context)
#############################################3
""" mana bu view customerga malimot qoshgandan keyin adresga otib yuboradi lekin customet bazaga saqlanmay qolaopti yani adres kiritgandan keim
 o'sha cuntomerga biriktirish uchun o'sha kustomer chiqmay qolopti shuni unstida ish olib borilmoqda hozir """
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddressForm()
        context = {
            'form':form
        }
        return render(request,'app/Address.html', context)
# ##############################################3
def delet_customers(request,pk):
    customers = Customers.objects.get(id=pk)

    if customers:
        customers.delete() # bu kamanda malumotni delet qiladi yani id teng bo'lgan idga bunda o'sha idni delete qiladi
        return redirect('index')

    context = {
        'customers':customers
    }
    return render(request, 'app/index.html', context)

def edit_customers(request, pk):
    customers = Customers.objects.get(id=pk) # keloptgan idga egan userga o'tadi yabi id teng bo'lsa idga o'sha userga o'tadi
    form = CustomersForm(instance=customers)  # malumotlarini to'ldirib beradi
    if request.method == 'POST':
        form = CustomersForm(request.POST, request.FILES, instance=customers) # POST keladigan malumotlar agar imege bo'ls uni POST bn emas FILES bilan olinadi
        if form.is_valid():
            form.save()
            return redirect('index')

    context ={
        'customers':customers,
        'form': form
    }
    return render(request,'app/edit-customer.html',context)