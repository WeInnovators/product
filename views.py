from django.shortcuts import render,redirect
from .models import Product,Order,Customer


def dashboard(request):
    ord=Order.objects.all()
    cust=Customer.objects.all()
    total_customer=cust.count()
    total_order=ord.count()
    deliver=ord.filter(status='Delivered').count()
    pending=ord.filter(status='Pending').count()
    context={
        'ord':ord,
        'cust':cust,
        'total_customer':total_customer,
        'total_order':total_order,
        'deliver':deliver,
        'pending':pending,
    }
    return render(request,'DB/dashboard.html',context)

def customer(request):
    cust=Customer.objects.all()
    return render(request,'DB/customer.html',{'cust':cust})

def product(request):
    item = Product.objects.all()
    return render(request,'DB/product.html',{'item':item})