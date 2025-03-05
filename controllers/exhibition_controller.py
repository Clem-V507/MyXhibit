from flask import Blueprint, render_template, request, redirect, url_for
from models.exhibition import Exhibition, Artwork

exhibition_bp = Blueprint('exhibition', __name__, template_folder='../templates')

# Stockage temporaire des expositions (pour une implémentation plus poussée, utilisez une base de données)
exhibitions = []

@exhibition_bp.route('/')
def index():
    return render_template('index.html', exhibitions=exhibitions)

@exhibition_bp.route('/exhibition/<int:exhibition_id>')
def exhibition_detail(exhibition_id):
    if exhibition_id < len(exhibitions):
        exhibition = exhibitions[exhibition_id]
        return render_template('exhibition_detail.html', exhibition=exhibition, exhibition_id=exhibition_id)
    else:
        return "Exposition non trouvée", 404

@exhibition_bp.route('/create_exhibition', methods=['GET', 'POST'])
def create_exhibition():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        new_exhibition = Exhibition(title, description)
        exhibitions.append(new_exhibition)
        return redirect(url_for('exhibition.index'))
    return render_template('create_exhibition.html')

@exhibition_bp.route('/exhibition/<int:exhibition_id>/add_artwork', methods=['GET', 'POST'])
def add_artwork(exhibition_id):
    if exhibition_id < len(exhibitions):
        exhibition = exhibitions[exhibition_id]
        if request.method == 'POST':
            title = request.form.get('title')
            image_url = request.form.get('image_url')
            description = request.form.get('description')
            new_artwork = Artwork(title, image_url, description)
            exhibition.add_artwork(new_artwork)
            return redirect(url_for('exhibition.exhibition_detail', exhibition_id=exhibition_id))
        return render_template('add_artwork.html', exhibition=exhibition)
    else:
        return "Exposition non trouvée", 404
