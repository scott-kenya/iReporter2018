import pytest
import json
from ... import create_app
from app.api.v1.models.incidentsM import incidents

app = create_app()


incidents = json.dumps(
		{
                        "Title": "Broken bridge.", 
                        "createdOn" : "12/12/2018",
                        "createdBy" : "Scott francis",
                        "type" : "red flag",
                        "location" : "N39-098 S09-234",
                        "status" : "Rejected",
                        "images" : "red.jpg",
                        "videos" : "red.mpeg",
                        "comment" : "This is a comment",
                         "id" : 1
            }
		)

updates_incident = json.dumps({
	"status":"Rejected"
	})


@pytest.fixture()
def client():
	app = create_app()
	test_client =app.test_client()
	return test_client
	

def test_post(client):
	red_post = client.post('/api/v1/incidents', data= incidents,
                       content_type='application/json')
	assert b'Incident is added' in red_post.data
	assert red_post.status_code == 201

def test_get(client):
    red_get = client.get('/api/v1/incidents')
    res_obj = json.loads(red_get.data.decode())
    assert 1 == len(res_obj)
    assert json.loads(incidents) == res_obj[0]
    assert red_get.status_code == 200

def test_get_by_id(client):
    red_get = client.get('/api/v1/incidents/1')
    assert b'Incident fetched' in red_get.data
    assert red_get.status_code == 200


def test_update_incidents(client):
    red_post = client.put('/api/v1/incidents/1', data = updates_incident,
                          content_type='application/json')
    assert b'Incident updated' in red_post.data
    assert red_post.status_code == 201

def test_delete_incidents(client):
    red_delete = client.delete('/api/v1/incidents/1')
    assert red_delete.status_code == 204
        