from rest_framework import serializers
from .models import Bb

class PostModel:
   def __init__(self, title, content) -> None:
      self.title = title
      self.content = content

class PostSerializer(serializers.ModelSerializer):
   author = serializers.HiddenField(default=serializers.CurrentUserDefault())

   class Meta:
      model = Bb
      fields = (
         "title",
         "content",
         "published",
         "image",
         "rubric",
         "author"
      )

   # title = serializers.CharField(max_length=55)
   # content = serializers.CharField()
   # published = serializers.DateTimeField(read_only=True)
   # image = serializers.CharField(default="images/default_pic.jpg")
   # rubric_id = serializers.IntegerField(default=1)

   # def create(self, validated_data):
   #    return Bb.objects.create(**validated_data)

   # def update(self, instance, validated_data):
   #    instance.title = validated_data.get("title", instance.title)
   #    return super().update(instance, validated_data)