"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import datetime
from que_ans_app.models import Question

class SimpleTest(TestCase):
  #  def test_basic_addition(self):
   #     """
    #    Tests that 1 + 1 always equals 2.
     #   """
      #  self.assertEqual(1 + 1, 2)
     def test_add_question(self):
        c=Client()
        response=c.post('/add/',{'que_owner':'ylh', 'que_description':'how to write django unittest',
                                 'que_publish_time':datetime.datetime.now().strftime("%Y-%m-%d")})
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
     def test1_add_question(self):
        c=Client()
        response=c.post('/add/',{'que_owner':'JasonnnnnnnnnnnnnnnnnJasonnnnnnnnnnnnnnnnn', 'que_description':'how to write django unittest',
                                 'que_publish_time':datetime.datetime.now().strftime("%Y-%m-%d")})
        
        #self.assertEqual(response.status_code, 200)
        
class QuestionTest(TestCase):
    def setUp(self):
         que_owner='ylh'
         que_description='how to write django unittest'
         que_publish_time=(datetime.datetime.now().strftime("%Y-%m-%d"))
         question=Question(que_owner=que_owner,que_description=que_description,que_publish_time=que_publish_time)
         question.save()
    def test_queList(self):
        question=Question.objects.get(que_owner='ylh')
        print(question)
        

