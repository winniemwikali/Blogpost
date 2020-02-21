from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, DataRequired


class PostForm(FlaskForm):
    CATEGORIES=[('FASHION & BEAUTY', 'FASHION & BEAUTY'), ('ART', 'ART'), ('CAREER & FINANCE', 'CAREER & FINANCE'), ('MOTHERHOOD', 'MOTHERHOOD'), ('GAMING', 'GAMING'), ('MUSIC', 'MUSIC')]
    category=SelectField("CATEGORIES",choices=CATEGORIES)
    title=StringField("TITLE",validators=[DataRequired()])
    post=TextAreaField("BLOG",validators=[Required()])
    submit = SubmitField('Publish Now')


class CommentForm(FlaskForm):
    comment = TextAreaField('')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')