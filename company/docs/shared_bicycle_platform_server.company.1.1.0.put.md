#### 请求地址

```
PUT /admin/beian/companys/:company_id
```

#### 请求参数	 

name                  |type    |NN |comments
----------------------|--------|---|----------------------
company_name          |string  |T  |公司名称
company_address       |int     |T  |公司地址
legal_person          |string  |T  |公司法人
contacts      	      |string  |T  |企业联系人
contacts_phone_num    |string  |T  |企业联系人手机号
business_license      |string  |T  |营业执照代码 
business_license_image|string  |T  |营业执照照片 

#### 返回结果

```
Status: 403 Forbidden 授权无效或已过期

Status: 404 Not Found 内容未找到
Status: 422 Unprocessable Entity
{
    "message": "Validation Failed",
	"errors": [
        {"field": "company_name", "code": "invalid"},
        ]
}
Status: 204 Ok 成功

```
Status: 204 成功
