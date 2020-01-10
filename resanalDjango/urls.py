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
    url(r'^analize/',views.analysis),
    url(r'^results/',views.ResultsView.as_view()),
    url(r'^ranalysis/',views.AnalizeApi.as_view()),
    url(r'^getfcd/',views.GetFCD.as_view()),
    url(r'^secfcd/',views.FCD_Section.as_view()),
    url(r'^totalfcd/',views.TotalFCD.as_view()),
    url(r'^genXL/',views.GenXL.as_view()),
    url(r'^genXLDash/',views.genXLDash.as_view()),
    url(r'^genallXL/',views.getAllXL.as_view()),
    url(r'^wake/',views.Wake.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)