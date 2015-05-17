# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from django.core.content_processors import csrf


from .models import Post
from .forms import PostForm
from .models import Userlog
from .forms import UserlogForm
from .forms import UserForm


    
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
   # if 'save' in request.POST:
    if request.method == "POST":
        #save button
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            print "mish"
            return HttpResponseRedirect(reverse(post_detail, kwargs={'pk': post.pk}))
        
        #upload button    
        
            
    else:
        form = PostForm()

    # Load documents for the list page
    #documents = Document.objects.all()
    #documents = Document.objects.order_by('documents/%Y/%m/%d').first()
    #documents = Document.objects.latest('pub_date')
        
   # return render(request, 'blog/post_edit.html', {'form': form})
    return render_to_response(
    'blog/post_edit.html',
    {'form': form},
    context_instance=RequestContext(request)
    )
        
    

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return HttpResponseRedirect(reverse(post_detail, kwargs={'pk': pk}))

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse(post_list))
    

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse(post_detail, kwargs={'pk': post.pk}))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    
# mish v1 upload image    
def list(request):
    # Handle file upload
   

    # Load documents for the list page

    # Render list page with the documents and the form
    return render_to_response(
        'blog/post_edit.html',
        context_instance=RequestContext(request)
    )
    
def Home(request):
    #posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    #return render(request, 'blog/post_draft_list.html', {'posts': posts}) 
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    users = User.objects.filter()
    loginform = UserForm(request.POST)
    userlog = UserlogForm(request.POST)
    
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    
    
    usernameLog = request.POST.get('usernameLog', 'X')
    passwordLog = request.POST.get('passwordLog', 'X')
    
    
    
    
    
    if request.method == "POST":
        
        
        #login
        
        if usernameLog and passwordLog:
            
            
            user = authenticate(username=usernameLog, password=passwordLog)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    print "User is valid, active and authenticated"
                else:
                    print ("The account has been disabled!")
            else:
                logout(request)
                print "mish~~"
                # the authentication system was unable to verify the username and password
                print ("The password was incorrect.")
                
        #else:
            
            
            
        #register
        if username and password and email:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
            if user.is_active:
                    login(request, user)
                    print "User is valid, active and authenticated"
            else:
                print ("The account has been disabled!")
            return HttpResponseRedirect(".")   
        
     
        
        #save button
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            return HttpResponseRedirect(".")   
            #return HttpResponseRedirect(reverse(post_detail, kwargs={'pk': post.pk}))
            
            
        
        
        #upload button    
        # formUpload = DocumentForm(request.POST, request.FILES)
        # if formUpload.is_valid():
        #     newdoc2 = Document(docfile = request.FILES['docfile'])
        #     newdoc2.save()
        #     print "mish22"
        #     # Redirect to the document list after POST
        #     return HttpResponseRedirect(".")    
            
    else:
        form = PostForm()
       #Userlog = UserlogForm()
        userlog = UserlogForm()
        loginform = UserForm()
        #formUpload = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()
    #documents = Document.objects.order_by('documents/%Y/%m/%d').first()
    #documents = Document.objects.latest('pub_date')
    #documents = Document.objects.order_by('id').reverse()[:1]
    
    # c={}
    # c.update(csrf(request))
    
    
    # if user is not None:
    #     auth.login(request, user)
    #     return render_to_response('login.html',c)
        
    # else:
    #     return HttpResponseRedirect('/accounts/invalid')
 
 
    return render_to_response(
    'blog/HomePage.html',
    {'userlog': userlog, 'loginform': loginform, 'posts': posts, 'form': form, 'users': users},
    # { 'posts': posts, 'form': form},
    context_instance=RequestContext(request)
    )