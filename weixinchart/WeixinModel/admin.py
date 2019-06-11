from django.contrib import admin
from WeixinModel.models import Weixin,Contact,Tag
 
# Register your models here.
admin.site.register([Weixin, Contact, Tag])

