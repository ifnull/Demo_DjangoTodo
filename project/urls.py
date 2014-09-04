from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from tastypie import api
import todo.api as todo_resources


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Homepage
    (r'^$', TemplateView.as_view(template_name='index.html')),
)

# Setup v1 API
v1_api = api.Api(api_name='v1')
v1_api.register(
    todo_resources.TodoResource()
)
urlpatterns += patterns('', (r'^api/', include(v1_api.urls)))

#used to show static assets out of the collected-static
if getattr(settings, 'SERVE_STATIC', False) and settings.SERVE_STATIC:
    urlpatterns += patterns(
        '',
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
        url(r'^uploads/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    )
