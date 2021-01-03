from django.shortcuts import render

def panel(request):
    return render(request, 'Backend/Pages/Dashboard/dashboard.html')

def content(request):
    return render(request, 'Backend/Pages/Manage/Content/manage-content.html')
