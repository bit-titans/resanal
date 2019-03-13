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
<<<<<<< HEAD
    url(r'^analize/',views.analysis),
    url(r'^results/',views.ResultsView.as_view()),
    url(r'^ranalysis/',views.AnalizeApi.as_view()),
=======
    url(r'^results/',views.ResultsView.as_view()),
>>>>>>> 251e90d840ba34262f62b20c27ec7291a10773b9
]

#urlpatterns = format_suffix_patterns(urlpatterns)