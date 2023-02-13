from modeltranslation.translator import  TranslationOptions
from modeltranslation.decorators import register
from .models import (
    AboutUs,
    WhatWeUse,
    Staff,
    TypeOfWork,
    EventLent,
    FreeVacancy,
    QuestionAnswer,
)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("upper_text", "description")


@register(WhatWeUse)
class WhatWeUseTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ("city","name", "position", "experience", "activity")


@register(TypeOfWork)
class TypeOfWorkTranslationOptions(TranslationOptions):
    fields = ("introduction", "type_of_service", "description_of_service")


@register(EventLent)
class EventLentTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(FreeVacancy)
class FreeVacancyTranslationOptions(TranslationOptions):
    fields = ("position", "period", "requirements", "responsibilities", "you_ll_recive")


@register(QuestionAnswer)
class QuestionAnswerTranslationOptions(TranslationOptions):
    fields = ("question", "answer")