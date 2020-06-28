from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask import current_app


class MDEditor(TextArea):

    def __call__(self, field, **kwargs):
        editor = current_app.extensions['mdeditor']
        mapping_value = {"id": field.id, "name": field.name, "value": field.data if field.data else '' }
        return editor.load(**mapping_value)
        

class MDEditorField(TextAreaField):
    widget = MDEditor()