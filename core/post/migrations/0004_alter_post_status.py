# Generated by Django 5.0.3 on 2024-03-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0003_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PF', 'Published'), ('DF', 'Draft')], default='DF', max_length=2),
        ),
    ]
