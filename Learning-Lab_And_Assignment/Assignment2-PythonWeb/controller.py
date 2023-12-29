import os
import datetime
from datetime import date
from form import AddBlogForm,DeleteBlogForm,SelectEditBlogForm,EditBlogForm
from flask import Flask,render_template,url_for,redirect,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api


#################################
###     Initialize       ########
#################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app, db)
api = Api(app)


#################################
###           Models     ########
#################################
class BlogPost(db.Model):
    __tablename__ = 'BlogPost'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    author = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    content = db.Column(db.Text)

    def __init__(self,title,subtitle,author,date_posted,content):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date_posted = date_posted
        self.content = content

    def json(self, urlHost):
        blogUrl = urlHost + '/post/' + str(self.id)
        return {'id':self.id,
                'title':self.title,
                'subtitle':self.subtitle,
                'author':self.author,
                'date_posted':self.date_posted.strftime('%d/%m/%Y'),
                'url':blogUrl}


#################################
###   View Functions     ########
#################################
@app.route('/')
def index():
    blogList = BlogPost.query.all()
    return render_template('HomePage.html', blogList=blogList)

@app.route('/delete', methods=['GET', 'POST'])
def delete_post():
    blogList = BlogPost.query.all()
    form = DeleteBlogForm()
    if form.validate_on_submit():
        id = request.form.get('idDelete')
        post = BlogPost.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('index'))
    print(form.id.data)
    return render_template('DeleteNewPostPage.html', blogList=blogList, form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    form = AddBlogForm()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        author = form.author.data
        date_posted = date.today()
        content = form.content.data

        newPost = BlogPost(title,subtitle,author,date_posted,content)
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('AddNewPostPage.html', form=form)

@app.route('/post/<id>')
def view_post(id):
    blog= BlogPost.query.get(id)
    return render_template('BlogContent.html', blog=blog)

@app.route('/editList', methods=['GET', 'POST'])
def editList_post():
    blogList = BlogPost.query.all()
    form = SelectEditBlogForm()
    if form.validate_on_submit():
        id = request.form.get('idEdit')
        return redirect(url_for('editPage_post', id=id))
    return render_template('EditBlogListPage.html', blogList=blogList, form=form)

@app.route('/editList/<id>', methods=['GET', 'POST'])
def editPage_post(id):
    blog= BlogPost.query.get(id)
    form = EditBlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.author = form.author.data
        blog.date_posted = date.today()
        blog.content = form.content.data

        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('EditContent.html', form=form, blog=blog)


#################################
#####            API     ########
#################################
class BlogApi(Resource):
    def get(self):
        blogList = BlogPost.query.all()
        urlHost = request.host
        return [blog.json(urlHost) for blog in blogList]

api.add_resource(BlogApi,'/listBlog')


#################################
###   Run Application    ########
#################################
if __name__ == '__main__':
    app.run(debug=True)
