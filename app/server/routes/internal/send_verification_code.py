# ------- standard library imports -------
import re

# ------- 3rd party imports -------
from flask_mail import Mail, Message
from flask import Blueprint, request, redirect, url_for, session

# ------- local imports -------
from app import app
from app.server.db.extensions import db
from app.server.db.models import VerificationCode, Email

send_otp_blueprint = Blueprint('send_otp_blueprint', __name__)


@send_otp_blueprint.route('/email_validation', methods=['POST'])
def email_validation():
    input_email = request.form['email']
    pattern = r'[^@]+@[^@]+\.[^@]+'
    is_email_valid = re.match(pattern, input_email)

    if is_email_valid:
        email = Email.query.filter_by(email=input_email).first()

        if email and email.is_verified:
            auth_token = Email.query.filter_by(email=input_email).first().auth_token
            return redirect(url_for('your_api_token_blueprint.your_api_token', auth_token=auth_token))

        elif email and not email.is_verified:
            return redirect(url_for('verify_code_blueprint.enter_verification_code', is_verified=False))

        else:
            if not email:
                session['user_email'] = input_email

                email = Email(email=input_email)
                verification_code = VerificationCode(email=email)
                db.session.add(verification_code, email)
                db.session.commit()

                # print('user added to db')
                # print('verification_code:')
                # print(verification_code)
                # print('*' * 33)

                mail = Mail(app.app)
                msg = Message('ShortMe Verification Code', sender='shortme.biz@gmail.com', recipients=[email.email])
                msg.body = str(f'Hi!\nThis is your verification code: {verification_code.verification_code}')
                mail.send(msg)
                return redirect(url_for('verify_code_blueprint.enter_verification_code'))
