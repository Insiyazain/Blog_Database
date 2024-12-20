from django.contrib import admin
from .models import Tag,Author,Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("title","date","author",)
    list_filter=("tag","date","author",)
    prepopulated_fields={"slug":("title",)}


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)