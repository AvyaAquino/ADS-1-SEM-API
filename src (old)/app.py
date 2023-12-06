from flask import Flask, render_template

app = Flask('__name__', static_folder='static')

@app.route('/')
def Home():
    return render_template('/Home/Home.html', titulo='Treinamento Scrum', previous='', next='Scrum')


@app.route('/Scrum')
def Scrum():
    return render_template('/Scrum/Scrum.html', titulo='Scrum: O método Ágil', previous='', next='Scrum')

@app.route('/ScrumTeam')
def ScrumTeam():
    return render_template('/Scrum Team/ScrumTeam.html', titulo='Scrum Team', previous='ScrumTeam', next='productOwner')
@app.route('/Processos')
def Processos():
    return render_template('/Processos/Processos.html', titulo='Processos', previous='Processos', next='scrumDaily')
@app.route('/Artefatos')
def Artefatos():
    return render_template('/Artefatos/Artefatos.html', titulo='Artefatos', previous='Artefatos', next='productBacklog')
@app.route('/Pacer')
def Pacer():
    return render_template('/Pacer/pacer.html', titulo='Pacer', previous='Artefatos', next='Pacer')

# Sub Topicos
@app.route('/productOwner')
def productOwner():
    return render_template('/Scrum Team/productOwner.html', titulo='Product Owner', previous='ScrumTeam', next='scrumMaster')
@app.route('/scrumMaster')
def scrumMaster():
    return render_template('/Scrum Team/scrumMaster.html', titulo='Scrum Master', previous='productOwner', next='devTeam')
@app.route('/devTeam')
def devTeam():
    return render_template('/Scrum Team/devTeam.html', titulo='Dev Team', previous='scrumMaster', next='devTeam')



@app.route('/scrumDaily')
def scrumDaily():
    return render_template('/Processos/scrumDaily.html', titulo='Scrum Daily', previous='Processos', next='sprintPlanning')
@app.route('/sprintPlanning')
def sprintPlanning():
    return render_template('/Processos/sprintPlanning.html', titulo='Sprint Planning', previous='scrumDaily', next='sprintReview')
@app.route('/sprintReview')
def sprintReview():
    return render_template('/Processos/sprintReview.html', titulo='Sprint Review', previous='sprintPlanning', next='sprintReview')



@app.route('/productBacklog')
def productBacklog():
    return render_template('/Artefatos/productBacklog.html', titulo='Product Backlog', previous='Artefatos', next='sprintBacklog')
@app.route('/sprintBacklog')
def sprintBacklog():
    return render_template('/Artefatos/sprintBacklog.html', titulo='sprintBacklog', previous='productBacklog', next='DOR')
@app.route('/DOR')
def DOR():
    return render_template('/Artefatos/DOR.html', titulo='DOR', previous='sprintBacklog', next='Incremento')
@app.route('/Incremento')
def Incremento():
    return render_template('/Artefatos/Incremento.html', titulo='Incremento', previous='DOR', next='burnDownChart')
@app.route('/burnDownChart')
def burnDownChart():
    return render_template('/Artefatos/burnDownChart.html', titulo='Burndown Chart', previous='Incremento', next='burnDownChart')


if __name__ == '__main__':
    app.run(debug=True)