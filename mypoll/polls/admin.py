from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# we use TabularInline so that the choices show with the questions within our admin. ChoiceInline extends from TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # how many extra fields do we want


class QuestionAdmin(admin.ModelAdmin):  # extend ModelAdmin
    # fieldsets is a list of tuples, which is why there is a comma at the end. In each , first thing is name (as we don't need one for question_text, its None), 2nd thing is a python dictionary
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
# admin.site.register(Choice)
