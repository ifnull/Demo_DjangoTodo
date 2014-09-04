from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from todo.models import Todo
from todo.serializers import MyDatetimeSerializer


class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        authorization = Authorization()
        resource_name = 'todo'
        allowed_methods = ['get', 'post', 'delete', 'put', 'patch']
        always_return_data = True
        serializer = MyDatetimeSerializer()
