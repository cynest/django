from django.conf.urls import url

from . import views

"""Form URL documentation

urlpatterns sorts urls based on characters after form in the url

if no characters it goes to form,
if it begins with your it goes to the index test page

thanks will redirect to form unless directed to by form, in which case it
returns the reverse of the string in the your_name entry in the post dictionary

"""

urlpatterns = [
	url(r'^$',views.get_name, name = 'name'),
	url(r'^thanks',views.thanks, name = 'thanks'),
	url(r'^your',views.index, name= 'test'),
	url(r'^', views.formredirect, name = 'redirect'),
]