from tastypie.resources import ModelResource
from todo.models import Todo


class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'
        allowed_methods = ['get', 'post', 'delete', 'put']
        always_return_data = True
