# `ViewSet`

- viewset.ModelViewSet，功能强大的视图类，基本增删改查功能已经实现，继承自6个类
  - mixins.CreateModelMixin，实现了增加功能，`{'post': 'create'}`
  - mixins.RetrieveModelMixin, 获取单个对象`{'get': 'retrieve'}`
  - mixins.UpdateModelMixin, 修改单个对象`{'put': 'update'}`                   
  - mixins.DestroyModelMixin,删除单个对象`{'delete': 'destroy'}`                   
  - mixins.ListModelMixin,获取多个对象 `{'get': 'list'}`                  
  - GenericViewSet, 
- `ViewSet` 只是**一种基于类的视图，它不提供任何方法处理程序**（如 `.get()`或`.post()`）
- 如果我们使用 ViewSet 需要自己绑定请求处理方法
- `ViewSet` 的方法处理程序仅使用 `.as_view()` 方法绑定到完成视图的相应操作。例如
  - `url(r'^users/$', UserViewSet.as_view({'get': 'list'}))`
- 一般情况下的请求方法和视图方法的对应为：
  - `{'get': 'list'}` ，获取多条数据
  - `{'post': 'create'}`，创建一条
  - `{'get': 'retrieve'}`，获取单条数据
  - `{'put': 'update'}`   ，全部更新
  - `{'delete': 'destroy'}`，删除一条数据
  - `{'patch': 'partial_update'}`，局部更新

## `ViewSet 和 APIView的使用选择`

- 基本增删改查，ModelViewSet
- 复杂逻辑，继承 GenericAPIView 或 APIView， 然后自己编写逻辑

