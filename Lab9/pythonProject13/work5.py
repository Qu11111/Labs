from flask import Flask, render_template, url_for, request
app = Flask(__name__)
menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]
@app.route("/")
def index():
    with app.test_request_context():
        print(url_for('index'))
    return render_template('index.html', menu = menu)
@app.route("/about")
def about():
    with app.test_request_context():
        print(url_for('about'))
    return render_template('about.html', title = "О сайте", menu = menu)
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form['username'])
    return render_template("contact.html", title = "Обратная связь", menu=menu)
if __name__ == "__main__":
    app.run(debug=True)

with app.test_request_context():
    print(url_for('profile', username="selfedu"))
# with app.test_request_context():
# print( url_for('index') )
# искусственный вызов контекста запроса без активации веб-сервера

# @app.route("/profile/<username>")
# def profile(username):
# return f"Пользователь: {username}"
# url-адреса как переменные
# @app.route("/profile/<int:username>")