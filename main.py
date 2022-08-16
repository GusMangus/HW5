from flask import Flask, render_template
from functions import load_candidates_from_json, get_candidates_by_id, get_candidates_by_name, get_candidates_by_skill
import json

app = Flask(__name__)

@app.route('/')
def candidate():
    candidates= load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:id>')
def get_candidate(id):
    candidate = get_candidates_by_id(id)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_candidates_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skills/<skill_name>')
def get_skills(skill_name):
    skill_name = skill_name.lower()
    candidates = get_candidates_by_skill(skill_name)
    return render_template('search.html', candidates=candidates)


if __name__ == "__main__":
    app.run(port=1984)