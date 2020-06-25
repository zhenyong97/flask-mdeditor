import unittest

from flask import Flask, render_template_string, current_app
from flask_wtf import FlaskForm, CSRFProtect

from flask_mdeditor import MDEditorField
from flask_mdeditor import MDEditor, _MDEditor


class MDEditorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)