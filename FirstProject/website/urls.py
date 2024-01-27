from django.urls import path
from website import views

urlpatterns = [
    path('',views.index, name="home"),
    path('about',views.about, name="about"),
    path('store',views.store_data, name="store"),
    path('show',views.show_data, name="show"),
    path('insert',views.insert, name="insert"),
    path('insert_show',views.insert_show, name="insert_show"),
    path('emp_edit/<int:id>',views.emp_edit, name="emp_edit"),
    path('emp_update/<int:id>',views.emp_update, name="emp_update"),
    path('emp_del/<int:id>',views.emp_delete, name="emp_del"),
    path('trush',views.del_trush, name="trush"),
    path('restore/<int:id>',views.emp_restore, name="restore"),
    path('emp_trush_del/<int:id>',views.emp_trush_delete, name="emp_trush_del"),
    path('delete_all',views.delete_all, name="delete_all")
]