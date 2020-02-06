#### 请求地址

```
GET /admin/bicycle_status_records
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
company_name          |string  |F  |公司名称
bicycle_num           |string  |F  |车辆编号
bicycle_status        |string  |F  |车辆状态 1:停放中2:行驶中3:调度中4:被预约
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

Status: 200 成功,返回一个[BicycleDriverRecord](entities.md#BicycleDriverRecord)对象列表