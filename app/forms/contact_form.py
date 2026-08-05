from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import(
    DataRequired,
    Email,
    Length
)
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed
class ContactForm(FlaskForm):

    name = StringField(
        "Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=255)
        ]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(max=1000)
        ]
    )

    attachment = FileField(
        "Attachment",
        validators=[
            FileAllowed(
                ["pdf", "png", "jpg", "jpeg", "txt"],
                "Unsupported file type.",
            )
        ],
    )

    submit = SubmitField("Send")