from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ListItem, Hyperlink
from django.core.paginator import Paginator
import pandas as pd



def home(request):
    return render(request, 'home.html')  # 渲染首页模板


# 专家列表视图
def list_items(request):
    # 获取搜索参数
    name_query = request.GET.get('name', '')
    department_query = request.GET.get('department', '')
    job_query = request.GET.get('job', '')

    # 多条件筛选
    list_items = ListItem.objects.all()
    if name_query:
        list_items = list_items.filter(name__icontains=name_query)
    if department_query:
        list_items = list_items.filter(department__icontains=department_query)
    if job_query:
        list_items = list_items.filter(job__icontains=job_query)

    # 分页
    paginator = Paginator(list_items, 20)  # 每页显示 20 条记录
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    hyperlinks = Hyperlink.objects.all()

    # 导入逻辑
    if request.method == 'POST' and 'import_file' in request.FILES:
        file = request.FILES['import_file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            ListItem.objects.create(
                name=row['姓名'],
                department=row['科室'],
                job=row['职称'],
                origin_department=row['所属医院科室'],
                project=row['帮扶专业'],
                duty=row['职务'],
                talent=row['专业特长'],
                official_time=row['坐诊时间'],
                contact=row['联系方式'],
                contactor=row['联系人']
            )
        return redirect('list_items')

    # 导出逻辑
    if request.GET.get('export') == 'true':
        data = list_items.values('name', 'department', 'job', 'origin_department', 'project', 'duty', 'talent',
                                 'official_time', 'contactor', 'contact')
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="list_items.xlsx"'
        df.to_excel(response, index=False)
        return response

    return render(request, 'list_items.html', {
        'list_items': page_obj,
        'hyperlinks': hyperlinks,
    })