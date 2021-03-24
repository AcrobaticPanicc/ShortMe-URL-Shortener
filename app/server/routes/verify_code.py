# ------- 3rd party imports -------
from flask import Blueprint, render_template, request, redirect, url_for, session

# ------- local imports -------
from app.server.db.extensions import db
from app.server.db.models import VerificationCode, AuthToken, Email

verify_code_blueprint = Blueprint('verify_code_blueprint', __name__, template_folder='templates')


@verify_code_blueprint.route('/verify', methods=['GET', 'POST'])
def enter_verification_code():
    is_verified = request.args.get('is_verified')
    is_code_valid = request.args.get('is_code_valid')
    return render_template('verify.html', is_code_valid=is_code_valid, is_verified=is_verified)


@verify_code_blueprint.route('/validate_code', methods=['POST'])
def validate_code():
    input_code = request.form['verification']
    code = VerificationCode.query.filter_by(verification_code=input_code).first()

    if code:
        email = Email.query.filter_by(email=session['user_email']).first()
        email.is_verified = True
        auth_token = AuthToken(email=email)
        db.session.add(auth_token)
        db.session.commit()
        return redirect(url_for('your_api_token_blueprint.your_api_token', auth_token=auth_token))

    else:
        return redirect(url_for('verify_code_blueprint.enter_verification_code', is_code_valid=False))
