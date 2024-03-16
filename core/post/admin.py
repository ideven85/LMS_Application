from django.contrib import admin

from core.post.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'author','body'[:20],'publish' ]
    list_max_show_all = 20
    list_filter = ['title']
