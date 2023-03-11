import flask
import random
app = flask.Flask(__name__)
number_add = 'https://media3.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e478gwvs85vec5c8vhiexcbsc2yduebhkhnhiovebuh&rid=giphy.gif&ct=g'
too_much = 'https://media3.giphy.com/media/fQoIDlLW6A6BAhyev8/giphy.gif?cid=ecf05e47sgbdzwizl28rexkigyq7xt23xeyqju43zc4e7g42&rid=giphy.gif&ct=g'
too_small = 'https://media3.giphy.com/media/j5bsZqX1KTKngMyu90/giphy.gif?cid=ecf05e471iesq9c4oyw433kx7slsqiy5co5hbjfs1v8gakuw&rid=giphy.gif&ct=g'
correct = 'https://media0.giphy.com/media/l1J9wXoC8W4JFmREY/giphy.gif?cid=ecf05e47io5ek6fp16552nkpht44sfah9mi32cpkeeakzrld&rid=giphy.gif&ct=g'
number = random.randint(0, 9)
@app.route('/')
def home():
    global number_add
    text = f'<center><h1> Guess Any Digits</h1><br><img src={number_add}></center>'
    return text

@app.route('/<digit>')
def guess(digit):
    digit = int(digit)
    global number, correct, too_much, too_small
    if digit == number:
        answer = f'<center><img src={correct}></center>'
        return answer
    elif digit > number:
        return f'<center><h1>really!!</h1><br><img src={too_much}></center>'
    else:
        return f'<center><h1>Oh!! Come on?</h1><br><img src={too_small}></center>'

if __name__ == '__main__':
    app.run()
