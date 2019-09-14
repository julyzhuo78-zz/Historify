from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

from gensim.summarization.summarizer import summarize

app = FlaskAPI(__name__)


notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

data = {
    0: {'name': 'Ada Lovelace', 'dob': 'December 10, 1815',
        'previous_observations': [{'date': 'September 14, 2019', 
                                   'observation': 'healthy'}, 
                                   {'date': 'September 13, 2019',
                                   'observation': 'flu'}],
        'current_observation': ''},
    1: {'name': 'Grace Hopper', 'dob': 'December 9, 1906',
        'previous_observations': [{'date': 'September 12, 2019',
                                    'observation': 'healthy'},
                                    {'date': 'September 11, 2019',
                                    'observation': 'healthy'}],
        'current_observation': ''},
    2: {'name': 'Katherine Johnson', 'dob': 'August 26, 1918',
        'previous_observations': [{'date': 'September 10, 2019',
                                    'observation': 'cold'}],
        'current_observation': ''}
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


def data_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'data': data[key]
    }


@app.route("/", methods=['GET', 'POST'])
def data_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        # name = str(request.data.get('name', ''))
        # raw_text = str(request.data.get('text', ''))

        # idx = max(data.keys()) + 1
        # data[idx] = {}

        # note = str(request.data.get('text', ''))
        # idx = max(notes.keys()) + 1
        # notes[idx] = summarize(note)
        # return data_repr(idx), status.HTTP_201_CREATED
        return status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    return [data_repr(i) for i in sorted(data.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


if __name__ == "__main__":
    app.run(debug=True)
