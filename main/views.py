from django.shortcuts import render
from django.shortcuts import redirect, reverse
from main.models import Reagent, Batch, Tracking
from users.forms import UserChangeForm
from decimal import Decimal
from django.contrib import messages
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from main.forms import QuantityForm
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'LIMS'
    }
    return render(request, 'main/index.html', context)


def main(request, page=1):
    query = request.GET.get('q')
    if query:
        samples = Reagent.objects.filter(name__icontains=query)
        if samples.exists():
            sample = samples.first()
            context = {
                'title': 'LIMS - Inventory Management',
                'samples': [sample],
                'batcn_nums': Batch.objects.all(),
            }
            return render(request, 'main/main.html', context)
        else:
            context = {
                'title': 'LIMS - Inventory Management',
                'samples': [], 
                'batcn_nums': Batch.objects.all(),
                'message': "Sorry, there are no matches for your search",
            }
            return render(request, 'main/main.html', context)
    else:
        samples = Reagent.objects.all().order_by('name')
        context = {
            'title': 'LIMS - Inventory Management',
            'samples': samples,
            'batcn_nums': Batch.objects.all(),
        }
        paginator = Paginator(samples, 6)
        samples_paginator = paginator.page(page)
        context.update({'samples':samples_paginator})
        return render(request, 'main/main.html', context)

def tracking(request, reagent_id):
    user=request.user
    form = UserChangeForm(instance=user)
    try:
        reagent = Reagent.objects.get(id=reagent_id)
        batches = Batch.objects.filter(reagent=reagent)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h2>404</h2><p>Not Found</p>")
    changes = []
    for batch in batches:
        tracking = Tracking.objects.filter(batch=batch).last()
        if tracking is None:
            tracking = Tracking(batch=batch, once_quantity_changed=0, user=request.user)
            tracking.save()
        changes.append(tracking)
    context = {
        'title': 'LIMS - Reagent tracking',
        'sample': reagent,
        'form': form, 
        'changes': changes,}
    return render(request, 'main/tracking.html', context)


def reagent_changed(request, id):
    tracking = Tracking.objects.get(id=id)
    batch = tracking.batch
    if request.method == 'POST':
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity_used = form.cleaned_data['quantity']
            once_quantity_changed = quantity_used
            remaining_quantity = batch.quantity - tracking.common_quantity_changed
            if quantity_used > remaining_quantity:
                messages.error(request, "The quantity cannot be greater than the available quantity")
                return redirect(reverse('tracking', args=[batch.reagent.id]))
            common_quantity_changed = tracking.common_quantity_changed + quantity_used
            batch.save()
            new_tracking = Tracking(once_quantity_changed=once_quantity_changed, common_quantity_changed=common_quantity_changed, user=request.user, batch=batch)
            new_tracking.save()
            return redirect(reverse('tracking', args=[batch.reagent.id]))
        else:
            messages.error(request, "Please enter valid quantity and click Confirm button")
            return redirect(reverse('tracking', args=[batch.reagent.id]))



