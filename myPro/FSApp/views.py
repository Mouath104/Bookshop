from re import template
from turtle import update
from unittest import loader
from django.shortcuts import HttpResponse,HttpResponseRedirect,render
from FSApp import models
from django.template import loader 

from FSApp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

#Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# @login_required
def index(req):
    authorized=req.user.is_superuser
    # userId = req.user.id;
    context = models.Books.objects.all()
    templ=loader.get_template("index.html")
    page = req.GET.get('page', 1)
    paginator = Paginator(context, 13)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    con = {
        'books' :books,
        'authorized':authorized,
        # 'userId':userId,
        }
    return HttpResponse(templ.render(con,req))

    ## trying to add a Paginator

    # user_list = User.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(user_list, 10)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)

    # return render(request, 'core/user_list.html', { 'users': users })


def add(req):
    if(req.user.is_superuser):
        templ=loader.get_template("add.html")
        return HttpResponse(templ.render({},req))
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/sorry")


def addP(request):
    if(request.user.is_superuser):
        price = request.POST['price']
        author = request.POST['author']
        img = request.POST['img']
        Desc = request.POST['Desc']
        title = request.POST['title']
        Book=models.Books(price=price,author=author,img=img,Desc=Desc,title=title)
        Book.save()
        messages.success(request, "Data has been Added successfully!")
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're not Autherized to add Records :/"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, request))


def delete(req,id):
    ack=False
    if(req.user.is_superuser):
        obj=models.Books.objects.get(id=id)
        obj.delete()
        # ack=True
        # context={
        #     'ack': ack
        # }
        # return render(req, 'index.html', context)
        # messages.add_message(req, messages.INFO, 'True')
        messages.error(req, "Data has been Deleted successfully!")
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're not Autherized to Delete :/"
        context = {
            'msg': msg,
            'ack': ack
        }
        messages.add_message(req, messages.INFO, 'False')
        return HttpResponse(template.render(context, req))
        return render(request, 'test.html', context)


def update(req,id):
    if(req.user.is_superuser):
        mybook = models.Books.objects.get(id=id)
        template = loader.get_template('edit.html')
        context = {
            'mybook': mybook,
        }
        return HttpResponse(template.render(context, req))
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're not Autherized to update Records :/"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, req))

def updaterow(request,id):
    if(request.user.is_superuser):
        price = request.POST['price']
        author = request.POST['author']
        img = request.POST['img']
        Desc = request.POST['Desc']
        title = request.POST['title']

        Book = models.Books.objects.get(id=id)
        Book.price = price
        Book.author = author
        Book.img = img
        Book.Desc = Desc
        Book.title = title

        Book.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're not Autherized to update Records :/"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, request))


# @login_required
def user_logout(request):
    if(request.user.is_authenticated):
        logout(request)
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
    else:
        template = loader.get_template('sorry.html')
        msg="you aren't logged in yet to log out 7abib :)"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, request))

# @login_required
# def Special(request):
#     return HttpResponse("U're logged in !")

# Create your views here.
def registerPost(request):
    if(not request.user.is_authenticated):
            # Get info from "both" forms
            # It appears as one form to the user on the .html page
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)

            # Check to see both forms are valid
            if user_form.is_valid() and profile_form.is_valid():

                # Save User Form to Database
                user = user_form.save()

                # Hash the password
                user.set_password(user.password)

                # Update with Hashed password
                user.save()

                # Now we deal with the extra info!

                # Can't commit yet because we still need to manipulate
                profile = profile_form.save(commit=False)

                # Set One to One relationship between
                # UserForm and UserProfileInfoForm
                profile.user = user

                # Check if they provided a profile picture
                if 'profile_pic' in request.FILES:
                    print('found it')
                    # If yes, then grab it from the POST form reply
                    profile.profile_pic = request.FILES['profile_pic']

                # Now save model
                profile_form.instance.is_staff=False
                user_form.instance.is_staff=False
                profile.save()
                username = request.POST.get('username')
                password = request.POST.get('password')
                return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
            else:
                # One of the forms was invalid if this else gets called.
                print(user_form.errors,profile_form.errors)
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're Already Registered :/"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, request))

def registerGet(request):
    if(not request.user.is_authenticated):
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        # This is the render and context dictionary to feed
        # back to the registration.html file page.
        return render(request,'Regestration/reg.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            })
    else:
        template = loader.get_template('sorry.html')
        msg="sorry U're Already Registered :/"
        context = {
            'msg': msg,
        }
        return HttpResponse(template.render(context, request))

# 2b addded later

# def profile_details(req):
#     pro=models.UserProfileInfo.objects.get(id=req.user.id)
#     usr=models.User.objects.get(id=req.user.id)
#     con={
#         'pro':pro,
#         'usr':usr
#     }
#     template = loader.get_template('profile.html')
#     return HttpResponse(template.render(con, req))



# def register(request):
#     if(not request.user.is_authenticated):
    
#         registered = False

#         if request.method == 'POST':

#             # Get info from "both" forms
#             # It appears as one form to the user on the .html page
#             user_form = UserForm(data=request.POST)
#             profile_form = UserProfileInfoForm(data=request.POST)

#             # Check to see both forms are valid
#             if user_form.is_valid() and profile_form.is_valid():

#                 # Save User Form to Database
#                 user = user_form.save()

#                 # Hash the password
#                 user.set_password(user.password)

#                 # Update with Hashed password
#                 user.save()

#                 # Now we deal with the extra info!

#                 # Can't commit yet because we still need to manipulate
#                 profile = profile_form.save(commit=False)

#                 # Set One to One relationship between
#                 # UserForm and UserProfileInfoForm
#                 profile.user = user

#                 # Check if they provided a profile picture
#                 if 'profile_pic' in request.FILES:
#                     print('found it')
#                     # If yes, then grab it from the POST form reply
#                     profile.profile_pic = request.FILES['profile_pic']

#                 # Now save model
#                 profile_form.instance.is_staff=False
#                 user_form.instance.is_staff=False
#                 profile.save()

#                 # Registration Successful!
#                 registered = True

#             else:
#                 # One of the forms was invalid if this else gets called.
#                 print(user_form.errors,profile_form.errors)

#         else:
#             # Was not an HTTP post so we just render the forms as blank.
#             user_form = UserForm()
#             profile_form = UserProfileInfoForm()
#         # This is the render and context dictionary to feed
#         # back to the registration.html file page.
#         return render(request,'Regestration/reg.html',
#                             {'user_form':user_form,
#                             'profile_form':profile_form,
#                             'registered':registered})
#     else:
#         template = loader.get_template('sorry.html')
#         msg="sorry U're Already Registered :/"
#         context = {
#             'msg': msg,
#         }
#         return HttpResponse(template.render(context, request))

def user_login(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect('http://127.0.0.1:8000/FSApp/')
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect('http://127.0.0.1:8000/FSApp/')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            messages.error(request, "Invalid login details supplied.")
            return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/user_login/")
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            # return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'Regestration/login.html', {})


def book_details(req,id):
    book_details=models.Books.objects.get(id=id)

     #check if the book u want to add to the cart is already exists to that user, if so, Make the Book in the Frontend-side Appears as Add2Cart/InCart
    bookincart=models.CartBooks.objects.filter(
        Q(book_id=id),
        Q(user_id=req.user.id)
    )
    template = loader.get_template('book_details.html')
    context = {
        'book_details': book_details,
        'bookincart':bookincart,
    }
    return HttpResponse(template.render(context, req))

# this controller returns to the same page of the current book details, kinda dumb solution (cause i'm lazy asf), but i'm gonna figure how to return to the same current page (Dynamically) later.
# @login_required
def CartBooksPost_ToBD(req,id):
    if(req.user.is_authenticated):
            book=models.Books.objects.get(id=id)
            user=models.User.objects.get(id=req.user.id)

            #check if the book u want to add to the cart is already exists to that user, if so, just increase the qunatity, else add the book to the cart.
            bookincart=models.CartBooks.objects.filter(
                Q(book_id=id),
                Q(user_id=req.user.id)
            )
            cb=models.CartBooks()
            #if the length is not zero, that means there already exist the book u want to add
            if len(bookincart) != 0 :
                bookincart[0].quantity=bookincart[0].quantity + 1
                bookincart[0].save()
            #the length == 0, which means the book is brand-new to add.
            else:
                cb.book=book
                cb.user=user
                cb.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/book_details/{id}".format(id=id))
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/user_login/".format(id=id)) 
# @login_required
def CartBooksPost(req,id):
    if(req.user.is_authenticated):
        book=models.Books.objects.get(id=id)
        user=models.User.objects.get(id=req.user.id)

        #check if the book u want to add to the cart is already exists to that user, if so, just increase the qunatity, else add the book to the cart.
        bookincart=models.CartBooks.objects.filter(
            Q(book_id=id),
            Q(user_id=req.user.id)
        )
        cb=models.CartBooks()
        #if the length is not zero, that means there already exist the book u want to add
        if len(bookincart) != 0 :
            bookincart[0].quantity=bookincart[0].quantity + 1
            bookincart[0].save()
        #the length == 0, which means the book is brand-new to add.
        else:
            cb.book=book
            cb.user=user
            cb.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/user_login/".format(id=id))


# need to make the logic and filteration here, not in the Templates !
# gonna do it later

# @login_required
def cart(req):
    if(req.user.is_authenticated):
        booksincart = models.CartBooks.objects.filter(
            Q(user_id=req.user.id)
        )
        # books=models.Books.objects.filter(
        #     books_id_in=booksincart.book_id
        # )
        cbooks=list()
        books=models.Books.objects.all()
        total=0
        for a in books:
            for b in booksincart:
                if(a.id==b.book_id):
                    total = total + int(a.price) * int(b.quantity)
                    cbooks.append(a)
        
        # queryset = models.Books.objects.select_related(
        # 'CartBooks'
        # ).filter(CartBooks__user_id__icontains=req.user.id)
        # # .filter(
        # #     Q(user_id=req.user.id)
        # # )
        templ=loader.get_template("cart.html")
        page = req.GET.get('page', 1)
        con = {
            'booksincart' :booksincart,
            # 'UserItems':UserItems,
            'cbooks':cbooks,
            'total':total,
            }
        return HttpResponse(templ.render(con,req))
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/user_login/".format(id=id))
        # i must add A redrecting, so as soon as user logged in, he will return to the page he was before he was authenticated 

##Custome Filter to convert String to int in the Cart Template

from django import template
register = template.Library()

@register.filter()
def to_int(value):
    return int(value)


def deleteItem(req,id):
    obj=models.CartBooks.objects.get(id=id)
    obj.delete()
    messages.error(req, "Data has been Deleted successfully!")
    return HttpResponseRedirect("http://127.0.0.1:8000/FSApp/cart")

