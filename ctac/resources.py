from import_export import resources
from .models import *


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
