from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.title

class Category(models.Model):
	intro = models.TextField()


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	comment = models.TextField()
