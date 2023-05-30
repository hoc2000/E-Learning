import json

from django.contrib import admin
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from django.utils import timezone
import pytz
from django.db.models.functions import TruncDay, TruncDate, TruncMonth
# Register your models here.

# TabularInline in course


# class course_data(admin.AdminSite):
#     def changelist_view(self, request, extra_context=None):
#         # Aggregate new authors per day
#         tz = pytz.timezone('Asia/Bangkok')
#         chart_data_course = (
#             Course.objects.annotate(date=TruncDay("created_at", tzinfo=tz))
#             .values("date")
#             .annotate(y=Count("id"))
#             .order_by("-date")
#         )
#         # Serialize and attach the chart data to the template context
#         as_json = json.dumps(list(chart_data_course), cls=DjangoJSONEncoder)
#         print("Json %s" % as_json)
#         extra_context = extra_context or {"chart_data_course": as_json}


class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn


class Requirements_TabularInline(admin.TabularInline):
    model = Requirements


class Video_TabularInline(admin.TabularInline):
    model = Video


class Document_TaularInline(admin.TabularInline):
    model = Document


class Lesson_TaularInline(admin.TabularInline):
    model = Lesson


class Course_display(admin.ModelAdmin):
    # Change from query set to JSON
    def changelist_view(self, request, extra_context=None):
        # Aggregate new authors per day
        # tz = pytz.timezone('Asia/Bangkok')
        data_course_publish = (
            Course.objects
            .filter(status="XEM ĐƯỢC")
            .annotate(
                month=ExtractMonth("created_at"))
            .values("month")
            .annotate(y=Count("id"))
            .order_by("month")
        )
        data_course_draft = (
            Course.objects
            .filter(status="NHÁP")
            .annotate(
                month2=ExtractMonth("created_at"))
            .values("month2")
            .annotate(y=Count("id"))
            .order_by("month2")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(data_course_publish), cls=DjangoJSONEncoder)
        as_json2 = json.dumps(list(data_course_draft), cls=DjangoJSONEncoder)

        print("Json %s" % as_json)
        print("Json %s" % as_json2)

        extra_context = extra_context or {
            "data_course_publish": as_json,
            "data_course_draft": as_json2}

        return super().changelist_view(request, extra_context=extra_context)

    list_display = [
        'img_preview',
        'title',
        'status',
        'category',
        'author',
        'price',
        'created_at',
        'update_at',
    ]
    list_display_links = [
        'title',
    ]

    list_filter = [
        'category',
        'author',
        'status',
    ]
    readonly_fields = ('img_preview', 'created_at')

    inlines = (what_you_learn_TabularInline,
               Requirements_TabularInline, Lesson_TaularInline)
    ordering = ("-created_at",)
    list_per_page = 11


class Author_display(admin.ModelAdmin):
    list_display = [
        'img_preview',
        'name',
        'created_at',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = [
        'name',
        'created_at',
    ]
    readonly_fields = ('img_preview', 'created_at')
    list_per_page = 11
# LESSON


class Department_display(admin.ModelAdmin):
    list_display = [
        'img_preview',
        'name',
    ]
    list_per_page = 11


class Lesson_display(admin.ModelAdmin):
    list_display = [
        'name',
        'course',
    ]
    list_display_links = [
        'name'
    ]
    list_filter = [
        'course',
    ]
    inlines = (Document_TaularInline, Video_TabularInline)
    list_per_page = 11

# QUIZ REGISTER


class create_question(admin.TabularInline):
    model = Question


class quiz_admin(admin.ModelAdmin):
    inlines = (create_question,)


class create_answer(admin.TabularInline):
    model = Answer


class question_admin(admin.ModelAdmin):
    inlines = (create_answer,)


class VideoAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['course'] = Course.objects.first().id  # set default author
        return initial


admin.site.register(Categories)
admin.site.register(Author, Author_display)
admin.site.register(Course, Course_display)
admin.site.register(Comment)
admin.site.register(Level)
admin.site.register(Department, Department_display)
admin.site.register(Video, VideoAdmin)
admin.site.register(Requirements)
admin.site.register(Lesson, Lesson_display)
admin.site.register(UserCourse)
admin.site.register(Payment)
admin.site.register(Question, question_admin)
admin.site.register(Quizzes)
admin.site.register(Result)
