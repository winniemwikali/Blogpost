from flask import render_template, request, redirect, url_for,abort
from ..requests import get_quote
from flask_login import login_required
from . import main
from ..models import Comment, User, Post
from .forms import CommentForm, UpdateProfile, PostForm
from flask_login import login_required,current_user
from ..import db,photos


@main.route("/",methods=["GET","POST"])
def index():
    random_quote = get_quote()
    categories=["ART", "FINANCE", "GAMING", "MUSIC"]
    return render_template('index.html',categories = categories,quotes=random_quote)


@main.route("/blog/<string:category>")
def posts(category):
    posts=list(Post.query.filter_by(category=category))
    return render_template("/blog.html",posts=posts)


@main.route("/post",methods=["GET","POST"])
@login_required
def add():
    post_form=PostForm()
    if post_form.validate_on_submit():
        post=Post(title=post_form.title.data, text=post_form.post.data,category=post_form.category.data, user_id=current_user.id, username=current_user.username)
        
        post.save_post()
        return redirect(url_for("main.index"))
    return render_template('./post.html',post_form=post_form)


@main.route("/delete/<int:id>",methods=["GET","POST"])
@login_required
def delete(id):
    deleted = Post.query.filter_by(id=id).first()
    db.session.delete(deleted)
    db.session.commit()
    return redirect (url_for('main.index'))


@main.route("/commentDelete/<int:id>",methods=["GET","POST"])
@login_required
def delete_comment(id):
    deleted_comment = Comment.query.filter_by(id=id).first()
    db.session.delete(deleted_comment)
    db.session.commit()
    return redirect (url_for('main.index'))
  


@main.route('/comment/new/<int:post_id>', methods=['GET', 'POST'])
@login_required
def new_comment(post_id):
    form = CommentForm()
    post = Post.query.filter_by(id=post_id).first()

    if form.validate_on_submit():
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(text=comment,user_id=current_user.id, post_id=post_id)

        # save review method
        db.session.add(new_comment)
        db.session.commit()
        
       
    all_comments = Comment.query.filter_by(post_id=post_id).all()
    
    return render_template('comment.html',form=form, comments=all_comments, post=post)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))






    

