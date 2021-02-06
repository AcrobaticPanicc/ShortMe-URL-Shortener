# ------- 3rd party imports -------
from flask import Blueprint, render_template

api_doc_blueprint = Blueprint('api_doc_blueprint', __name__, template_folder='templates')


@api_doc_blueprint.route('/api_doc')
def api_doc():
    return render_template('api_doc.html')
