from django.shortcuts import get_list_or_404
from django.http import Http404

def get_object_or_404_custom(klass, *args, **kwargs):
    """
    Retrieve an object or return a custom response if not found.
    
    :param klass: Model or QuerySet to query
    :param args: Additional arguments for the query
    :param kwargs: Keyword arguments for the query
    :return: Object if found, raises Http404 otherwise
    """
    queryset = klass.objects if hasattr(klass, '_default_manager') else klass
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None
