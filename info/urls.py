from django.urls import path

from info.views import (
    SubmitApplicationView,
    StaffView,
    ProjectsView,
    TypeOfWorkView,
    OurPartnerView,
    EventLentView,
    FreeVacancyView,
    QuestionAnswerView,
    GetConsultView,
    AdView,
    ConnectionView,
    AboutUsView,
    WhatWeUseView
)
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('feedback', FeedbackView)
urlpatterns =[
    path('submitapplication/', SubmitApplicationView.as_view()),
    path('staff/', StaffView.as_view({'get': 'list'})),
    path('projects/', ProjectsView.as_view({'get': 'list'})),
    path('typeofwork/', TypeOfWorkView.as_view({'get': 'list'})),
    path('ourpartner/', OurPartnerView.as_view({'get': 'list'})),
    path('eventlent/', EventLentView.as_view({'get': 'list'})),
    path('freevacancy/', FreeVacancyView.as_view({'get': 'list'})),
    path('questionanswer/', QuestionAnswerView.as_view({'get': 'list'})),
    path('getconsult/', GetConsultView.as_view()),
    path('ad/', AdView.as_view({'get': 'list'})),
    path('connection/', ConnectionView.as_view({'get': 'list'})),
    path('about_us/', AboutUsView.as_view({'get': 'list'})),
    path('what_we_use/', WhatWeUseView.as_view({'get': 'list'})),
]
