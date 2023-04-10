from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, User, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "text", "author", "image", "group", "pub_date")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        fields = ("id", "author", "post", "text", "created")
        model = Comment
        read_only_fields = ("post",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        fields = ("user", "following")
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=["user", "following"],
                message="Уже подписаны!",
            )
        ]

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError(
                "Подписка на самого себя недоступна!"
            )
        return data
