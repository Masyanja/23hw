from flask import Blueprint, request, jsonify
from flask_restx import ValidationError

from builder import build_query, build_query_2
from models import RequestParams
import functions

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():

    try:
        params = RequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    result = build_query(
        cmd=params['cmd1'],
        param=params['value1'],
    )
    result = build_query_2(cmd=params['cmd2'],
                           param=params['value2'], res_data=result)
    return jsonify(result)

