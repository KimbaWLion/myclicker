from django.conf.urls import patterns, url
from milestone import views


urlpatterns = patterns('',
	# Login/logout
	('^login/$', 'django.contrib.auth.views.login'),
	('^logout/$', views.logout_page),
	
	# Registration
    (r'^register/', views.register),
	
	('^student/$', views.student),
#	(r'^student/stylesheets/base.css$', views.student_base),
#	(r'^student/stylesheets/skeleton.css$', views.student_skeleton),
#	(r'^student/stylesheets/layout.css$', views.student_layout),
	('^professor/$', views.professor),
	('^professor/update.xml$', views.update_xml),
	('^student/update.xml$', views.update_xml),
#	(r'^professor/stylesheets/base.css$', views.professor_base),
#	(r'^professor/stylesheets/skeleton.css$', views.professor_skeleton),
#	(r'^professor/stylesheets/layout.css$', views.professor_layout),
#	(r'^professor/images/favicon.ico$', views.professor_icon),
	('^hello/$', views.hello),
	('^javascript/$', views.trial),
	('^mile0/$', views.noxml),
	('^milestone/$', views.xml),
	('^milestone/update.xml$', views.update_xml),
	('^update$', views.update_xml),
	('^database/$', views.database),
)