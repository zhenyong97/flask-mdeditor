"""
    flask_mdeditor

    :author: ZiscLi <506141737@qq.com>
    :copyright: (c) 2020 by Zisc Li
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app, request, Blueprint, url_for, render_template_string, render_template
from flask import send_from_directory, jsonify
from markupsafe import Markup
import os
from flask_mdeditor.utils import random_filename

from flask_mdeditor.fields import MDEditorField # noqa

class _MDEditor():

    """the class implement function for jinja2 template."""
    @staticmethod 
    def load(**kwargs):
        # print(render_template('markdown.html'))
        if not kwargs.get('name'):
            kwargs['name'] = 'mdeditor'
        return Markup(render_template('markdown.html', **kwargs))

    @property
    def config(self):
        DEFAULT_CONFIG = {
            'width': current_app.config.get('MDEDITOR_WIDTH','100%'),
            'height': current_app.config.get('MDEDITOR_HEIGHT', 500),
            'toolbar': ["undo", "redo", "|",
                        "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                        "h1", "h2", "h3", "h5", "h6", "|",
                        "list-ul", "list-ol", "hr", "|",
                        "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                        "emoji", "html-entities", "pagebreak", "goto-line", "|",
                        "help", "info",
                        "||", "preview", "watch", "fullscreen"],
            'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                                    "PNG", "bmp", "BMP", "webp", "WEBP"],
            'image_folder': 'editor',
            'theme': current_app.config.get('MDEDITOR_THEME','default'),  # dark / default
            'preview_theme': current_app.config.get('MDEDITOR_PREVIEW_THEME', 'default'),  # dark / default
            'editor_theme': current_app.config.get('MDEDITOR_EDITOR_THEME', 'default'),  # pastel-on-dark / default
            'toolbar_autofixed': True,
            'search_replace': True,
            'emoji': True,
            'tex': True,
            'task_list': False,
            'flow_chart': True,
            'sequence': True,
            'language': current_app.config.get("MDEDITOR_LANGUAGE",'en'),  # zh / en
            'watch': True,  # Live preview
            'lineWrapping': current_app.config.get('MDEDITOR_WRAPPING','False'),  # lineWrapping
            'lineNumbers': False  # lineNumbers
        }
        return DEFAULT_CONFIG



class MDEditor(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.blueprint = Blueprint('mdeditor', __name__, static_folder='static', template_folder='templates',
                              static_url_path='/mdeditor' + app.static_url_path)
        self.blueprint.add_url_rule('/uploads', '__uploads', self.__uploads, methods=['post'])
        self.blueprint.add_url_rule('/files/<path:filename>', '__files_show', self.__uploaded_files)
        app.register_blueprint(self.blueprint, url_prefix='/mdeditor')
        
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['mdeditor'] = _MDEditor()
        app.context_processor(self.context_processor)
        app.config.setdefault("MDEDITOR_FILE_UPLOADER", '')  # 上传的文件夹

    def __uploaded_files(self, filename):
        # print("in ulpadeed")
        path = current_app.config['MDEDITOR_FILE_UPLOADER']
        return send_from_directory(path, filename)

    def __uploads(self):
        # 图片上传
        # print("in logic!!!")s
        f = request.files.get('editormd-image-file')
        # print(f)
        extension = f.filename.split('.')[-1].lower()
        if extension not in ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                            "PNG", "bmp", "BMP", "webp", "WEBP"]:
            return upload_fail(message='Image only!')
        if os.path.exists(current_app.config['MDEDITOR_FILE_UPLOADER']): # 如果路径存在
            save_filename = random_filename(f.filename)
            f.save(os.path.join(current_app.config['MDEDITOR_FILE_UPLOADER'], save_filename))
            return upload_success(url=url_for('mdeditor.__files_show', filename=save_filename, _external=True))
        else:
            return upload_fail(message='请实例化上传路径')


    @staticmethod
    def context_processor():
        # print(current_app.extensions['mdeditor'].config)
        return {'mdeditor': current_app.extensions['mdeditor'], 'mdeditor_config': current_app.extensions['mdeditor'].config}


def upload_fail(message=None):
    return jsonify(success=0, message=message, url='')


def upload_success(url):
    return jsonify(success=1, message='上传成功', url=url)
