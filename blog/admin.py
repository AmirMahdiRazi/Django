from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

# @admin.regiter(Post)


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    list_display = ('title', 'author', 'counted_views',
                    'status', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    # ordering = ['-created_date']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
