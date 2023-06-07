from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from area.models import *
from .forms import AreaForm


# Create your views here.

def index(request):
    q = MainForm.objects
    order = request.GET["order"] if "order" in request.GET else "-id"
    # gos_num = request.GET["gos_num"] if "gos_num" in request.GET else "-id"

    area_list = q.order_by(order) if order else q.all()
    form = AreaForm

    return render(request, "area/index.html", {"area_list": area_list, "form": form})
    # return render(request, "area/index.html", {"form": form})


def edit(request, id):
    model = MainForm.objects.get(pk=id)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/area")
    else:
        form = AreaForm(instance=model)

    return render(request, "area/edit.html", {"form": form})


def delete(request, id):
    MainForm.objects.get(pk=id).delete()
    return HttpResponseRedirect("/area")


def filial_data(request, id):
    company_list = Company.objects.filter(filial_id=id)
    grp_list = GrrProject.objects.filter(filial_id=id)
    ret = {'company': {}, 'grp': {}}
    for c in company_list:
        ret['company'][c.id] = c.name
    for c in grp_list:
        ret['grp'][c.id] = c.name
    return JsonResponse(ret)


def grp_data(request, id):
    plot_list = Plot.objects.filter(grp_id=id)
    ret = {}
    for c in plot_list:
        ret[c.id] = c.name
    return JsonResponse(ret)


def plot_data(request, id):
    plot = Plot.objects.get(pk=id)
    if not plot.lic_id:
        return JsonResponse({})
    one_lic = Lic.objects.get(id=plot.lic_id)
    if not one_lic:
        return JsonResponse({})
    ret = {"id": one_lic.id, "name": one_lic.name, "gos_num": one_lic.gos_num}
    return JsonResponse(ret)


def add(request):
    if request.method == "POST":
        form = AreaForm(json.loads(request.body.decode('utf-8')))

        if form.is_valid():
            work_type = WorkType.objects.get(pk=form.cleaned_data['work_type'].id)
            o = form.save(commit=False)
            o.measure_unit_id = work_type.measure_unit_id
            o.user_create = request.user.id if request.user.is_authenticated else None
            o.time_create = datetime.datetime.now()
            o.save()

            # order = request.GET["order"] if "order" in request.GET else ""
            # gos_num = request.GET["gos_num"] if "gos_num" in request.GET else ""

            q = MainForm.objects
            area_list = q.order_by('-id').all()

            return render(request, "area/area_list.html", {"area_list": area_list})
        else:
            return HttpResponse("Data is invalid: " + str(form.errors))

    return HttpResponse("Must be POST method")


