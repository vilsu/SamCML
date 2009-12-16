from django.db import models

import history 

class Tag(models.Model):
    tag = models.CharField(max_length=50, null=False)

    def __unicode__(self):
        return u'%s' % (self.tag)

class Author(models.Model):
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField()

    def __unicode__(self):
        return self.title

class Code(models.Model):
    title = models.CharField(max_length=150, null=False)
    tags = models.ManyToManyField(Tag, null=False)
    body = models.TextField(null=False)
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    history = models.ManyToManyField(history.History)

# nice presentation in p1 = (name='sami'); p1.save; ...; p1 ... in unicode
    def __unicode__(self):
        return self.name
