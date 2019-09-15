from flask import request, url_for, redirect
from flask_api import FlaskAPI, status, exceptions
# import flask_login

from gensim.summarization.summarizer import summarize

app = FlaskAPI(__name__)
app.secret_key = 'super secret string'


# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email

#     # DO NOT ever store passwords in plaintext and always compare password
#     # hashes using constant-time comparison!
#     user.is_authenticated = request.form['password'] == users[email]['password']

#     return user


# data = {
#     0: {'name': 'Ada Lovelace', 'dob': 'December 10, 1815',
#         'observations': [{'date': 'September 14, 2019', 
#                                    'observation': 'healthy'}, 
#                                    {'date': 'September 13, 2019',
#                                    'observation': 'flu'}],
#         'current_observation': ''},
#     1: {'name': 'Grace Hopper', 'dob': 'December 9, 1906',
#         'previous_observations': [{'date': 'September 12, 2019',
#                                     'observation': 'healthy'},
#                                     {'date': 'September 11, 2019',
#                                     'observation': 'healthy'}],
#         'current_observation': ''},
#     2: {'name': 'Katherine Johnson', 'dob': 'August 26, 1918',
#         'previous_observations': [{'date': 'September 10, 2019',
#                                     'observation': 'cold'}],
#         'current_observation': 'blah'}
# }

data = {
    0: {'ptName': '',
        'cheifComplaint': '',
        'onset': '',
        'quality': '',
        'radiate': '',
        'severity': '',
        'dejavu': '',
        'assoc': '',
        'aggrov': '',
        'allev': '',
        'function': '',
        'concern': '',
        'feel': '',
        'expect': '',
        'allergies': '',
        'surgeries': '',
        'illness': '',
        'hospital': '',
        'medication': '',
        'altTher': '',
        'momfhx': '',
        'dadfhx': '',
        'significant': '',
        'occupation': '',
        'underling': '',
        'livingSit': '',
        'smoke': '',
        'alcohol': '',
        'drugs': '',
        'sleep': '',
        'exercise': '',
        'diet': ''}
}

keys = ['ptName', 'cheifComplaint', 'onset', 'quality', 'radiate',
        'severity', 'dejavu', 'assoc', 'aggrov', 'allev', 'function',
        'concern', 'feel', 'expect', 'allergies', 'surgeries',
        'illness', 'hospital', 'medication', 'altTher', 'momfhx',
        'dadfhx', 'significant', 'occupation', 'underling',
        'livingSit', 'smoke', 'alcohol', 'drugs', 'sleep',
        'exercise', 'diet']

# mrns = {'Ada Lovelace': 0,
#        'Grace Hopper': 1,
#        'Katherine Johnson': 2}


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
        # Only add data to existing patients
        # Assume that all patients are in the MRN database
        # TODO: read in POST object as a dictionary and iterate through to add values
        # for k, v in request.data.items():
        #     print(k, v)

        post_input = request.data

        for k, v in post_input.items():
            data[len(data.keys()) - 1][k] = v

    #     for k in keys:

    #     name = str(request.data.get('ptName', ''))

    #     
    #     name = post_input['ptName']
    #     # raw_text = str(request.data.get('text', ''))

    #     if name in mrns.values():
    #         mrn = mrns[name]

    #         observation_val = ['Chief complaint: {}'.format(post_input['cheifComplaint']),
    #                         'Onset: {}'.format(post_input['onset']),
    #                         'Quality: {}'.format(post_input['quality'])]

    #         # if data[mrn]['current_observation'] != '':
    #         #     data[mrn]['previous_observations'].append({'date': 'September 14, 2019',
    #         #         'observation': data[mrn]['current_observation']})
    #     else:
    #         raise exceptions.NotFound()

    #     # data[mrn]['current_observation'] = summarize(raw_text)

    #     # return data_repr(mrn), status.HTTP_201_CREATED

    # print('here')
    # request.method == 'GET'
    return [data_repr(i) for i in sorted(data.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        # note = str(request.data.get('text', ''))
        # notes[key] = note
        # return note_repr(key)
        raise exceptions.NotFound()

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in data:
        raise exceptions.NotFound()
    return data_repr(key)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return '''
#                <form action='login' method='POST'>
#                 <input type='text' name='email' id='email' placeholder='email'/>
#                 <input type='password' name='password' id='password' placeholder='password'/>
#                 <input type='submit' name='submit'/>
#                </form>
#                '''

#     email = request.form['email']
#     if request.form['password'] == users[email]['password']:
#         user = User()
#         user.id = email
#         flask_login.login_user(user)
#         return redirect(url_for('protected'))

#     return 'Bad login'


if __name__ == "__main__":
    app.run(debug=True)
