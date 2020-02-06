#### 请求地址

```
POST /admin/beian/bicycles
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
bicycle_model_code    |string  |T  |车辆型号编码
company_id            |string  |T  |企业id
bicycle_model_name    |string  |T  |车辆型号名称
bicycle_model_describe|string  |T  |车辆型号描述
bicycle_model_image   |string  |T  |车辆型号图片
bicycle_type          |int     |T  |单车类型 
 

#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 404 Not Found 内容未找到

Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
	"errors": [
        {"field": "bicycle_model_code", "code": "invalid"},
        ]
}
Status: 201 Ok 成功

```
Status: 201 成功
{
	"beian_bicycle_id": "sjdkjadjsakjda",
	"created_time": 1625375822,
}