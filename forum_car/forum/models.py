from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    TYPE_USER_VIEW = (
        ('fio', 'ФИО'),
        ('pseudo_name', 'Псевдоним'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=5000,
                           verbose_name=('Описание'),
                           blank=True, null=True)
    type_view = models.CharField(max_length=255,
                                 verbose_name=('Тип представления'),
                                 choices=TYPE_USER_VIEW,
                                 blank=True, null=True)
    pseudoname = models.CharField(max_length=255,
                                  verbose_name=('Псевдоним'),
                                  blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Comment(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField(max_length=1000, verbose_name='Текст комментария')


class Article(models.Model):
    PUSBLISH_STATUS = (
        ('publish', 'Да'),
        ('unpublish', 'Нет'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,
                             verbose_name='Title', blank=True,
                             null=True, default='')
    content = models.TextField()
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    status = models.CharField(max_length=55, verbose_name='Publish?', choices=PUSBLISH_STATUS)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return '{} {} '.format(self.title, self.create_at)

    def __repr__(self):
        return 'this is object in sqlite data base with unique id {}'.format(self.id)


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Марка")
    model = models.CharField(max_length=200, db_index=True, default='', verbose_name="Модель")
    year = models.CharField(max_length=200, db_index=True, default="", verbose_name="Год выпуска")
    slug = models.SlugField(max_length=200, db_index=True)
    engine = models.DecimalField(max_digits=10, decimal_places=2, default='', verbose_name="Обьем двигателя")
    petrol = models.CharField(max_length=200, db_index=True, default='', verbose_name="Вид топлива")
    transmission = models.CharField(max_length=200, db_index=True, default="", verbose_name="Коробка передач")
    image = models.ImageField(upload_to='foto_car/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:ProductDetail', args=[self.id, self.slug])


class Tag(models.Model):
    """Класс тегов статей
    """
    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class News(models.Model):
    """Класс новостей
    """
    user = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True)
    title = models.CharField("Заголовок", max_length=100)
    text_min = models.TextField("Мин. текст", max_length=350)
    text = models.TextField("Текст статьи")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keywords = models.CharField("Ключевые слова", max_length=50)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Ксласс комментариев к новостям
    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        verbose_name="Автомобили",
        on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)
