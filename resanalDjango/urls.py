from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from resanal import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/', views.ResultList.as_view()),
    url(r'^json1/', views.FetchList.as_view()),
    url(r'^json2/', views.MultiAPIView.as_view()),
    url(r'^crawl/',views.crawl),
    url(r'^results/',views.ResultsView.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)