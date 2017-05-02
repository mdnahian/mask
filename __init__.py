from flask import Flask, request, jsonify
import json
from db import *

app = Flask(__name__)


@app.route('/api/<method>', methods=['GET', 'POST'])
def api(method):
    if request.method == 'POST':
        api_key = request.form['api_key']
        username = request.form['username']

        if api_key is not None and api_key is not '':
            if username is not None and username is not '':
                if method is not None and method is not '':
                    if authenticate(username, api_key):
                        db = get_db()
                        if method is 'create':
                            category = request.form['category']
                            if category is not None and category is not '':
                                if category is 'broadcast':
                                    pass
                                elif category is 'facetime':
                                    pass
                                elif category is 'message':
                                    pass
                                elif category is 'post';
                                    pass
                                else:
                                    return jsonify(
                                        error='category is invalid',
                                        code=107
                                    )
                            else:
                                return jsonify(
                                    error='category not specified',
                                    code=106
                                )
                        elif method is 'get':
                            exesql('SELECT * FROM session ')
                        elif method is 'update':
                            pass
                        elif method is 'destroy':
                            pass
                        else:
                            return jsonify(
                                error='method is invalid',
                                code=105
                            )
                    else:
                        return jsonify(
                            error='',
                            code=104
                        )
                else:
                    return jsonify(
                        error='method not specified',
                        code=103
                    )
            else:
                return jsonify(
                    error='username not specified',
                    code=102
                )
        else:
            return jsonify(
                error='api key not specified',
                code=101
            )
    else:
        return jsonify(
            error='invalid request method',
            code=100
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
