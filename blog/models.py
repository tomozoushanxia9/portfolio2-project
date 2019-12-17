from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    # title = models.CharField('タイトル', max_length=50)
    # text = models.TextField('テキスト')
    # # created_at = models.DateField('作成日', auto_now_add=True)
    # # updated_at = models.DateField('更新日', auto_now=True)
    # def __str__(self):
    #     return self.title
    # class Meta:
    #     verbose_name = 'ブログ'
    #     verbose_name_plural = 'ブログ'
