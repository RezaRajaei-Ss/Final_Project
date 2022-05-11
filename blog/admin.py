from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Article , Category

#admin header change 
admin.site.site_header = "پنل مدیریت وبسایت"

# Register your models here.
admin.site.disable_action('delete_selected')


# @admin.action(description='انتشار کردن مقالات انتخاب شده')
# def make_published(modeladmin, request, queryset):
# 	queryset.update(status='p')

@admin.action(description='انتشار کردن مقالات انتخاب شده')
def make_published(self, request, queryset):
		updated = queryset.update(status='p')
		self.message_user(request, ngettext(
			'%d مقاله منتشر شد',
			'%d مقاله منتشر شد',
			updated,
		) % updated, messages.SUCCESS)


# @admin.action(description='پیشنویس کردن مقالات انتخاب شده')
# def make_draft(modeladmin, request, queryset):
# 	queryset.update(status='d')


@admin.action(description='پیشنویس کردن مقالات انتخاب شده')
def make_draft(self, request, queryset):
		updated = queryset.update(status='d')
		self.message_user(request, ngettext(
			'%d مقاله پیشنویس شد',
			'%d مقاله پیشنویس شد',
			updated,
		) % updated, messages.SUCCESS)



class CategoryAdmin(admin.ModelAdmin):
	list_display = ('position', 'title', 'slug', 'parent', 'status')
	list_filter = (['status'])
	search_fields =('title','slug')
	prepopulated_fields= {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug', 'author','publish','status','category_to_str', 'is_spical', 'thumbnail_tag')
	list_filter = ('publish', 'status', 'author')
	search_fields =('title','description')
	prepopulated_fields= {'slug': ('title',)}
	ordering = ['status','-publish']
	actions = [make_published, make_draft]

   
admin.site.register(Article, ArticleAdmin)