from django.contrib import admin
from . import models

class ArcticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'date_created', 'user_name')
    search_fields = ('title', 'category__name', 'user_name')
    list_filter = ('category', 'date_created')
    list_display_links = ('title','category', 'date_created', 'user_name')
    

admin.site.register(models.ArticleCategory)
admin.site.register(models.Arcticle,ArcticleAdmin)