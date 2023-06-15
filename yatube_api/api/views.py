from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import (ModelViewSet,
                                     ReadOnlyModelViewSet,
                                     GenericViewSet)
from rest_framework.pagination import LimitOffsetPagination

from .permissions import OwnerOrReadOnly
from posts.models import Group, Post
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnerOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
