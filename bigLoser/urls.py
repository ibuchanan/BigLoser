from django.conf.urls import patterns, url, include
from django.contrib import admin
from bigLoser import views

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'weight/add/$', views.WeightCreate.as_view(), name='weight_add'),
    url(r'^(?P<user_id>\d+)/report/$', views.render_chart, name='render_chart'),
    url(r'^(?P<user_id>\d+)/$', views.user_homepage, name = 'user_homepage')
)

urlpatterns += patterns(
	'django.contrib.auth.views',

	url(r'^login/$', 'login',
		{'template_name': 'login.html'},
		name='bigLoser_login'),

	url(r'^logout/$', 'logout',
		{'next_page': 'index'},
		name='bigLoser_logout'),
	)