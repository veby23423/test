from django.urls import path
from . import views


handler404 = "app.views.page_not_found"

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("save_article/", views.save_article, name="save_article"),
    path("check_action/", views.check_action, name="check_action"),
    path("novostiRu/", views.novostiru, name="novostiru"),
    path("setstate/", views.setstate, name="setstate"),
    path("addstatie_1/", views.addstatie_1, name="addstatie_1"),
    path("post/<int:id_statie>/", views.post_statie, name="post_statie"),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:id_profile>/", views.profile_suces, name="profile_suces"),
    path("setpassworld/", views.setpassworld, name="setpassworld"),
    path("passworld_update/", views.passworld_update, name="passworld_update"),
    path("setname/", views.setname, name="setname"),
    path("name_update/", views.name_update, name="name_update"),
    path("setemail/", views.setemail, name="setemail"),
    path("email_update/", views.email_update, name="email_update"),

]
