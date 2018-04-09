from django.db import models


class WinAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    stu_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    option_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # 部根据模型生成表
        db_table = 'win_answer'


class WinQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_lib_id = models.IntegerField()
    question_content = models.CharField(max_length=255, blank=True, null=True)
    question_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'win_question'


class WinQuestionLib(models.Model):
    lib_id = models.AutoField(primary_key=True)
    lib_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'win_question_lib'
