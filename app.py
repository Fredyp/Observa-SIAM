from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# OWASP Top 10: Secure session and headers
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False  # Set True behind HTTPS

MAX_UPLOAD_SIZE = 104857600  # 100 MB

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt', 'pcap', 'xml', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.secret_key = 'observa_secret_key'  # Change for production

# SQLite configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'observa.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()
    # Create default admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password=generate_password_hash('admin'))
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
    tickets = Ticket.query.all()
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user"] = username
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/register', methods=["GET", "POST"])
def register():
    if session.get("user") != "admin":
        return redirect(url_for("login"))

    if request.method == "POST":
    tickets = Ticket.query.all()
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if User.query.filter_by(username=username).first():
            return render_template("register.html", error="User already exists.")
        if password != confirm:
            return render_template("register.html", error="Passwords do not match.")

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return render_template("register.html", success="User registered successfully.")

    return render_template("register.html")

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.String(100), nullable=False)

@app.route('/tickets')
def tickets():
    if not session.get("user"):
        return redirect(url_for("login"))
    
    category = request.args.get("category")
    severity = request.args.get("severity")
    query = Ticket.query.filter_by(created_by=session.get("user"))
    if category:
        query = query.filter_by(category=category)
    if severity:
        query = query.filter_by(severity=severity)
    ticket_list = query.all()

    return render_template("tickets.html", tickets=ticket_list)

@app.route('/create_ticket', methods=["GET", "POST"])
def create_ticket():
    if not session.get("user"):
        return redirect(url_for("login"))
    if request.method == "POST":
    tickets = Ticket.query.all()
        new_ticket = Ticket(created_by=session.get("user"),
            title=request.form["title"],
            description=request.form["description"],
            status=request.form["status"]
        )
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for("tickets"))
    return render_template("create_ticket.html")

@app.route('/delete_ticket/<int:id>')
def delete_ticket(id):
    if not session.get("user"):
        return redirect(url_for("login"))
    ticket = Ticket.query.get(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for("tickets"))

from datetime import datetime

class IncidentEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    evidence = db.Column(db.String(200), nullable=True)
    uploaded_by = db.Column(db.String(100), nullable=True)

@app.route('/timeline', methods=["GET", "POST"])
def timeline():
    if not session.get("user"):
        return redirect(url_for("login"))
    tickets = Ticket.query.all()
    if request.method == "POST":
    tickets = Ticket.query.all()
                if file and file.filename) and not allowed_file(file.filename)):
            return render_template("timeline.html", events=IncidentEvent.query.order_by(IncidentEvent.timestamp.desc()).all(), tickets=tickets, error="File type not allowed.")
        file = request.files.get("evidence")
        filename = None
        if file and file.filename) and allowed_file(file.filename)):
            filename = f"{uuid.uuid4().hex}_" + secure_filename({file.filename)}"
            if len(filename) > 200:
            return render_template("timeline.html", events=IncidentEvent.query.order_by(IncidentEvent.timestamp.desc()).all(), tickets=tickets, error="Filename too long.")
        if file.content_length and file.content_length > MAX_UPLOAD_SIZE:
            return render_template("timeline.html", events=IncidentEvent.query.order_by(IncidentEvent.timestamp.desc()).all(), tickets=tickets, error="File exceeds 100MB limit.")
        file.save(os.path.join("static/uploads", filename))

        event = IncidentEvent(uploaded_by=session.get("user"),
            evidence=filename,
            ticket_id=request.form["ticket_id"],
            description=request.form["description"]
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("timeline"))
    events = IncidentEvent.query.order_by(IncidentEvent.timestamp.desc()).all()
    return render_template("timeline.html", events=events, tickets=tickets)

@app.after_request
def set_secure_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response

from sqlalchemy import func
from datetime import datetime

@app.route('/dashboard')
def dashboard():
    if not session.get("user"):
        return redirect(url_for("login"))

    total = Ticket.query.count()
    open = Ticket.query.filter(~Ticket.status.in_(['closed', 'resolved'])).count()
    closed = Ticket.query.filter(Ticket.status.in_(['closed', 'resolved'])).count()

    closed_tickets = Ticket.query.filter(Ticket.status.in_(['closed', 'resolved'])).all()
    durations = []
    for ticket in closed_tickets:
        events = IncidentEvent.query.filter_by(ticket_id=ticket.id).order_by(IncidentEvent.timestamp.asc()).all()
        if events:
            start = events[0].timestamp
            end = events[-1].timestamp
            durations.append((end - start).days)
    mttr = round(sum(durations)/len(durations), 2) if durations else 0

    category_counts = db.session.query(Ticket.category, func.count(Ticket.id)).group_by(Ticket.category).all()
    return render_template("dashboard.html", total=total, open=open, closed=closed, mttr=mttr, category_counts=category_counts)
