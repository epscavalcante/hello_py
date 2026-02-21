from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/signup')
async def signup():
    """
    Endpoint for user signup.
    """
    return {'message': 'Signup endpoint'}
