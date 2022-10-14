from django.urls import include, re_path
#from rest_framework.documentation import include_docs_urls

API_TITLE = 'Youtube playlist download'
API_DESCRIPTION = 'A Web API for download playlist\'s youtube.'

urlpatterns = [
    re_path(r'^', include('playlist.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    re_path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
