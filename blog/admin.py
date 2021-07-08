from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'short_body', 'created_on', 'last_modified')

    # def show_category(self, obj):
    #     return "\n".join([c.categories for c in obj.categories_set.all()])

class CategoryAdmin(admin.ModelAdmin):
     pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)