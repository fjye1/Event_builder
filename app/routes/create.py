from flask import Blueprint, render_template, url_for, redirect, flash
from app.extensions import db
from app.models import Company, Client
from app.forms import EventForm, CompanyForm, ClientForm

create_bp = Blueprint('create', __name__)


@create_bp.route("/create")
def home():
    return render_template(
        "create/home.html")


@create_bp.route("/create/company" , methods=['GET', 'POST'])
def company():
    form = CompanyForm()

    if form.validate_on_submit():
        new_company = Company(
            name=form.name.data,
        )
        db.session.add(new_company)
        db.session.commit()
        return redirect(url_for('home.index'))

    return render_template(
        "create/company.html", form=form)


@create_bp.route("/create/client", methods=['GET', 'POST'])
def client():
    form = ClientForm()

    companies = Company.query.all()
    form.company_id.choices = [(c.id, c.name) for c in companies]

    if not companies:
        flash("No companies found. Please create a company first.", "warning")
        return redirect(url_for('create.company'))


    if form.validate_on_submit():
        new_client = Client(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            company_id=form.company_id.data
        )

        db.session.add(new_client)
        db.session.commit()

        return redirect(url_for('home.index'))

    return render_template("create/client.html", form=form)



@create_bp.route("/create/event")
def event():
    form = EventForm()
    return render_template(
        "create/event.html",
        form=form)
