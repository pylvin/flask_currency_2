from views.all_views import index

from initialize import app,db
app.add_url_rule('/',view_func=index,methods=['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True)
