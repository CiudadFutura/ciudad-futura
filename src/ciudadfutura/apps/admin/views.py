from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from ciudadfutura.decorators import staff_required
from ciudadfutura.apps.auth.models import User, Tag, MisionMember, Supplier
from ciudadfutura.apps.mision.models import ShoppingCycle, Circle
from ciudadfutura.apps.product.models import Product, Category
from ciudadfutura.apps.order.models import Order, OrderItem
from ciudadfutura.utils import paginate
from .forms import UserForm, TagForm, ProductForm, SupplierForm, ShoppingCycleForm, CircleForm, OrderForm,\
    OrderItemForm, UserEditForm, CategoryForm


@staff_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html', {

    })


@staff_required
def admin_user_list(request):
    selected = [
        int(tag_id) for tag_id in request.GET.getlist('tags')
    ]

    results = User.objects.all()
    if selected:
        results = results.filter(tags__in=selected)

    return render(request, 'admin/admin_user_list.html', {
        'results': paginate(request.GET, results),
        'tags': Tag.objects.all(),
        'selected': selected
    })


@staff_required
def admin_user_form(request, user_id=None):

    user = None

    if user_id is not None:
        user = User.objects.get(id=user_id)

    if request.POST:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('admin:user-list')
    else:
        form = UserForm(instance=user)

    return render(request, 'admin/admin_user_form.html', {
        'form': form,
    })


@staff_required
def admin_user_details(request, user_id):
    return render(request, 'admin/admin_user_details.html', {})


@staff_required
def admin_user_edit(request, user_id):

    user = None

    if user_id is not None:
        user = User.objects.get(id=user_id)

    if request.POST:
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('User successfully saved.'))
            return redirect('admin:user-list')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'admin/admin_user_form.html', {
        'form': form,
    })


@staff_required
def admin_user_delete(request, user_id):
    User.objects.get(id=user_id).delete()
    messages.success(request, _('User successfully deleted.'))
    return redirect('admin:user-list')


@staff_required
def admin_tag_list(request):
    return render(request, 'admin/admin_tag_list.html', {
        'results': paginate(request.GET, Tag.objects.all())
    })


@staff_required
def admin_tag_delete(request, tag_id):
    Tag.objects.get(id=tag_id).delete()
    messages.success(request, _('Tag successfully deleted.'))
    return redirect('admin:tag-list')


@staff_required
def admin_tag_form(request, tag_id=None):
    tag = None

    if tag_id is not None:
        tag = Tag.objects.get(id=tag_id)

    if request.POST:
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save()
            messages.success(request, _('Tag successfully saved.'))
            return redirect('admin:tag-list')
    else:
        form = TagForm(instance=tag)

    return render(request, 'admin/admin_tag_form.html', {
        'form': form,
    })


@staff_required
def admin_product_list(request):
    return render(request, 'admin/admin_product_list.html', {
        'results': paginate(request.GET, Product.objects.all())
    })


@staff_required
def admin_product_form(request, product_id=None):
    product = None

    if product_id is not None:
        product = Product.objects.get(id=product_id)

    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, _('Product successfully saved.'))
            return redirect('admin:product-list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'admin/admin_product_form.html', {
        'form': form,
    })


@staff_required
def admin_product_delete(request, product_id):
    Product.objects.get(id=product_id).delete()
    messages.success(request, _('Product successfully deleted.'))
    return redirect('admin:product-list')


@staff_required
def admin_category_list(request):
    return render(request, 'admin/admin_category_list.html', {
        'results': paginate(request.GET, Category.objects.all())
    })


@staff_required
def admin_category_form(request, category_id=None):
    category = None

    if category_id is not None:
        category = Category.objects.get(id=category_id)

    if request.POST:
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, _('Category successfully saved.'))
            return redirect('admin:category-list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'admin/admin_category_form.html', {
        'form': form,
    })


@staff_required
def admin_category_delete(request, category_id):
    Category.objects.get(id=category_id).delete()
    messages.success(request, _('Category successfully deleted.'))
    return redirect('admin:category-list')


@staff_required
def admin_supplier_list(request):
    return render(request, 'admin/admin_supplier_list.html', {
        'results': paginate(request.GET, Supplier.objects.select_related())
    })


@staff_required
def admin_supplier_form(request, supplier_id=None):

    user = None

    if supplier_id is not None:
        user = User.objects.get(supplier__id=supplier_id)

    if request.POST:
        form = SupplierForm(request.POST, instance=user)
        if form.is_valid():
            supplier = form.save()
            messages.success(request, _('Supplier successfully saved.'))
            return redirect('admin:supplier-list')
    else:
        form = SupplierForm(instance=user)

    return render(request, 'admin/admin_supplier_form.html', {
        'form': form,
    })


@staff_required
def admin_supplier_delete(request, supplier_id):
    Supplier.objects.get(id=supplier_id).delete()
    messages.success(request, _('Supplier successfully deleted.'))
    return redirect('admin:supplier-list')


@staff_required
def admin_shopping_cycle_list(request):
    return render(request, 'admin/admin_shopping_cycle_list.html', {
        'results': paginate(request.GET, ShoppingCycle.objects.all()),
    })


@staff_required
def admin_shopping_cycle_form(request, shopping_cycle_id=None):
    shopping_cycle = None

    if shopping_cycle_id is not None:
        shopping_cycle = ShoppingCycle.objects.get(id=shopping_cycle_id)

    if request.POST:
        form = ShoppingCycleForm(request.POST, instance=shopping_cycle)
        if form.is_valid():
            shopping = form.save()
            for circle in Circle.objects.all():
                circle.shopping_cycle = shopping
                circle.save()
            messages.success(request, _('Shopping Cycle successfully saved.'))
            return redirect('admin:shopping-cycle-list')
    else:
        form = ShoppingCycleForm(instance=shopping_cycle)

    return render(request, 'admin/admin_shopping_cycle_form.html', {
        'form': form,
    })


@staff_required
def admin_shopping_cycle_delete(request, shopping_cycle_id):
    ShoppingCycle.objects.get(id=shopping_cycle_id).delete()
    messages.success(request, _('Shopping Cycle successfully deleted.'))
    return redirect('admin:shopping-cycle-list')


@staff_required
def admin_circle_list(request):
    object_list = MisionMember.objects.filter(is_lead=True)
    return render(request, 'admin/admin_circle_list.html', {
        'results': paginate(request.GET, object_list)
    })


@staff_required
def admin_circle_form(request, circle_id=None):
    circle = None

    if circle_id is not None:
        circle = Circle.objects.get(id=circle_id)

    if request.POST:
        form = CircleForm(request.POST, instance=circle)
        if form.is_valid():
            circle = form.save()
            messages.success(request, _('Circle successfully saved.'))
            return redirect('admin:circle-list')
    else:
        form = CircleForm(instance=circle)

    return render(request, 'admin/admin_circle_form.html', {
        'form': form,
    })


@staff_required
def admin_circle_delete(request, circle_id):
    Circle.objects.get(id=circle_id).delete()
    messages.success(request, _('Circle successfully deleted.'))
    return redirect('admin:circle-list')


@staff_required
def admin_order_list(request):
    return render(request, 'admin/admin_order_list.html', {
        'results': paginate(request.GET, Order.objects.all())
    })


@staff_required
def admin_order_form(request, order_id=None):
    order = None

    if order_id is not None:
        order = Order.objects.get(id=order_id)

    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            messages.success(request, _('Order successfully saved.'))
            return redirect('admin:order-list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'admin/admin_order_form.html', {
        'form': form,
    })


@staff_required
def admin_order_delete(request, order_id):
    Order.objects.get(id=order_id).delete()
    messages.success(request, _('Order successfully deleted.'))
    return redirect('admin:order-list')


@staff_required
def admin_order_item_list(request):
    return render(request, 'admin/admin_order_item_list.html', {
        'results': paginate(request.GET, OrderItem.objects.all())
    })


@staff_required
def admin_order_item_form(request, order_item_id=None):
    order = None

    if order_item_id is not None:
        order = OrderItem.objects.get(id=order_item_id)

    if request.POST:
        form = OrderItemForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            messages.success(request, _('Order successfully saved.'))
            return redirect('admin:order-item-list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'admin/admin_order_item_form.html', {
        'form': form,
    })


@staff_required
def admin_order_item_delete(request, order_item_id):
    Order.objects.get(id=order_item_id).delete()
    messages.success(request, _('Order successfully deleted.'))
    return redirect('admin:order-item-list')
