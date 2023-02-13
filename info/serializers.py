from rest_framework import serializers

from info.models import *
from info.telegram_sender import send_message_telebot

class SubmitApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitApplication
        fields = (
            'id', 'name', 'email', 'resume',
        )
    def create(self, validated_data):
        text = f'Новый отклик на вакнсию:\nИмя: {validated_data["name"]}\nEmail: {validated_data["email"]}\nРезюме: {validated_data["resume"]}'
        send_message_telebot(text)
        return super().create(validated_data)


class GetProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('name_of_project',)


class StaffSerializer(serializers.ModelSerializer):
    projects = GetProjectsSerializer(many=True,read_only=True)
    class Meta:
        model = Staff
        fields = (
            'id', 'name', 'position', 'experience', 'activity', 'projects',
        )


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Projects
        fields = (
            'id', 'image', 'name_of_project','stage',  'url', 'staff'
        )
        
        



class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'id', 'upper_text', 'description', 'count_ready', 'count_active', 'count_await_p',
        )
        extra_kwargs= {
            'count_ready': {
                'read_only': True
            },
            'count_active': {
                'read_only': True
            },
            'count_await_p': {
                'read_only': True
            },
        }


class TypeOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfWork
        fields = (
            'id', 'introduction','type_of_service', 'description_of_service', 'image'
        )


class OurPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPartner
        fields = (
            'id', 'name', 'logo', 'url',
        )


class EventLentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLent
        fields = (
            'id', 'name', 'image', 'description',
        )


class FreeVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeVacancy
        fields = (
            'id', 'position', 'period', 'requirements', 'responsibilities', 'you_ll_recive',
        )


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = (
            'id', 'adress', 'email', 'phone_number',
        )


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = (
            'id', 'question', 'answer',
        )
    


# class FeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = (
#             'id', 'feedback', 'name'
#         )


class GetConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetConsult
        fields = (
            'id', 'name', 'question', 'contact'
        )
    def create(self, validated_data):
        text = f'Новый вопрос:\nИмя: {validated_data["name"]}\nВопрос: {validated_data["question"]}\nКонтакты: {validated_data["contact"]}'
        send_message_telebot(text)
        return super().create(validated_data)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'id', 'name', 'image', 'url'
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id', 'image'
        )

class WhatWeUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeUse
        fields = (
            'id','title', 'description','image'
        )