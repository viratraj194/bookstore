from django.shortcuts import redirect, render,get_object_or_404
from posts.forms import CategoryForm, PostPoemForm, PostStoryForm
from posts.models import Category, PostPoem, PostStory
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib import messages





@login_required(login_url='login')
def add_posts(request):
    categorys = Category.objects.filter(user = request.user)
    poems = PostPoem.objects.filter(user = request.user)
    storys = PostStory.objects.filter(user = request.user)

    context = {
        'categorys':categorys,
        'poems':poems,
        'storys':storys
    }
    return render(request,'posts/add_posts.html',context)

@login_required(login_url='login')
def add_poem_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_name = category_form.cleaned_data['category_name']
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
            post.save()
            post.poem_slug = slugify(post_title) + '-' + str(post.id)

            print(post.id)
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



def list_poems(request):
    # categories = Category.objects.all()
    poems = PostPoem.objects.all()   
    context = {
        'poems':poems,
        # 'post_count':post_count
    }
    return render(request,'posts/list_poems.html',context)

@login_required(login_url='login')
def post_story(request):
    if request.method == 'POST':
        form = PostStoryForm(request.POST,request.FILES)
        if form.is_valid():
            story_title = form.cleaned_data['story_title']
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            post.story_slug = slugify(story_title) + '-' + str(post.id)          
            post.save()
            messages.success(request,'Story posted successfully'.title())
            return redirect('dashboard')
        else:
            print(form.errors)
    
    else:
        form = PostStoryForm()
    context = {
        'form':form
    }
    return render(request,'posts/post_story.html',context)




def list_storys(request):
    storys = PostStory.objects.all()
    context = {
        'storys':storys
    }
    return render(request,'posts/list_storys.html',context)

@login_required(login_url='login')
def post_poem_edit(request,pk=None):
    poem = get_object_or_404(PostPoem,pk=pk)
    if request.method == 'POST':
        form = PostPoemForm(request.POST,request.FILES,instance=poem)
        if form.is_valid():
            post_title = form.cleaned_data['post_title']
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            post.poem_slug = slugify(post_title) + '-' + str(post.id)

            print(post.id)
            post.save()
            messages.success(request,'Your Poem is successfully Updated'.title())
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = PostPoemForm(instance=poem)
    context = {
        'form':form,
        'poem':poem
    }
    return render(request,'posts/post_poem_edit.html',context)

def post_poem_delete(request,pk=None):
    poem = get_object_or_404(PostPoem,pk=pk)
    poem.delete()
    messages.success(request,'post deleted'.title())
    return redirect('dashboard')

def poem_details(request,poem_slug):
    poem = get_object_or_404(PostPoem,poem_slug=poem_slug)
    context = {
        'poem':poem
    }
    return render(request,'posts/poem_details.html',context)


def post_story_edit(request,pk=None):
    story = get_object_or_404(PostStory,pk=pk)
    if request.method == 'POST':
        form = PostStoryForm(request.POST,request.FILES,instance=story)
        if form.is_valid():
            story_title = form.cleaned_data['story_title']
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            post.story_slug = slugify(story_title) + '-' + str(post.id)          
            post.save()
            messages.success(request,'Story Updated successfully'.title())
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = PostStoryForm(instance=story)

        context = {
            'form':form,
            'story':story
        }
    return render(request,'posts/post_story_edit.html',context)


def post_story_delete(request,pk=None):
    story = get_object_or_404(PostStory,pk=pk)
    story.delete()
    messages.success(request,'Story deleted'.title())
    return redirect('add_posts')

def story_details(request,story_slug):
    story = get_object_or_404(PostStory,story_slug=story_slug)
    context = {
        'story':story
    }
    return render(request,'posts/story_details.html',context)


def all_category(request):
    categorys =  Category.objects.all()
    poems = PostPoem.objects.all()[:5]
    storys = PostStory.objects.all()[:5]
    context = {
        'poems':poems,
        'storys':storys,
        'categorys':categorys
    }

    return render(request,'posts/all_category.html',context)