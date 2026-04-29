from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # related_name='comments' satisfies the "Related name: comments.all()" requirement
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=50)
    # Default ForeignKey setup satisfies the "post.comment_set.all()" style requirement
    post = models.ForeignKey(Post, on_delete=models.CASCADE)