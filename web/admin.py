from django.contrib import admin
from web.models import Next, Author

# Register your models here.

# admin.site.register(Next)
# admin.site.register(Author)

@admin.register(Next)
class NextAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'date_created']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['prefix', 'first_name', 'last_name', 'dob']