from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello_view import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^greet/$', hello),
    url(r'^error/$', error),
    url(r'^getip/$', getIP),
    url(r'^form_test/$', form_test),
    url(r'^formdata/$', greet_with_form_data),
    url(r'^reversed/(?P<bit>.*)/$', reverse_url_bit),
    url(r'^sum/(\d+)/(\d+)/$', url_sum),
    url(r'^show_metadata/$', show_metadata),
    url(r'^show_metadata_with_load/$', show_metadata_with_load),
    url(r'^show_metadata_with_load/$', show_metadata_with_load),
)
