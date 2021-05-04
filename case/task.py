from celery import shared_task
from case.models import Case, CaseResult

@shared_task(name="repeat_case")
def repeat_case(object_id, repeat):
    try:
        case = Case.objects.get(id=object_id)
    except:
        return False
    CaseResult.objects.create(
        case=case, 
        message="{0}={1}".format(repeat, case.message*repeat)
    )


