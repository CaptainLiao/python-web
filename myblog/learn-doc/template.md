# Templates 介绍
## 什么是`Templates`?
  * HTML文件
  * 使用了`Django`模板语言（`Django Template Language, DTL`）
  * 可使用用第三方模板（如`Jinja2`）

## 开发第一个`Template`
* 步骤
  * 在`APP`的根目录下创建名叫`TemplateS`的目录
  * 在该目录下创建`HTML`文件
  * 在`views.py`中返回`render()`
* `DTL`初步使用
  * `render()`函数中支持一个`dict`类型参数
  * 在模板中使用**{{参数名}}**来直接使用

## 不同APP下`templates`目录中的同名`.html`文件会照成冲突
因为`Django`按照`settings.py/INSTALLED_APPS`中的添加顺序查找`templates`

**解决方案：**在APP的`templates`目录下创建以APP名称的目录，将`html`文件放入新创建的目录下






























