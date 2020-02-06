#### 请求地址

```
PATCH /admin/beian/bicycles/:beian_bicycle_id
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
access_num            |int     |T  |准入数量


#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 404 Not Found 内容未找到

Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
	"errors": [
        {"field": "access_num", "code": "invalid"},
        ]
}
Status: 204 Ok 成功

```
