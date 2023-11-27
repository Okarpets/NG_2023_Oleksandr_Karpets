from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        mas = [['.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.']]
        x = 1
        y = 2
        user = mas[x][y] = '@'
        control = str(request.form['control']) #Get command fron user
        match control:
            case "▶":
                print("▶")
                user = mas[x][y+1] = '▶' #Вправо
            case "◀":
                print("◀")
                user = mas[x][y-1] = '◀' #Влево
            case "▲":
                print("▲")
                user = mas[x-1][y] = '▲' #Вверх
            case "▼":
                print("▼")
                user = mas[x+1][y] = '▼' #Вниз
            case "◢":
                print("◢")
                user = mas[x+1][y+1] = '◢' #Вниз-право
            case "◣":
                print("◣")
                user = mas[x+1][y-1] = '◣' #Вниз-лево
            case "◤":
                print("◤")
                user = mas[x-1][y-1] = '◤' #Вверх-лево
            case "◥":
                print("◥")
                user = mas[x-1][y+1] = '◥' #Вверх-право
        html = '<table>'
        for row in mas:
            html += '<tr>'
            for value in row:
                html += '<td>{}</td>'.format(value)
            html += '</tr>'
        html += '</table>'
        
        html = html.replace('<>', '')
        print(html)
        return render_template("index.html", user=user, html=str(html))


if __name__ == "__main__":
  app.run(debug=True)