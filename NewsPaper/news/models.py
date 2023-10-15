
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse




class Author(models.Model):
    name_author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)



    def update_rating(self):
        a = Post.objects.filter(id_author=self.id).aggregate(Sum('rating'))['rating__sum'] * 3
        b = Comment.objects.filter(id_user=self.id_user).aggregate(Sum('rating_comment'))['rating_comment__sum']
        c = Post.objects.filter(id_author=self.id).values('id')
        d = 0
        for i in c:
            com = Comment.objects.filter(id_post=i['id']).aggregate(Sum('rating_comment'))['rating_comment__sum']
            if com != None:
                d += com
        self.rating = a + b + d
        self.save()

sport = 'sp'
politics = 'pol'
education = 'ed'
technology = 'tech'
movie = 'mov'

POSITIONS = [
    (sport, 'Спорт'),
    (politics, 'Политика'),
    (education, 'Образование'),
    (technology, 'Технологии'),
    (movie, 'Кино')
]

class Category(models.Model):
    name_category = models.CharField(max_length=10, choices = POSITIONS, default = technology, unique = True)

    def __str__(self):
        return self.name_category


article = 'art'
news = 'new'

PUBLICATION = [
    (article, 'Статья'),
    (news, 'Новость')
]

class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    article_or_news = models.CharField(max_length=8, choices = PUBLICATION, default = news)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    categories = models.ManyToManyField('Category', through = 'PostCategory')

    def preview(self):
        return self.text[0:125] + "..."

    @property
    def rating_post(self):
        return self.rating

@rating_post.setter
    def rating_post(self, value):
        self.rating = int(value) if value >= 0 else 0
        self.save()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()




    def __str__(self):
        return f'{self.title} {self.text[:10000]} {self.time_in} {self.author} {self.article_or_news} {self.categories} {self.rating}'

    def get_absolute_url(self):
        return reverse('posts_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text_comment = models.CharField(max_length=500)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default = 0)

    @property
    def comment_rating(self):
        return self.rating_comment

    @comment_rating.setter
    def comment_rating(self, value):
        self.rating_comment = int(value) if value >= 0 else 0
        self.save()

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()