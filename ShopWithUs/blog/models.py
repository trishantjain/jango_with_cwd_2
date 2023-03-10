from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    head0 = models.CharField(max_length=50, default="")
    chead0 = models.CharField(max_length=600, default="")
    head1 = models.CharField(max_length=50, default="")
    chead1 = models.CharField(max_length=600, default="")
    head2 = models.CharField(max_length=50, default="")
    chead2 = models.CharField(max_length=600, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title
