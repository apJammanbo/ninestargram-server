from django.db import models
from ninestargram_server.users import models as user_models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, null=True, related_name="images"
    )

    @property
    def like_count(self):
        return self.likes.all().count()

    def __str__(self):
        return "{} - {}".format(self.location, self.caption)

    class Meta:
        ordering = ["-created_at"]


class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True, related_name="comments"
    )

    def __str__(self):
        return self.message


class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True, related_name="likes"
    )

    def __str__(self):
        return "User: {} - Image Caption: {}".format(
            self.creator.username, self.image.caption
        )
