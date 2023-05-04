# Generated by Django 4.1.3 on 2023-05-03 15:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_postpoem_post_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=50)),
                ('story_content', models.TextField(validators=[django.core.validators.MinLengthValidator(800)])),
                ('story_summary', models.TextField(max_length=500)),
                ('story_slug', models.SlugField(max_length=100, unique=True)),
                ('story_cover_photo', models.ImageField(upload_to='story_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]