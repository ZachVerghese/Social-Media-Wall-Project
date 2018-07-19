from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.login),
    url(r'^process_login$', views.process_login),
    url(r'^process_registration$', views.process_registration),
    url(r'^wall$',views.index),
    url(r'^create_message$', views.create_message),
    url(r'^create_comment$', views.create_comment),
    url(r'^delete/(?P<post_id>\d+)$',views.delete)
]

# 1. login screen
# 2. process registration
# 3. process login
# 4. home page
# 5. process add message
# 6. process add comment