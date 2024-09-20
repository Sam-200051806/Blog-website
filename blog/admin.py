from django.contrib import admin
from .models import Author,Tag,Post
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tag","date" ,)
    list_display = ("author","date","title", )
    prepopulated_fields = {"slug" : ("title",)}
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)