#### 请求地址

```
GET /admin/beian/bicycles/:beian_bicycle_id/bicycle_number
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
page_size             |int     |F  |页数 默认15
page_num              |int     |F  |页码

#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
	"errors": [
        {"field": "page_size", "code": "invalid"},
        ]
}

Status: 404 Not Found 内容未找到

Status: 200 Ok 成功

```

Status: 200 成功,返回一个[BicycleNumber](entities.md#BicycleNumber)对象