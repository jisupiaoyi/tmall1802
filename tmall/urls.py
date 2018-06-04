from django.conf.urls import url
import xadmin

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('admin/', xadmin.site.urls),
]
