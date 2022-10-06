from django.contrib import admin
from .models import Tweets

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    exclude = ('time',)
admin.site.register(Tweets, TweetAdmin)