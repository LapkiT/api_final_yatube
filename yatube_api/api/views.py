from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from posts.models import Post, Follow, Group
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Post.objects.select_related('author')
        group_id = self.request.query_params.get('group_id', None)
        if group_id is not None:
            queryset = queryset.filter(group_id=group_id)
        return queryset

    def list(self, request, *args, **kwargs):
        if 'limit' in request.query_params or 'offset' in request.query_params:
            return super().list(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = None


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
