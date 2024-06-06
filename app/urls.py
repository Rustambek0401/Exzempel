from django.contrib import admin
from django.urls import path
from app.views import index,detail,add_customers,delet_customers,edit_customers, address

urlpatterns = [
            path('', index, name='index'), # asosiy oynani ochadi
            path('detail/<int:pk>', detail, name='detail'), # detailni ochadi
            path('add-customers/', add_customers, name='add_customers'), #bu customerga malumot qo'shish oynasiga yo'naltiradi
            path('address/', address, name='address'),  #adresga yonaltiradi
            path('delet/<int:pk>',delet_customers, name='delet'), # delet qiladi
            path('edit/<int:pk>', edit_customers, name='edit'), # malumotni yangiladi
]