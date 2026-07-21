from django.test import TestCase
from projects.models import Project
from tasks.models import Task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        cls.project = Project.objects.create(
            name='test_project',
            owner=cls.user
        )

    def setUp(self):
        self.deadline = timezone.now()
        self.task = Task.objects.create(
            title='test_task',
            project=self.project,
            created_by=self.user
        )
        self.task_done = Task.objects.create(
            title='test_task_done',
            project=self.project,
            created_by=self.user,
            status=Task.TaskStatusChoices.DONE
        )
        self.task_in_progress = Task.objects.create(
            title='test_task_in_progress',
            project=self.project,
            created_by=self.user,
            status=Task.TaskStatusChoices.IN_PROGRESS
        )
        self.task_with_deadline = Task.objects.create(
            title='test_task_with_deadline',
            project=self.project,
            created_by=self.user,
            deadline=self.deadline,
        )
        self.task_with_assigned_user = Task.objects.create(
            title='test_task_with_assigned_user',
            project=self.project,
            created_by=self.user,
            deadline=self.deadline,
            assigned_to=self.user,
        )

    def test_task_creation_default(self):
        self.assertEqual(
            self.task.status,
            Task.TaskStatusChoices.TODO
        )

    def test_task_str_returns_title(self):
        self.assertEqual(
            str(self.task),
            self.task.title
        )

    def test_task_belongs_to_project(self):
        self.assertEqual(
            self.project,
            self.task.project
        )

    def test_project_has_task_in_related_name(self):
        self.assertIn(
            self.task,
            self.project.tasks.all()
        )

    def test_done_manager_returns_only_done_tasks(self):
        tasks = Task.done.all()
        self.assertIn(
            self.task_done,
            tasks,
        )
        self.assertEqual(
            1,
            tasks.count()
        )
        self.assertNotIn(
            self.task_in_progress,
            tasks
        )
        self.assertNotIn(
            self.task,
            tasks
        )

    def test_default_objects_manager_still_returns_all_tasks(self):
        tasks = Task.objects.all()
        self.assertIn(
            self.task_done,
            tasks,
        )
        self.assertIn(
            self.task,
            tasks,
        )
        self.assertIn(
            self.task_in_progress,
            tasks,
        )
        self.assertEqual(
            tasks.count(),
            5
        )

    def test_task_create_without_deadline(self):
        self.assertIsNone(
            self.task.deadline,
        )

    def test_task_create_and_save_with_deadline(self):
        self.assertEqual(
            self.task_with_deadline.deadline,
            self.deadline,
        )

    def test_task_assigned_user_save(self):
        self.assertEqual(
            self.task_with_assigned_user.assigned_to,
            self.user
        )

    def test_user_has_task_in_assigned_tasks_related_name(self):
        self.assertIn(
            self.task_with_assigned_user,
            self.user.assigned_tasks.all(),
        )



