from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("contact_us/",views.contact,name="contact_us"),
    path("about_us/",views.about, name="about_us"),
    path("to_does/",views.to_does, name="to_do"),
    path("remove/<int:pk>",views.remove,name="remove"),
    path('mark_compeleted/<int:id>',views.markcomp, name="mark_comp"),
    path('sign_up/',views.sign_up,name='sign_up')
]
