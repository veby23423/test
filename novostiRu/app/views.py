from django.shortcuts import render, redirect
from app.models import App, Statie


def register(request):
    return render(request, "app/register.html", {"title": "Регистрация"})


def login(request):
    return render(request, "app/login.html", {"title": "Вход"})


def save_article(request):
    app = App()
    app.name = request.POST.get("name")
    app.email = request.POST.get("email")
    app.passworld = request.POST.get("passworld")

    app.save()
    # object_db = App(name="Алеша", email="veby@bk.ru", passworld="123123")
    # object_db.save()

    return redirect("http://127.0.0.1:8000/login/")


last_login = None
last_email = None

def check_action(request):
    global last_login
    global last_email
    email = request.POST.get("email")
    passworld = request.POST.get("passworld")

    app = App.objects.all()

    # return redirect("http://127.0.0.1:8000/login/")

    i = 0
    while True:
        try:
            index_app = app[i]

            email_db = index_app.email
            passworld_db = index_app.passworld
            if email_db == email and passworld_db == passworld:
                last_login = index_app.id
                last_email = index_app.email
                return redirect("http://127.0.0.1:8000/novostiRu/")
            else:
                i += 1
        except Exception as ex:
            print("Ошибка", ex)
            break


def novostiru(request):
    statie = Statie.objects.all()

    data = {
        "all_statie": statie,
    }

    return render(request, "app/novostiRu.html", context=data)


def setstate(request):
    return render(request, "app/menu_save_db.html")


def addstatie_1(request):
    title = request.POST.get("title")
    anons = request.POST.get("anons")
    full_text = request.POST.get("full_text")

    statie = Statie()
    statie.title = title
    statie.anons = anons
    statie.full_text = full_text
    statie.save()

    return redirect("http://127.0.0.1:8000/novostiRu/")


def post_statie(request, id_statie):
    statie = Statie.objects.all()

    i = 0
    while True:
        try:
            index_statie = statie[i]

            title = index_statie.title
            full_text = index_statie.full_text
            id_statie_db = index_statie.id

            if int(id_statie_db) == int(id_statie):
                data = {
                    "title": title,
                    "full_text": full_text,
                    "id": id_statie_db,
                }

                return render(request, "app/show_full_statie.html", context=data)
            else:
                i += 1

        except Exception as ex:
            print(ex)
            break


def profile(request):
    global last_login
    app = App.objects.all()

    i = 0
    while True:
        index_app = app[i]
        pk_log = index_app.pk

        if int(last_login) == int(pk_log):
            return render(request, "app/succes_profile.html", {"id": pk_log})
        else:
            i += 1


def profile_suces(request, id_profile):
    app = App.objects.all()

    i = 0
    while True:
        index_app = app[i]
        pk = index_app.pk

        try:
            if int(pk) == int(id_profile):
                name = index_app.name
                email = index_app.email
                passworld = index_app.passworld

                data = {
                    "name": name,
                    "email": email,
                    "passworld": passworld,
                }

                return render(request, "app/profile.html", context=data)
            else:
                i += 1
        except Exception as ex:
            print(ex)
            break


def setpassworld(request):
    return render(request, "app/setpassworld.html")


def passworld_update(request):
    new_passworld = request.POST.get("passworld")

    app = App.objects.all()

    i = 0
    while True:
        try:
            index_app = app[i]

            if int(index_app.pk) == int(last_login):
                index_app.passworld = new_passworld
                index_app.save()
                return redirect("http://127.0.0.1:8000/profile/")

            else:
                i += 1

        except Exception as ex:
            print(ex)
            break

def setname(request):
    return render(request, "app/setname.html")
    
    

def setemail(request):
    return render(request, "app/setemail.html")
    

def name_update(request):
    new_name = request.POST.get("name")

    app = App.objects.all()

    i = 0
    while True:
        try:
            index_app = app[i]

            if int(index_app.pk) == int(last_login):
                index_app.name = new_name
                index_app.save()
                return redirect("http://127.0.0.1:8000/profile/")

            else:
                i += 1

        except Exception as ex:
            print(ex)
            break

def email_update(request):
    new_email = request.POST.get("email")


    app = App.objects.all()

    cheack = False
    i = 0
    while True:
        try:
            index_app = app[i]

            if new_email == index_app.email:
                cheack = True
                break
            else:
                cheack = False
                i += 1

        except Exception as ex:
            print(ex)
            break
    
    while True:
        if cheack:
            return redirect("http://127.0.0.1:8000/profile/")
        else:
            if int(index_app.pk) == int(last_login):
                index_app.email = new_email
                index_app.save()
                return redirect("http://127.0.0.1:8000/profile/")

            else:
                i += 1
            



def page_not_found(request, exception):
    return render(request, "app/404.html", status=404)