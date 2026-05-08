from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {
    1: {"name": "item_1", "description": 'Este es el item 1'},
    2: {"name": "item_2", "description": 'Este es el item 2'},
    3: {"name": "item_3", "description": 'Este es el item 3'}
}

@app.get('/')
def read_root():
    return {"message": "Hello World"}

@app.get('/items/')
def read_item(item_id: int):
    if item_id in fake_db:
        return fake_db[item_id]
    else:
        raise HTTPException(status_code = 404, detail = "Item not found")


@app.post('/items/created/{item_id}')
def created_item(item_id : int, name: str, description: str):
    if item_id in fake_db:
        raise HTTPException(status_code = 404, detail = "Item already exists")
    else:
        fake_db[item_id] = {'name' : name, 'description': description}
    return fake_db[item_id]