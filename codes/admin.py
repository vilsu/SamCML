from django.contrib import admin
from SamCML.codes.models import Code, Author    # do not show revions 

class AuthorAdmin(admin.ModelAdmin):
        list_display = ('name', 'email',)
        search_fields = ('name',)

class CodeAdmin(admin.ModelAdmin):
        list_display = ('title', 'body', 'pub_date',)
        list_filter = ('pub_date',)
        pub_date_hierarchy = ('pub_date',)
        ordering = ('-pub_date',)
        fields = ('title', 'authors',)  # exclude pub_pub_date 
        filter_horizontal = ('authors',)    
        #raw_id_fields = ('title',)

admin.site.register(Code, CodeAdmin)
admin.site.register(Author, AuthorAdmin)
