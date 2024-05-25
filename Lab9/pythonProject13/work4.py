from flask import Flask, render_template, url_for
app = Flask(__name__)
menu = ["Установка", "Первое приложение", "Обратная связь"]
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

@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

if __name__ == "__main__":
    app.run(debug=True)

# with app.test_request_context():
#     print(url_for('profile', username="selfedu"))
# with app.test_request_context():
# print( url_for('index') )
# искусственный вызов контекста запроса без активации веб-сервера


# url-адреса как переменные
# @app.route("/profile/<int:username>")