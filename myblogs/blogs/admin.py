from django.contrib import admin
from .models import Author, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'date_created', 'author')  
    fields = ('title', 'content', 'date_created','author')  
    readonly_fields = ('date_created',)  
    search_fields = ('title','content','author__user__username')

    def short_content(self, obj):
        return obj.content[:20] + '...' if len(obj.content) > 20 else obj.content
    short_content.short_description = 'Content'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_posts')  
    fields = ('user',)
    search_fields = ('user__username',)
    def list_posts(self, obj): 
        post_titles = [post.title for post in obj.post_set.all()]
        return ", ".join(post_titles[:3])
    list_posts.short_description = 'Posts'  


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)  

# Register your models here.
