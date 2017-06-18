from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^json_workbook/', 'pyxform_interface.views.json_workbook'),
    url(r'^$', 'pyxform_interface.views.index'),
    (r'^downloads/(?P<path>.*)$', 'pyxform_interface.views.serve_file'),
]

urlpatterns += staticfiles_urlpatterns()
