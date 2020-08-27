from django.db import models


# Create your models here.
class EmailEntry(models.Model):
    # 定義null = True會將你的資料庫相應欄位設置為NULL（不定義就會設置為NOT NULL）。對於Django的欄位類型（如DateTimeField、ForeignKey），空值意味著會在資料庫中存儲NULL值
    #定義blank=True，這取決於該欄位在表單中是否為必填項。表單包括admin管理以及自己定義的表單。如果定義了blank=True，表單中相應的欄位可以不填寫內容
    email = models.EmailField()
    name = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    # date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)  # set when saved?
    timestamp = models.DateTimeField(auto_now_add=True)  # set when added?
