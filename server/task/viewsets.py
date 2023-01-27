from rest_framework import viewsets
from .models import Task , LowResultsSetPagination
from .serializers import TaskSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    pagination_class = LowResultsSetPagination
    # permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'language']

    @action(methods=['POST'],detail= False, url_path="create-task")
    def create_task(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'added'})
    
    @action(methods=['GET'], detail= False,url_path="tasks")
    def get_task(self, request):
        task = Task.objects.all()
        data=TaskSerializer(task, many=True).data
        return Response(data)

# , permission_classes=[IsAuthenticated]
    @action(methods=['PUT'], detail= True ,url_path="update-tasks")
    def update_task(self, request, pk):
        if not pk:
            return Response({'error': 'not put'})

        try:
            instance = Task.objects.get(id=pk)
        except:
            return Response({'error': 'not put'})

        serializer = self.serializer_class(data=request.data ,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': serializer.data})

    @action(methods=['DELETE'], detail= True, url_path="delete-tasks")
    def delete_task(self, request, pk):
        if not pk:
            return Response({'error': 'not put'})

        try:
            task = Task.objects.get(id=pk)
        except:
            return Response({'error': 'not put'})

        task.delete()
        return Response({'message': 'task delete'})

        