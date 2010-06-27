from django.contrib.auth.decorators import permission_required
from django.views.generic.create_update import create_object, delete_object, update_object
from django.views.generic.list_detail import object_detail
from products.models import Product, Category

def detail_product(*args, **kwargs):
    """Detail view of the product.
    
    If user has permissions to delete products, pass that info to template.
    
    """
    return object_detail(queryset=Product.objects.all(),
                         extra_context={'admin':
                                        args[0].user.has_perm('products.del_product')},
                        *args, **kwargs)

def detail_category(*args, **kwargs):
    """Detail view of the category.

    If user has permissions to delete categories, pass that info to template.

    """
    return object_detail(queryset=Category.objects.all(),
                         extra_context={'admin':
                                        args[0].user.has_perm('products.del_category')},
                        *args, **kwargs)

@permission_required('products.add_product')
def new_product(*args, **kwargs):
    """Create a new product.

    Permission checking wrapper for generic view.
    
    """
    return create_object(model=Product, post_save_redirect='/products', *args, **kwargs)

@permission_required('products.del_product')
def delete_product(*args, **kwargs):
    """Delete the product.

    Permission checking wrapper for generic view.

    """
    return delete_object(model=Product,
                         post_delete_redirect='/products',
                         *args, **kwargs)

@permission_required('products.change_product')
def change_product(*args, **kwargs):
    """Update product info.

    Permission checking wrapper for generic view.

    """
    return update_object(model=Product,
                         post_save_redirect='/products/',
                         template_name='products/product_update_form.html',
                         *args, **kwargs)

@permission_required('products.add_category')
def new_category(*args, **kwargs):
    """Create a new category.

    Permission checking wrapper for generic view.
    
    """
    return create_object(model=Category, post_save_redirect='/products/categories', *args, **kwargs)

@permission_required('products.del_category')
def delete_category(*args, **kwargs):
    """Delete the category.

    Permission checking wrapper for generic view.
    
    """
    return delete_object(model=Category,
                         post_delete_redirect='/products/categories',
                         *args, **kwargs)

