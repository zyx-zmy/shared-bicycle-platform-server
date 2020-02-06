#### 请求地址

```
GET /admin/bicycles
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
company_name          |string  |F  |公司名称
bicycle_num           |string  |F  |车辆编号
bicycle_type_num      |string  |F  |车型编号
bicycle_type          |int     |F  |单车类型
put_status            |int     |F  |投放状态 1:未投放 2:已投放 3:维修中 4 已回收
page_size             |int     |F  |页数 默认15
page_num              |int     |F  |页码


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

Status: 200 成功,返回一个[Bicycle](entities.md#Bicycle)对象列表