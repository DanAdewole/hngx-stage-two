from django.urls import path

from .views import PersonList, PersonDetail


urlpatterns = [
	path("api", PersonList.as_view(), name="person_list"),
 	path("api/<str:name>", PersonDetail.as_view(), name="person_detail")
]
