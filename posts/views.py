from django.shortcuts import redirect, render,get_object_or_404
from posts.forms import CategoryForm, PostPoemForm
from posts.models import Category
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib import messages


@login_required(login_url='login')
def add_posts(request):
    categorys = Category.objects.filter(user = request.user)
    context = {
        'categorys':categorys
    }
    return render(request,'posts/add_posts.html',context)

@login_required(login_url='login')
def add_poem_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.c['category_name']
            category = category_form.save(commit=False)
            category.user = request.user

            category.save()  # here the category id will be generated
            category.slug = slugify(category_name) + '-' + str(category.id)  # chicken-15
            category.save()
            messages.success(request, 'Category Added successfully'.title())

            return redirect('add_posts')
        else:
            messages.error(request,category_form.errors)
            
    else:
        category_form = CategoryForm()
    context = {
        'category_form':category_form,
    }
    return render(request,'posts/add_poem_category.html',context)


@login_required(login_url='login')
def edit_category(request,pk=None):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            category.slug = slugify(category_name) + '-' + str(category.id)
            category.save()
            messages.success(request, 'Category updated successfully'.title())
            return redirect('add_posts')
        else:
            messages.error(request,'error')
            print(form.errors)
            return redirect('add_posts')
    else:
        form = CategoryForm(instance=category)    
    context = {
        'form':form,
        'category':category
    }
    return render(request,'posts/edit_category.html',context)


@login_required(login_url='login')
def delete_category(request,pk=None):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    messages.success(request,'Category deleted successfully'.title())
    return redirect('add_posts')


def post_poem(request):
    if request.method == 'POST':
        form = PostPoemForm(request.POST,request.FILES)
        if form.is_valid():
            post_title = form.cleaned_data['post_title']
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post_title) + '-' + str(post.id)
            post.save()
            messages.success(request,'Your Poem is successfully post'.title())
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = PostPoemForm()
    context = {
        'form':form
    }
    return render(request,'posts/post_poem.html',context)