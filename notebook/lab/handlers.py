"""Tornado handlers for the tree view."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from tornado import web
from ..base.handlers import IPythonHandler


class LabHandler(IPythonHandler):

    """Render the Jupyter Lab View."""

    @web.authenticated
    def get(self):
        self.write(self.render_template('lab.html',
            page_title='Jupyter Lab',
            terminals_available=self.settings['terminals_available'],
            mathjax_url=self.mathjax_url))


#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------


default_handlers = [
    (r"/lab", LabHandler),
    ]
