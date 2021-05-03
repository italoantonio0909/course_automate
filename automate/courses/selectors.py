from .models import Course


def course_by_id(*, course_id: int):
    return Course.objects.get(id=course_id)
    