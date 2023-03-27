from import_export import resources
from .models import FileMs


class modelresource (resources.ModelResource):
    class meta:
        model=FileMs