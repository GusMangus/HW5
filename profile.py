from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h1 style=" color: red"> Роберт Оппенгеймер </h1> 
    </br>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/JROppenheimer-LosAlamos.jpg/375px-JROppenheimer-LosAlamos.jpg" alt="Фтотография" />
    </br>
    <h2> Эта страница посвящена <a href="https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%BF%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D0%BC%D0%B5%D1%80,_%D0%A0%D0%BE%D0%B1%D0%B5%D1%80%D1%82"> Роберту Оппенгеймеру </a> </h2>
    <p> Оппенгеймера часто называют <del> отцом атомной бомбы</del>.</br>
    Но он также известен следующими долстижениями </br>
    <ins>- приближение Борна — Оппенгеймера </ins> для молекулярных волновых функций,</br>
    <ins>-работы по теории электронов и позитронов </ins>,</br>
    <ins>-процесс Оппенгеймера — Филлипс в ядерном синтезе </ins>,</br>
    <strong> - первое предсказание квантового туннелирования</strong>. </br>
    Вместе со своими учениками он внёс важный вклад в современную теорию нейтронных звёзд и чёрных дыр, а также в решение отдельных проблем квантовой механики, квантовой теории поля и физики космических лучей. </br> 
    Оппенгеймер был учителем и пропагандистом науки, отцом-основателем американской школы теоретической физики, получившей мировую известность в 1930-е годы.</p>
    """
    return page_content


app.run()