from django.contrib import admin
from .models import *
from jet.filters import RelatedFieldAjaxListFilter
from jet.admin import CompactInline
# Register your models here.

# TabularInline in course


class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn


class Requirements_TabularInline(admin.TabularInline):
    model = Requirements


class Video_TabularInline(CompactInline):
    model = Video
    extra = 1
    show_change_link = True


class Document_TaularInline(CompactInline):
    model = Document


class Lesson_TabularInline(CompactInline):
    model = Lesson
    inlines = (Document_TaularInline, Video_TabularInline)


class Course_display(admin.ModelAdmin):
    list_display = [
        'img_preview',
        'title',
        'category',
        'author',
        'price',
        'created_at',
    ]
    list_display_links = [
        'title',
    ]
    list_filter = (
        ('author', RelatedFieldAjaxListFilter),
        ('category', RelatedFieldAjaxListFilter),
    )
    readonly_fields = ('img_preview', 'created_at')

    inlines = (what_you_learn_TabularInline,
               Requirements_TabularInline, Lesson_TabularInline)


class Author_display(admin.ModelAdmin):
    list_display = [
        'img_preview',
        'name',
        'created_at',
    ]
    list_display_links = [
        'name',
    ]
    readonly_fields = ('img_preview', 'created_at')

# LESSON


class Lesson_display(admin.ModelAdmin):
    list_display = [
        'name',
        'course',
    ]
    list_display_links = [
        'name'
    ]
    list_filter = [
        ('course', RelatedFieldAjaxListFilter),
    ]

# QUIZ REGISTER


class create_question(admin.TabularInline):
    model = Question


class quiz_admin(admin.ModelAdmin):
    inlines = (create_question,)


class create_answer(admin.TabularInline):
    model = Answer


class question_admin(admin.ModelAdmin):
    inlines = (create_answer,)


admin.site.register(Categories)
admin.site.register(Author, Author_display)
admin.site.register(Course, Course_display)
admin.site.register(Comment)
admin.site.register(Level)
admin.site.register(Video)
admin.site.register(Language)
admin.site.register(Requirements)
admin.site.register(Lesson, Lesson_display)
admin.site.register(UserCourse)
admin.site.register(Payment)
admin.site.register(Question, question_admin)
admin.site.register(Quizzes)
admin.site.register(Result)
