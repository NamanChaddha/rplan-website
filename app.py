from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Portfolio data mapping dictionary register
PROJECT_DATABASE = {
    'tata': {
        'main': "Project - Construction of Fibre Glass manufacturing Plant for Owens Corning India Limited, (US$ 50 Million) Navi Mumbai (India).",
        'sub': "Handled all mechanical contracts closures for this project at the completion stage."
    },
    'eta': {
        'main': "Project - Construction of Essar Oil Refinery – (10MTPA) Jamnagar (India). Expediting OSBL units’ Construction.",
        'sub': "Supervised the track laid piping between Utilities to various units and cross country pipelines."
    },
    'nbtc': {
        'main': "Project - Clean Fuels Project (CFP) & Petrochemical Piping Packages for NBTC Group, Kuwait.",
        'sub': "Managed operational timeline schedules, advanced resource leveling, and heavy heavy-lift construction tracking."
    },
    'kentech': {
        'main': "Project - Electrical & Instrumentation (E&I) Infrastructure Setup for Major Energy Assets with Kentech Group.",
        'sub': "Supervised strict testing packages, QA/QC system handovers, and technical milestone declarations."
    },
    'qatar': {
        'main': "Project - Plant Expansion Engineering, Procurement & Construction Closeouts for Qatar Engineering & Construction Company W.L.L.",
        'sub': "Led complex turnaround scheduling (TA Planning), system logic diagnostics, and structural asset lifecycle handovers."
    },
    'alhassan': {
        'main': "Project - Cross-Country Cross-Border Pipeline Systems & Industrial Utilities Infrastructure for Al Hassan Engineering Company Abu Dhabi LLC.",
        'sub': "Managed contractual clearance updates, multi-system bifurcations, and final engineering log wrap-ups."
    },
    'fiber_glass': {
        'main': "Project - Construction of Fibre Glass manufacturing Plant for Owens Corning India Limited, (US$ 50 Million) Navi Mumbai (India).",
        'sub': "Handled all mechanical contracts closures for this project at the completion stage."
    },
    'refinery': {
        'main': "Project - Construction of Essar Oil Refinery – (10MTPA) Jamnagar (India).",
        'sub': "Supervised the track laid piping between Utilities to various units."
    }
}

@app.route('/')
def home():
    """Renders the main expert project consultancy homepage."""
    return render_template('index.html')

@app.route('/portfolio')
def tce():
    """Renders the standalone dedicated historical track record page."""
    return render_template('tce.html')

@app.route('/api/project/<string:company_key>')
def get_project_details(company_key):
    lookup_key = company_key.lower().strip()
    if lookup_key in PROJECT_DATABASE:
        return jsonify({'success': True, 'data': PROJECT_DATABASE[lookup_key]}), 200
    return jsonify({'success': False, 'message': 'Project data not located'}), 404
@app.route('/trainings')
def trainings():
    return render_template("trainings.html")
@app.route('/certifications')
def certifications():
    return render_template("certifications.html")
@app.route('/sts')
def sts():
    return render_template("sts.html")
@app.route('/client')
def client():
    return render_template("clients.html")
@app.route('/training_pics')
def training_pics():
    return render_template("exp temp.html")
@app.route('/EPCM_01')
def EPCM_01():  # <--- url_for('check_prof') looks for THIS name
    return render_template('epcm01.html')
@app.route('/EPCM_02')
def EPCM_02():  # <--- url_for('check_prof') looks for THIS name
    return render_template('epcm02.html')
@app.route('/EPCM_03')
def EPCM_03():  # <--- url_for('check_prof') looks for THIS name
    return render_template('epcm03.html')
@app.route('/EPCM_04')
def EPCM_04():  # <--- url_for('check_prof') looks for THIS name
    return render_template('epcm04.html')
@app.route('/EPCM_05')
def EPCM_05():  # <--- url_for('check_prof') looks for THIS name
    return render_template('epcm05.html')
@app.route('/stota_01')
def stota_01():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota01.html')
@app.route('/stota_02')
def stota_02():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota02.html')
@app.route('/stota_03')
def stota_03():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota03.html')
@app.route('/stota_04')
def stota_04():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota04.html')
@app.route('/stota_05')
def stota_05():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota05.html')
@app.route('/stota_06')
def stota_06():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota06.html')
@app.route('/stota_07')
def stota_07():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota07.html')
@app.route('/stota_08')
def stota_08():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota08.html')
@app.route('/stota_09')
def stota_09():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota09.html')
@app.route('/stota_10')
def stota_10():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota10.html')
@app.route('/stota_11')
def stota_11():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota11.html')
@app.route('/stota_12')
def stota_12():  # <--- url_for('check_prof') looks for THIS name
    return render_template('stota12.html')

@app.route('/pmc_01')
def pmc_01():  # <--- url_for('check_prof') looks for THIS name
    return render_template('pmc01.html')
@app.route('/pmc_02')
def pmc_02():  # <--- url_for('check_prof') looks for THIS name
    return render_template('pmc02.html')
@app.route('/pmc_03')
def pmc_03():  # <--- url_for('check_prof') looks for THIS name
    return render_template('pmc03.html')

@app.route('/vision')
def vision():  # <--- url_for('check_prof') looks for THIS name
    return render_template('mission_vision.html')
@app.route('/mission')
def mission():  # <--- url_for('check_prof') looks for THIS name
    return render_template('mission.html')
@app.route('/vision')
def vision():  # <--- url_for('check_prof') looks for THIS name
    return render_template('vision.html')
if __name__ == '__main__':
    app.run(debug=True)
