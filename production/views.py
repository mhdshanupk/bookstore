from django.shortcuts import render,HttpResponse,redirect
from . models import Book,Reviews
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def user_register(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        user_name=request.POST.get('username')
        pword=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if pword == confirm_password:


            User.objects.create_user(
                email=email,
                username=user_name,
                password=pword,
        )
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        pword=request.POST.get('password')
        user=authenticate(username=uname, password=pword)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home')
            return redirect('user_home',id=user.id)
        return HttpResponse('Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
        books=Book.objects.all()
        if request.method == 'POST':
            temp_type=request.POST.get('type')
            temp_title=request.POST.get('title')
            if temp_type == '':
                books=Book.objects.all()
            else:
                books=Book.objects.filter(type=temp_type)
            if temp_title:
                books=Book.objects.filter(title_icontains=temp_title)
        return render(request,'home.html',{'book1':books})
@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        Book_name=request.POST.get('name')
        Book_author=request.POST.get('author')
        Book_cover=request.FILES.get('photo')
        Book_Category=request.POST.get('category')
        Book_price=request.POST.get('price')
        is_pub=request.POST.get('check')

        Book.objects.create(
            name=Book_name,
            author=Book_author,
            image=Book_cover,
            type=Book_Category,
            price=Book_price,
            is_published=is_pub
            )
        return redirect('home')
    return render(request,'add_book.html')


@login_required(login_url='login')
def book_view(request,id):
    book=Book.objects.get(id=id)
    review=Reviews.objects.filter(fk_book=id)
    current_user=request.user
    if request.method == 'POST':
        temp_comment=request.POST.get('comments')
        Reviews.objects.create(
            fk_user=current_user,
            fk_book=book,
            reviews=temp_comment,
        )
    return render(request,'book_view.html',{'books':book,'review':review})



@login_required(login_url='login')
def book_edit(request,id):
    book1=Book.objects.get(id=id)
    if request.method == 'POST':
        Book_name=request.POST.get('name')
        Book_author=request.POST.get('author')
        Book_cover=request.POST.FILES('image')
        Book_price=request.POST.get('price')
        book1.name=Book_name
        book1.author=Book_author
        book1.image=Book_cover
        book1.price=Book_price
        book1.save()
        return redirect('home')
    return render(request,'book_edit.html',{'book':book1})
@login_required(login_url='login')
def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('home')
@login_required(login_url='login')
def user_home(request,id):
    view1=Book.objects.all()
    return render(request,'user_home.html',{'views':view1})
@login_required(login_url='login')
def review_edit(request,id):
        data=Reviews.objects.get(id=id)
        book=data.fk_book
        if request.method == 'POST':
            temp_comment=request.POST.get('comments')
            data.reviews=temp_comment
            data.save()
            return redirect('book_view',id=book.id)
        return render(request,'review_edit.html',{'data':data})
@login_required(login_url='login')
def review_delete(request,id):
    data=Reviews.objects.get(id=id)
    book=data.fk_book
    data.delete()
    return redirect('book_view',id=book.id)
@login_required(login_url='login')
def publish(request,id):
    book=Book.objects.get(id=id)
    if book.is_published==True:
        book.is_published=False
    else:
        book.is_published=True
    book.save()
    return redirect('home')

