from django.contrib import admin
from .models import *

# Register your models here.

class userFilter(admin.SimpleListFilter):
    title = u'字符'
    parameter_name = 'char'

    def lookups(self, request, model_admin):
        return (
            ('0', u'abcd'),
            ('1', u'123456'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(userName='abcd')
        elif self.value() == '1':
            return queryset.filter(userName='123456')

class charFilter(admin.SimpleListFilter):
    title = u'字符'
    parameter_name = 'char'

    def lookups(self, request, model_admin):
        return (
            ('0', u'abcd'),
            ('1', u'123456'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(author='abcd')
        elif self.value() == '1':
            return queryset.filter(author='123456')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('userName', 'describe', 'password', 'loginTimes',)

    search_fields = ('userName',)

    list_filter = ('userName', userFilter)


class PassageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'creationTime', 'changeTime',)

    search_fields = ('title',)

    list_filter = ('title', charFilter)

class RepliesAdmin(admin.ModelAdmin):
    list_display = ('passage', 'author', 'replyTime', 'content',)

    search_fields = ('content',)

    list_filter = ('content', charFilter)


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Passage, PassageAdmin)
admin.site.register(Replies, RepliesAdmin)

