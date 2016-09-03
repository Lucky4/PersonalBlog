from django.contrib import admin
from PersonalBlog_app.models import User, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(User)
admin.site.register(Post, PostAdmin)

