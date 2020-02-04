#### 请求地址

```
GET /admin/beian/companys
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
company_name          |string  |F  |公司名称
start_time            |string  |F  |开始时间 时间戳 如果没选择则不传
end_time              |string  |F  |结束时间 时间戳 如果没选择则不传


#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
	"errors": [
        {"field": "company_name", "code": "invalid"},
        ]
}

Status: 200 Ok 成功

```

Status: 200 成功,返回一个[Company](entities.md#Company)对象列表