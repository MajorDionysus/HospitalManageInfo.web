from django.db import models


# models.py
class ListItem(models.Model):
    name = models.CharField(max_length=255, verbose_name="外聘专家姓名")
    department = models.CharField(max_length=255, verbose_name="科室")
    origin_department = models.CharField(max_length=255, verbose_name="专家所属医院科室", null=True, blank=True)
    project = models.CharField(max_length=255, verbose_name="帮扶专业", null=True, blank=True)
    job = models.CharField(max_length=255, verbose_name="职称", null=True, blank=True)
    duty = models.CharField(max_length=255, verbose_name="职务", null=True, blank=True)
    talent = models.CharField(max_length=255, verbose_name="专业特长", null=True, blank=True)
    official_time = models.CharField(max_length=255, verbose_name="坐诊时间", null=True, blank=True)
    contactor = models.CharField(max_length=50, verbose_name="联系人", null=True, blank=True)
    contact = models.CharField(max_length=50, verbose_name="联系方式", null=True, blank=True)
    is_visible = models.BooleanField(default=True, verbose_name="是否显示")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name


class Hyperlink(models.Model):
    text = models.CharField(max_length=255, verbose_name="链接文字内容")
    url = models.URLField(verbose_name="链接地址")
    group = models.CharField(max_length=255, blank=True, null=True, verbose_name="分组")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
