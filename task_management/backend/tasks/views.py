import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger('task_management')

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensuring that only authenticated users can access these views

    def list(self, request, *args, **kwargs):
        logger.debug(f"Task list requested by user: {request.user}")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.debug(f"Task creation requested by user: {request.user}")
        logger.debug(f"Data received: {request.data}")

        # Automatically set the user field to the authenticated user
        request.data['user'] = request.user.id
        response = super().create(request, *args, **kwargs)
        
        logger.debug(f"Task created with response: {response.data}")
        return response

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensuring that only authenticated users can access these views

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Task detail requested for id: {kwargs['pk']} by user: {request.user}")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.debug(f"Task update requested for id: {kwargs['pk']} by user: {request.user}")
        logger.debug(f"Data received: {request.data}")

        # Ensure the task's user is not modified
        request.data.pop('user', None)
        
        response = super().update(request, *args, **kwargs)

        logger.debug(f"Task updated with response: {response.data}")
        return response

    
    def partial_update(self, request, *args, **kwargs):
        logger.debug(f"Partial task update requested for id: {kwargs['pk']} by user: {request.user}")
        logger.debug(f"Data received: {request.data}")

        # Ensure the task's user is not modified
        request.data.pop('user', None)
        response = super().partial_update(request, *args, **kwargs)

        logger.debug(f"Task partially updated with response: {response.data}")
        return response


    def destroy(self, request, *args, **kwargs):
        logger.debug(f"Task deletion requested for id: {kwargs['pk']} by user: {request.user}")
        return super().destroy(request, *args, **kwargs)
