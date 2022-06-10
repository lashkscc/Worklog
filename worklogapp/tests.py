from django.test import TestCase
from django.contrib.auth.models import User
from .models import Status, Task, TaskComment
# Create your tests here.

class StatusTest(TestCase):
    def setUp(self):
        self.status=Status(statusName='To do', statusDescription='testdescription', statusPosition=1)

    def test_statusstring(self):
        self.assertEqual(str(self.status), 'To do')

    def test_table_name(self):
        self.assertEqual(str(Status._meta.db_table), 'status')

class TaskTest(TestCase):
    def setUp(self):
        self.userCreated=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.status=Status(statusName='To do', statusDescription='testdescription', statusPosition=1)

        self.task = Task(taskName='testtask1', taskDescription='testdescription', taskUserCreated=self.userCreated, taskDateCreated='2019-01-01', 
        taskDeadline='2019-01-01', taskStatus=self.status)

    def test_taskstring(self):
        self.assertEqual(str(self.task), 'testtask1')

    def test_table_name(self):
        self.assertEqual(str(Task._meta.db_table), 'task')

class TaskCommentTest(TestCase):
    def setUp(self):
        self.userCreated=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.status=Status(statusName='To do', statusDescription='testdescription', statusPosition=1)

        self.task = Task(taskName='testtask1', taskDescription='testdescription', taskUserCreated=self.userCreated, taskDateCreated='2019-01-01', 
        taskDeadline='2019-01-01', taskStatus=self.status)

        self.taskComment = TaskComment(taskid=self.task, taskCommentDescription='testdescription', taskUserCreated=self.userCreated, taskDateCreated='2019-01-01')

    def test_taskcommentstring(self):
        self.assertEqual(str(self.taskComment), 'testtask1')

    def test_table_name(self):
        self.assertEqual(str(TaskComment._meta.db_table), 'taskcomment')