from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Category, Article, ArticleImage
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),
        }),
    )

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('title', 'image'),
        }),
    )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    list_filter = ('category',)  
    inlines = [ArticleImageInline]
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    
    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description', 'main_page', 'category'),  
        }),
        (u'Додатково', {
            'classes': ('grp-collapse grp-collapse-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()

admin.site.register(Article, ArticleAdmin)