from flask import Flask, jsonify,  request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# initializes a new Flask application. app is the main object for your web application.
app = Flask(__name__)   

# sets the configuration for the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xxxx@localhost:xxxx/notes'
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False

# This line initializes the SQLAlchemy object with the Flask application. 
# db is the object used to interact with the database.
db = SQLAlchemy(app)

# This line initializes the Marshmallow object with the Flask application. 
# ma is used for serializing and deserializing the database models.
ma = Marshmallow(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(100))

    def __init__(self,title,body):
        self.title = title
        self.body = body
    
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body')


# These lines create instances of the ArticleSchema:
# article_schema is used for serializing/deserializing a single Article object,
# articles_schema is used for serializing/deserializing multiple Article objects (hence the many=True argument).
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@app.route('/add', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']
    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@app.route('/get', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)


@app.route('/update/<id>/', methods=['PUT'])
def update_articles(id):
    article = Articles.query.get(id)
    title =  request.json['title']
    body = request.json['body']
    article.title = title
    article.body = body
    db.session.commit()
    return article_schema.jsonify(article)

@app.route('/delete/<id>/', methods=['DELETE'])
def delete_articles(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)

if __name__ == '__main__':
    app.run(debug=True)