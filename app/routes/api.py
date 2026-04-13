from flask import Blueprint, request, jsonify
from app.models import Company, Client, Venue, Vehicle, FuelType, Product, ProductExtra, Skill, Staff


api_bp = Blueprint('api', __name__)

@api_bp.route("/api/clients")
def api_clients():
    company_id = request.args.get("company_id", type=int)
    if company_id:
        clients = Client.query.filter_by(company_id=company_id).all()
    else:
        clients = Client.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in clients])


@api_bp.route("/api/venues")
def api_venues():
    client_id = request.args.get("client_id", type=int)
    if client_id:
        client = Client.query.get(client_id)
        venues = client.venues if client else []
    else:
        venues = []
    return jsonify([{"id": v.id, "name": v.name} for v in venues])