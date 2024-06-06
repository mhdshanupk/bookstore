from django.contrib import admin
from . models import Book,Reviews

class BookAdmin(admin.ModelAdmin):
    list_display=('id','image','name','price','type')
    list_filter=['type']


class ReviewsAdmin(admin.ModelAdmin):
    list_display=('id','fk_book','fk_user','reviews' )
    list_filter=['fk_book']


admin.site.register(Book, BookAdmin)
admin.site.register(Reviews,ReviewsAdmin)