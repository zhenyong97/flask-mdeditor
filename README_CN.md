# Flask-mdeditor
[![ENV](https://img.shields.io/badge/release-v0.1-blue.svg)](https://github.com/pylixm/django-mdeditor)
[![ENV](https://img.shields.io/badge/pypi-v0.1-blue.svg)](https://pypi.org/project/Flask-MDEditor/)
[![ENV](https://img.shields.io/badge/中文-v0.1-blue.svg)](./README_CN.md)
[![ENV](https://img.shields.io/badge/python-3.7x-green.svg)]()
[![ENV](https://img.shields.io/badge/flask-1.0+-green.svg)]()
[![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

![](./flask_and_mdeditor.png)

**Flask-mdeditor**  是基于[Editor.md](https://github.com/pandao/editor.md)的一个[flask]() Markdown文本编辑插件应用

**Flask-mdeditor** 的灵感来源启发与 [django-mdeditor](https://github.com/pylixm/django-mdeditor), [flask-ckeditor](https://github.com/greyli/flask-ckeditor)

**注:**
* 关于Markdown页面的渲染问题，建议使用后端渲染，可以使用如[mistune](https://github.com/lepture/mistune)的第三方python后端markdown渲染

## 功能
------------------------------
* 集成Editor.md的大部分功能
    * 支持标准的Markdown 文本、 CommonMark 和 GFM (GitHub Flavored Markdown) 文本;
    * 支持实时预览、图片上传、格式化代码、搜索替换、皮肤、多语言等。
    * 支持TOC 目录和表情；
    * 支持 TeX, 流程图、时序图等图表扩展。
    * 提供了`MDEditorField` 用来支持FlaskForm

## 快速开始
------------------------------
### 安装
> `pip install flask-mdeditor`
### 初始化
必须先以通常的方式初始化此扩展，然后才能使用该扩展，为了能够正确保存上传图片，MDEDITOR_FILE_UPLOADER是**需要**首先配置，例如：
```python
from flask_mdeditor import MDEditor
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['MDEDITOR_FILE_UPLOADER'] = os.path.join(basedir, 'uploads') # this floder uesd to save your uploaded image
mdeditor = MDEditor(app)
```
### 在Flask-WTF/WTForms中使用

使用Flask-WTF / WTForms时，可以导入FLASK-MDEDITOR提供的MDEditorField，就像StringField一样使用它：
```python
from flask_mdeditor import  MDEditorField
class PostForm(FlaskForm):
    content = MDEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()

```
在template中渲染
```html
<form action="/xxx" method="POST">
        {{ form.csrf_token }}
        {{ form.content.label }} {{ form.content() }}
        {{ form.submit() }}
</form>
```
如果您不使用wtf，则可以使用全局 jinja2 func `{{ mdeditor.load() }}` 来加载编辑器，例如：
```html
<form action="/" method="POST">
    {{ mdeditor.load() }}
    <button type="submit">提交</button>
</form>
```

### 获取上传的md内容
* 使用wtf的方式

```python
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        body = form.content.data
        ...
```
* 另外

由于MDEditor textarea只是普通的`<textarea>`元素，因此可以通过传递** mdeditor **作为键来从request.form获取数据：
```python
@app.route('/save', methods=['POST'])
def new_post():
    if request.method == 'POST':
        data = request.form.get('mdeditor')
    ...
```
------------------
## Tip
demo中的flask_test可供参考

## 更多的配置
可以通过添加如下的字段修改mdeditor的特性
|Name|Default Value| Info | Required | Option
|-|-|-|-|-|
|MDEDITOR_FILE_UPLOADER| path | the floder path used to save uploaded img  | √ | 
|MDEDITOR_HEIGHT|500px|Browser rendering editor height|×|
|MDEDITOR_WIDTH|100%|Browser rendering editor width|×|
|MDEDITOR_THEME|default|editor main theme|×|dark / default|
|MDEDITOR_PREVIEW_THEME|default|preview area theme|×| default / dark
|MDEDITOR_EDITOR_THEME|default|edit area theme|×| pastel-on-dark / default
|MDEDITOR_LANGUAGE|zh|editor language|×|zh / en

## TODO
* 编写完整的单元测试
* 代码优化
* 丰富功能

## License
The MIT License.

Copyright (c) 2020 Zisc