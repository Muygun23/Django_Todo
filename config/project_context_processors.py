from todo.models import Category


def global_category_context(request):
    # global_caregories=Category.objects.all()
    return dict (
        global_caregories=Category.objects.filter(is_active=True)
    )


