from django.contrib import admin

# Register your models here.
from .models import ToDo, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(ToDo, PostAdmin)
admin.site.register(Comment)
