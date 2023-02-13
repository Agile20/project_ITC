from rest_framework import generics, viewsets 
from django.conf import settings

from info.serializers import *


class SubmitApplicationView(generics.CreateAPIView):
    queryset = SubmitApplication.objects.all() 
    serializer_class = SubmitApplicationSerializer
        

class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


class ProjectsView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    

class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


class TypeOfWorkView(viewsets.ModelViewSet):
    queryset = TypeOfWork.objects.all()
    serializer_class = TypeOfWorkSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response

class OurPartnerView(viewsets.ModelViewSet):
    queryset = OurPartner.objects.all()
    serializer_class = OurPartnerSerializer


class EventLentView(viewsets.ModelViewSet):
    queryset = EventLent.objects.all()
    serializer_class = EventLentSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


class FreeVacancyView(viewsets.ModelViewSet):
    queryset = FreeVacancy.objects.all()
    serializer_class = FreeVacancySerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


class ConnectionView(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class QuestionAnswerView(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


# class FeedbackView(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer
#     http_method_names = ['get', 'post']


class GetConsultView(generics.CreateAPIView):
    queryset = GetConsult.objects.all()
    serializer_class = GetConsultSerializer


class AdView(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class WhatWeUseView(viewsets.ModelViewSet):
    queryset = WhatWeUse.objects.all()
    serializer_class = WhatWeUseSerializer
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        languages = request.LANGUAGE_CODE
        response.data['languages'] = languages
        return response


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

