from django.db import models

class student_info(models.Model):
    # 字符
    t_name=models.CharField(max_length=20,default='linhongcun')
    # 数字
    t_age=models.IntegerField(default=21)   # 使用数字长度设置无效
    # 图片
    t_image=models.CharField(max_length=300,default='http://itaem.oss-cn-shenzhen.aliyuncs.com/20180509083509.jpg?Expires=4679469344&OSSAccessKeyId=LTAIATBJKsu6vu4R&Signature=PJkwOp9DVhtYu3Xkka0MnZVfnP0%3D')

