from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from task_manager_app.models import Task

# Create your tests here.
class TaskTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title = "Testing",
            description = "Test tas description",
            date="2025-05-07"

        )
        self.url = reverse("task-list-create")
        self.task_url = reverse("task-detail",args=[self.task.id])


    def test_create_task(self):
        data = {
            "title": "New Task",
            "description": "Task created during test",
            "date": "2025-05-09"
        }
        response = self.client.post(self.url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_get_all_task(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)                   #to get one task 


    def test_patch_task(self):
        data = {"title": "Update Task"}
        response = self.client.patch(self.task_url,data,content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["title"],"Update Task") 

    def test_delete_task(self):
        response = self.client.delete(self.task_url)                    #delete a task using delete method
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

       

    def test_task_not_found(self):
        response = self.client.patch(reverse('task-detail', args=[999]))  #invalid task id
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




