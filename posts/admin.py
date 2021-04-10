from django.contrib import admin
from .models import Post,PostComment
# Register your models here.
admin.site.register(PostComment)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
