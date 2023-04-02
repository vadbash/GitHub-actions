from django.test import TestCase
from django.template.defaultfilters import slugify
from .models import UserList, Register, WorkerList


class ModelsTestCase(TestCase):
    #test for model UserList
    def test_UserList(self):
        post = UserList.objects.create(
                                   name = 123,
                                   surname = "qeweqw",
                                   email = "avasd@asd.com",
                                   password = "55weqweqew55",)
    #test for model Register
    def test_Register(self):
        post = Register.objects.create(
                                   name = "",
                                   description = "qwewerdsf",
                                   email = 'avasd@asd.com',
                                   password = "usa444da")
    #test for model Bots
    def test_WorkerList(self):
        post = WorkerList.objects.create(
                                   name = "asdasdsd",
                                   surname = "qeweqw",
                                   email = "avasd@asd.com",
                                   password = "weq123weqew",)
        post.save()