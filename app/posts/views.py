# app/posts/views.py
from flask import render_template, request, redirect, url_for
from app.posts import posts_blueprint
from app.posts.forms import PostForm  # Correct relative import
from app.models import Posts, db

@posts_blueprint.route('/create', methods=['GET', 'POST'])
def posts_create():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(
            name=form.name.data,
            description=form.description.data,
            image=form.image.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.posts_list'))
    return render_template('posts/create.html', form=form)

@posts_blueprint.route('/', methods=['GET'])
def posts_list():
    posts = Posts.query.all()
    return render_template('posts/list.html', posts=posts)

@posts_blueprint.route('/<int:id>', methods=['GET'])
def post_show(id):
    post = Posts.query.get_or_404(id)
    return render_template('posts/show.html', post=post)

@posts_blueprint.route('/<int:id>/update', methods=['GET', 'POST'])
def posts_update(id):
    post = Posts.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.name = form.name.data
        post.description = form.description.data
        post.image = form.image.data
        db.session.commit()
        return redirect(url_for('posts.post_show', id=post.id))
    return render_template('posts/update.html', form=form, post=post)

@posts_blueprint.route('/<int:id>/delete', methods=['POST'])
def posts_delete(id):
    post = Posts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.posts_list'))
