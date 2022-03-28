from django.db import models

# Create your models here.

# import the base model class that we want our models to extend. any class we create will entend
# each model is represented by a class that subclasses(entends) django.db.models.Model. Each model has class variables, each of which represents a database field in the model.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Each field is an instance of a Field class
    pub_date = models.DateTimeField(
        "date published"
    )  # we can give each field an optional -user-friendly' name by passing a string as first argument
    # add string methods to all models, so that we have a useful representation  of Question and Choice objects rather just  [<Question: Question object (1)>]>
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )  # foreign key so that each choice has a Q. when question is deleted, all its choices will also be deleted.
    choice_text = models.CharField(max_length=200)  # CharField has a required argument of max_length
    votes = models.IntegerField(default=0)  # we can optionally give default values

    def __str__(self):
        return self.choice_text
