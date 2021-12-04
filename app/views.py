from app import db
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Cert, Tag
from werkzeug.utils import secure_filename
import json

views = Blueprint("views", __name__)



@views.route("/catalog")
def cert_catalog():
    certs = get_certs()
    path = "app/static/images/"
    for cert in certs:
        with open(path + cert.img_name, "wb") as binary_file:
            # save files to images folder
            # TODO: is there a way to make images saved to server?
            binary_file.write(cert.img)
    return render_template("catalog.html", certs=certs, user=current_user)


@views.route("/")
@login_required
def home():
    return render_template(
        "home.html", title="Certalog", url="localhost:5000", user=current_user
    )


@views.route("/create")
def create_thoughts():
    return render_template("create-thought.html", user=current_user)


@views.route("/success")
def success():
    return render_template("success.html", user=current_user)


@views.route("/upload", methods=["GET", "POST"])
def upload_cert():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        img = request.files["img"]
        notes = request.form.get("notes")
        tag_string = request.form.get("tags")

        tags = process_form_data(tag_string)

        img_name = secure_filename(img.filename)

        if not img:
            return "No picture is uploaded", 400

        new_cert = Cert(
            title=title,
            author=author,
            img=img.read(),
            img_name=img_name,
            img_mimetype=img.mimetype,
            notes=notes,
            user_id=current_user.id,
            tags=tags,
        )

        # add to database here
        db.session.add(new_cert)
        db.session.commit()

    return render_template("success.html", user=current_user)


def get_tags_from_string(tag_string):
    raw_tags = tag_string.split(",")

    # filter out any empty tag names
    tag_names = [name.strip() for name in raw_tags if name.strip()]

    # query the database and retrieve any tags we have already saved
    existing_tags = Tag.query.filter(Tag.name.in_(tag_names))

    # determine which tag names are new
    new_names = set(tag_names) - set([tag.name for tag in existing_tags])

    # create a list of unsaved Tag instances for the new tags
    new_tags = [Tag(name=name) for name in new_names]

    # return all existing tags + all the new, unsaved tags
    return list(existing_tags) + new_tags


def process_form_data(value_form):
    if value_form:
        return get_tags_from_string(value_form)
    else:
        return []


def get_certs():
    return Cert.query.order_by(Cert.date_added).all()


@views.route("/<int:id>")
def get_cert(id):
    curr_cert = Cert.query.filter_by(id=id).first()
    if not curr_cert:
        return "Cert not found"
    return render_template("cert-details.html", cert=curr_cert, user=current_user)


@views.route("/delete", methods=["POST"])
def delete_cert():
    # get the json response from the delete button
    cert = json.loads(request.data)
    # get the cert id
    certId = cert["certId"]
    # use that cert id to query the database
    cert = Cert.query.get(certId)

    # if we found the cert with that id
    if cert:
        # we check if the cert's user id is the same as the current user id
        if cert.user_id == current_user.id:
            db.session.delete(cert)
            db.session.commit()
    return jsonify({})


@views.route("/search", methods=["GET", "POST"])
def search_cert():
    if request.method == "POST":
        data = request.form.get("tag")
        print(data)
        filtered_certs = Cert.query.filter(Cert.tags.any(Tag.name.contains(data))).all()
    return render_template("catalog.html", certs=filtered_certs, user=current_user)



