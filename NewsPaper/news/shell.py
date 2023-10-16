from django.contrib.auth.models import User

user_1 = User.objects.create_user(username='Daria Gusina', password='322223')
user_2 = User.objects.create_user(username='Dmitriy Kubik', email='dmitriy@mail.ru')
user_3 = User.objects.create_user(username='Yana Yana')



from news.models import Author

author_1 = Author.objects.create(name_author=User.objects.get(username='Дима'))
author_2 = Author.objects.create(name_author=User.objects.get(username='Гоша'))
author_3 = Author.objects.create(name_author=User.objects.get(id=10))



from news.models import Category

category_1 = Category.objects.create(name_category='Спорт')
category_2 = Category.objects.create(name_category='Политика')
category_3 = Category.objects.create(name_category='Образование')
category_4 = Category.objects.create(name_category='Технологии')
category_5 = Category.objects.create(name_category='Кино')

from news.models import Post

post_1 = Post.objects.create(author = Author.objects.get(name_author=9), title='Выборы в США', text="В 2024 году состоятся выборы президента США", article_or_news ='new')
post_2 = Post.objects.create(author = Author.objects.get(pk=1), title='Картина за 1000000 рублей', text="«Эта картина была продана за одну минуту»", article_or_news ='art')
post_3 = Post.objects.create(author=Author.objects.get(pk=1), title='В Москве построили новый парк', text="В столице России построили самый большой парк в Европе за 1 миллиард долларов", article_or_news ='new')
post_4 = Post.objects.create(author=Author.objects.get(pk=2), title='Роналду лучший игрок', text="Криштиану  Роналду считаетсяя самым лучшим футболистом в мире по версии французского журналиста", article_or_news = 'new')
Post.objects.create(author=Author.objects.get(name_author=10), title="История СССР в 20 веке", text="История СССР явдяется очень интересной. Потому что страна за один век пережила много войн и экономических кризисов", article_or_news = 'article')

from news.models import PostCategory
from news.models import Post
from news.models import Category

PostCategory.objects.create(post = Post.objects.get(pk=1), category = Category.objects.get(name_category = 'Политика'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(name_category = 'Образование'))
PostCategory.objects.create(post = Post.objects.get(pk=3), category = Category.objects.get(name_category = 'Политика'))
PostCategory.objects.create(post = Post.objects.get(pk=4), category = Category.objects.get(name_category = 'Спорт'))
PostCategory.objects.create(post = Post.objects.get(pk=5), category = Category.objects.get(name_category = 'Кино'))

from news.models import Comment
from django.contrib.auth.models import User
from news.models import Post

comment_1 = Comment.objects.create(post = Post.objects.get(pk=1), user = User.objects.get(username = 'Дима'), text_comment = 'Круто')
Comment.objects.create(post = Post.objects.get(pk=2), user = User.objects.get(id=9), text_comment = 'Не понравилось')
comment_3 = Comment.objects.create(post = Post.objects.get(pk=3), user = User.objects.get(username = 'Гоша'), text_comment = 'Ахахах')
comment_4 = Comment.objects.create(post = Post.objects.get(pk=4), user = User.objects.get(username = 'Яна'), text_comment = 'Смешно')
Comment.objects.create(post = Post.objects.get(pk=5), user = User.objects.get(username = 'Юра'), text_comment = 'Понял')

from news.models import Post
from news.models import Comment

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=5).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=4).dislike()

from news.models import Author

Author.objects.get(pk=1).update_rating()
Author.objects.get(pk=2).update_rating()
Author.objects.get(pk=3).update_rating()
