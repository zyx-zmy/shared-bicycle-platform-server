#### 请求地址

```
GET /admin/bicycles/:bicycle_id
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------


#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 404 Not Found 内容未找到

Status: 200 Ok 成功

```

Status: 200 成功,返回一个[Bicycle](entities.md#Bicycle)对象