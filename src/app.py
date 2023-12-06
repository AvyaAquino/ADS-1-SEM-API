from flask import Flask, render_template

app = Flask('__name__', static_folder='static')

#home

@app.route('/')
def home():
    return render_template('/home/home.html', titulo='Treinamento Scrum', previous='', next='scrum')

#Tópicos

@app.route('/scrum')
def scrum():
    return render_template('/scrum/scrum.html', titulo='Scrum: O método Ágil', previous='', next='scrumTeam')

@app.route('/scrumTeam')
def scrumTeam():
    return render_template('/scrumTeam/scrumTeam.html', titulo='Scrum Team', previous='scrum', next='productOwner')

@app.route('/processos')
def processos():
    return render_template('/processos/processos.html', titulo='Processos', previous='scrumTeam', next='scrumDaily')

@app.route('/artefatos')
def artefatos():
    return render_template('/artefatos/artefatos.html', titulo='Artefatos', previous='processos', next='productBacklog')

@app.route('/pacer')
def pacer():
    return render_template('/pacer/pacer.html', titulo='Avaliação Pacer', previous='artefatos', next='pacer')

#sub Tópicos

    #Scrum Team
@app.route('/productOwner')
def productOwner():
    return render_template('/scrumTeam/productOwner.html', titulo='Product Owner', previous='scrumTeam', next='scrumMaster')

@app.route('/scrumMaster')
def scrumMaster():
    return render_template('/scrumTeam/scrumMaster.html', titulo='Scrum Master', previous='productOwner', next='devTeam')

@app.route('/devTeam')
def devTeam():
    return render_template('/scrumTeam/devTeam.html', titulo='Dev Team', previous='scrumMaster', next='devTeam')

    #Processos

@app.route('/scrumDaily')
def scrumDaily():
    return render_template('/processos/scrumDaily.html', titulo='Scrum Daily', previous='processos', next='sprintPlanning')

@app.route('/sprintPlanning')
def sprintPlanning():
    return render_template('/processos/sprintPlanning.html', titulo='Sprint Planning', previous='scrumDaily', next='sprintReview')

@app.route('/sprintReview')
def sprintReview():
    return render_template('/processos/sprintReview.html', titulo='Sprint Review', previous='sprintPlanning', next='sprintReview')

    #Artefatos

@app.route('/productBacklog')
def productBacklog():
    return render_template('/artefatos/productBacklog.html', titulo='Product Backlog', previous='artefatos', next='sprintBacklog')

@app.route('/sprintBacklog')
def sprintBacklog():
    return render_template('/artefatos/sprintBacklog.html', titulo='sprintBacklog', previous='productBacklog', next='dor')

@app.route('/dor')
def dor():
    return render_template('/artefatos/dor.html', titulo='Definition of Ready', previous='sprintBacklog', next='incremento')

@app.route('/incremento')
def incremento():
    return render_template('/artefatos/incremento.html', titulo='Incremento', previous='dor', next='burndownChart')

@app.route('/burndownChart')
def burndownChart():
    return render_template('/artefatos/burndownChart.html', titulo='Burndown Chart', previous='incremento', next='burndownChart')


if __name__ == '__main__':
    app.run(debug=True)