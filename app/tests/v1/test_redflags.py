import pytest
import json
from ... import create_app
from app.api.v1.models.redflagM import redflags

app = create_app()


redflag = json.dumps(
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

updates_redflag = json.dumps({
	"status":"Rejected"
	})


@pytest.fixture()
def client():
	app = create_app()
	test_client =app.test_client()
	return test_client
	

def test_post(client):
	red_post = client.post('/api/v1/redflags', data= redflag,
                       content_type='application/json')
	assert b'Redflag is added' in red_post.data
	assert red_post.status_code == 201

def test_get(client):
    red_get = client.get('/api/v1/redflags')
    res_obj = json.loads(red_get.data.decode())
    assert 1 == len(res_obj)
    assert [redflags[0]] == res_obj
    assert red_get.status_code == 200