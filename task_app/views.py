# tasks/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# API view for handling tasks (GET, POST, DELETE)
@api_view(['GET', 'POST', 'DELETE'])
def tasks(request):
    if request.method == 'GET':
        try:
            # Retrieve all tasks
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response({'tasks': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            data = request.data

            # Check if it's a single task or a list of tasks
            if isinstance(data, list):
                task_ids = []

                # Create multiple tasks
                for task_data in data:
                    if 'title' not in task_data:
                        return Response({'error': 'Title is required for creating task'}, status=status.HTTP_400_BAD_REQUEST)
                    task_obj = Task.objects.create(title=task_data['title'], is_completed=task_data.get('is_completed', False))
                    task_ids.append({'id': task_obj.id})

                return Response(task_ids, status=status.HTTP_201_CREATED)
            else:
                # Create a single task
                if 'title' not in data:
                    return Response({'error': 'Title is required for creating task'}, status=status.HTTP_400_BAD_REQUEST)
                task_obj = Task.objects.create(title=data['title'], is_completed=data.get('is_completed', False))
                return Response({'id': task_obj.id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            data = request.data
            if 'tasks' not in data or not isinstance(data['tasks'], list):
                return Response({'error': 'Invalid input format. Expected a list of tasks'}, status=status.HTTP_400_BAD_REQUEST)

            task_ids = [task['id'] for task in data['tasks']]

            # Check if all provided task IDs exist
            existing_tasks = Task.objects.filter(id__in=task_ids).values_list('id', flat=True)
            missing_ids = set(task_ids) - set(existing_tasks)

            if missing_ids:
                return Response({'error': f'Tasks with IDs {list(missing_ids)} not found'}, status=status.HTTP_404_NOT_FOUND)

            # Delete the tasks
            deleted_tasks = Task.objects.filter(id__in=task_ids).delete()

            if deleted_tasks[0] > 0:  # Check if any tasks were deleted
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'No tasks were deleted'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API view for handling a single task by ID (GET, DELETE, PUT)
@api_view(['GET', 'DELETE', 'PUT'])
def task_by_id(request, pk):
    if request.method == 'GET':
        try:
            # Retrieve a specific task by ID
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({'error': 'There is no task at that id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            # Delete a specific task by ID
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Task.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)  # Still return 204 if the task doesn't exist
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            # Update a specific task by ID
            task = Task.objects.get(pk=pk)
            data = request.data
            serializer = TaskSerializer(task, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Task.DoesNotExist:
            return Response({'error': 'There is no task at that id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
