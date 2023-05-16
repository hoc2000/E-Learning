from django.utils import timezone
from django.db import models
from django.utils.text import slugify  # auto create slug
from django.db.models.signals import pre_save  # presave auto create and save
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import random
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# Categoriess
# Color


class Categories(models.Model):
    choice_icon = (
        ('fab fa-python', 'python'),
        ('fab fa-java', 'java'),
        ('fas fa-snowman', 'snowman')
    )

    icon = models.CharField(choices=choice_icon, max_length=200, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('-id')

####### AUTHOR models#############


class Author(models.Model):
    author_profile = models.ImageField(
        upload_to="author", default='author/2021-11-19-14-04-25_0.png')
    name = models.CharField(max_length=100, null=True)
    about_author = RichTextField()
    slug = models.SlugField(default='', max_length=500,
                            null=True, blank=True,)
    created_at = models.DateTimeField(
        default=timezone.datetime.now(), editable=False)

    @property
    def short_description(self):
        return truncatechars(self.about_author, 20)

    def img_preview(self):
        return mark_safe('<img src="{}" width="80" />'.format(self.author_profile.url))
    img_preview.short_description = 'Image'
    img_preview.allow_tags = True

    def __str__(self):
        return self.name

    def author_snippet(self):
        return self.about_author[:300] + "..."


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.language


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_review = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.course_review + " - " + self.comment

# COURSE


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Course(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = AutoDateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    description = RichTextField()
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    deadline = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default='', max_length=500,
                            null=True, blank=True, editable=False)
    status = models.CharField(choices=STATUS, max_length=100, null=True)
    certificate = models.CharField(max_length=100, null=True)
    featured_image = models.ImageField(
        upload_to="featured_img", default='static/course_all.png', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

    def short_description(self):
        return truncatechars(self.description, 20)

    def img_preview(self):
        return mark_safe('<img src="{}" width="80" />'.format(self.featured_image.url))
    img_preview.short_description = 'Image'
    img_preview.allow_tags = True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_details", kwargs={'slug': self.slug})

    @staticmethod
    def autocomplete_search_fields():
        return 'author', 'category'
# Tự tạo slug cho Course


def create_slug_course(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_course(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_course(instance)

# Tạo slug cho author


def create_slug_author(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Author.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_author(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver_author(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_author(instance)


# PreSave sau khi Save
pre_save.connect(pre_save_post_receiver_course, Course)
pre_save.connect(pre_save_post_receiver_author, Author)


class What_you_learn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points


class Requirements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Lesson: " + self.name + " -  " + "Course: " + self.course.title

    class Meta:
        ordering = ['id']


class Video(models.Model):
    thumbnail = models.ImageField(
        upload_to="Yt_Thumbnail", default="Yt_Thumbnail/youtube-thumbnails.jpg", null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    youtube_id = models.CharField(max_length=200)
    time_duration = models.IntegerField(null=True)
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title


def create_course(instance, select_course=None):
    course = instance.lesson.course
    if select_course is not None:
        course = select_course
    return course

# Tự động điền course vào field -gg


def autofill_course(sender, instance, *args, **kwargs):
    if not instance.course:
        instance.course = create_course(instance)


class Document(models.Model):
    TYPE = (
        ('pdf', 'pdf'),
        ('docx', 'docx'),
        ('pptx', 'pptx'),
        ('rar', 'rar'),
    )
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    file = models.FileField(upload_to="Documents",
                            max_length=100, null=True)
    file_type = models.CharField(
        choices=TYPE, max_length=10, null=True, blank=True)
    preview = models.BooleanField(default=False)

    def __str__(self):
        return self.name


pre_save.connect(autofill_course, Video)
pre_save.connect(autofill_course, Document)


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    paid = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " - " + self.course.title


class Payment(models.Model):
    order_id = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    user_course = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " -- " + self.course.title


difficulties = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)


class Quizzes(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    topic = models.CharField(max_length=100)
    number_of_questions = models.IntegerField(null=True)
    time_duration = models.IntegerField(null=True)
    require_passing_score = models.IntegerField(null=True)
    difficulty_level = models.CharField(
        choices=difficulties, max_length=100, null=True)

    def __str__(self):
        return self.topic + " - " + self.course.title

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]


def create_slug_quizzes(instance, new_slug=None):
    slug = slugify(instance.topic)
    if new_slug is not None:
        slug = new_slug
    qs = Quizzes.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_quizzes(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver_quizzes(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_quizzes(instance)


pre_save.connect(pre_save_post_receiver_quizzes, Quizzes)


class Question(models.Model):
    text = models.CharField(max_length=1000)
    quizzes = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    point = models.IntegerField(null=True)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " - " + self.quiz.topic
