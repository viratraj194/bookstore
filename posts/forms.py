from django import forms
from. models import Category,PostPoem, PostStory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class PostPoemForm(forms.ModelForm):
    cover_image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-50 '}))
   
    class Meta:
        model = PostPoem
        fields = ['category','poem_content','post_title','post_overview','author_name','cover_image']


class PostStoryForm(forms.ModelForm):
    story_cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-50 '}))
    class Meta:
        model = PostStory
        fields = ('category','story_title','story_content','story_summary','author_name','story_cover_photo')
