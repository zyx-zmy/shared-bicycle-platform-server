#### 请求地址

```
POST /admin/beian/bicycles/:beian_bicycle_id/bicycle_number
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
number_file           |FILE    |F   |文件名

#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 422 Unprocessable Entity
{
	"message": "Validation Failed",
	"errors": [{"field": "FILE", "code": "invalid"},]
} //文件上传失败或解析失败

{
	"message": "Validation Failed",
	"errors": [{"resource": "FILE", "code": "incorrect_format"},]
} //文件格式有误

{
	"message": "Validation Failed",
	"errors": [{"resource": "FILE", "code": "scale_out"}]
} //超过文件上传条数限制

{
	"message": "Validation Failed",
	"errors": [{"resource": "FILE", "code": "incorrect_format"},]
} //文件行列不正确

{
	"message": "Validation Failed",
	"errors": [{"resource": "FILE", "code": "access_num"}]
} //超过停车场准入数量

Status: 404 Not Found 内容未找到

Status: 201 Ok 成功

```

Status: 201 成功
{
	"success": 3, //成功条数
	"failed": 1, //失败条数
	"err_row": [1] //失败的行
}





