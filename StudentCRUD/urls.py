from django.contrib import admin
from django.urls import path

# 注意要引入 url
from django.conf.urls import url
# 注意要引入自己的 views
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^allPage/$', views.all_page),   # 前往所有学生的网页
    url(r'^addPage/$', views.add_page),     # 前往新增学生的网页
    url(r'^addStudent/$', views.add_student),   # 添加学生的 dao 操作
    url(r'^search/$', views.search_student),   # 根据 t_name 查找学生的 dao 操作
    url(r'^get/(?P<student_id>[0-9]*)/$', views.search_student_id),   # 根据 id 查找学生的 dao 操作
    url(r'^updateStudent/$', views.update_student),   # 修改学生的 dao 操作
    url(r'^delete/(?P<student_id>[0-9]*)/$', views.delete_student),   # 删除学生的 dao 操作
]
