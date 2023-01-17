from rest_framework import viewsets
from .models import Task , LowResultsSetPagination
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = LowResultsSetPagination
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'language']

    @action(methods=['POST'],detail= False, url_path="toggle-task", permission_classes=[IsAuthenticated])
    def toggle_task(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'added'})
    
    @action(methods=['GET'], detail= False, permission_classes=[IsAuthenticated],url_path="list_task")
    def get_task(self, request):
        title = request.title
        task = Task.objects.filter(title=title)
        data=TaskSerializer(instance=task).data
        return Response(data)

    @action(methods=['PUT'], detail= False, permission_classes=[IsAuthenticated],url_path="<int:pk>")
    def update_task(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'not put'})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({'error': 'not put'})

        serializer = self.serializer_class(data=request.data ,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': serializer.data})
        

class TaskFilterBackend(TaskViewSet):
    def get_queryset(self):
        queryset = Task.objects.filter(
            Q(taskGet__in= self.request.GET.getlist("tasks"))|
            Q(language__in= self.request.GET.getlist("languages"))
        )
        