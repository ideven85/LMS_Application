# Generated by Django 5.0.3 on 2024-03-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0002_alter_post_options_post_publish_and_more'),
        ('core_user', '0003_user_posts_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to='core_post.post'),
        ),
    ]
