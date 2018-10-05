from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True 



tasks = []

@app.route('/', methods=['POST','GET'])
def index():

    #check the type of request that's coming in. POST or GET

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)


    return render_template('todos.html', title="Get It Done!", tasks=tasks)

app.run()