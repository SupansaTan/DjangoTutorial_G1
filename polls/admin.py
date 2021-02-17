from django.contrib import admin
from .models import Question,Choice,Vote

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Vote)