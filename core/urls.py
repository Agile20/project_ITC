
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('info.urls')),
    path('auth/', include('rest_framework.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

# urlpatterns += i18n_patterns(
#     path('', include('info.urls')),
#     path('about_us/', include('about_us.urls')),
#     path('what_we_use/', include('what_we_use.urls')),
#     path('staff/', include('staff.urls')),
#     path('typeofwork/', include('typeofwork.urls')),
#     path('eventlent/', include('eventlent.urls')),
#     path('freevacancy/', include('freevacancy.urls')),
#     path('questionanswer/', include('questionanswer.urls')),
# )

urlpatterns += i18n_patterns(
    path('', include('info.urls')),
)


urlpatterns += i18n_patterns(

)


urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
