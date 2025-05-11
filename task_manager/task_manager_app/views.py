from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from task_manager_app.models import Task
from task_manager_app.serializers import TaskSerializer

# Create your views here.

class TaskListCreateView(APIView):
    def get(self,request):
        search=request.query_params.get('search')
        search_date=request.query_params.get('search_date')
        sort_by_date=request.query_params.get('sort_by_date')

        tasks = Task.objects.all()

        if search:
            tasks=tasks.filter(title__icontains=search)
        if search_date:
            tasks= tasks.filter(date=search_date)
        if sort_by_date == 'true':
            tasks = tasks.order_by('date')

        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
class TaskDetailView(APIView):
    def patch(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({"error":"Task not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(task,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        try:
            task = Task.objects.get(pk=pk)

        except Task.DoesNotExist:
            return Response({"error":"Task not found"},status=status.HTTP_404_NOT_FOUND)
        

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

