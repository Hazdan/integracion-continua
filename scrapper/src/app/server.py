from api import api_bp
from sanic import Sanic, response

from app.config import AppConfig


def create_app(config: AppConfig) -> Sanic:
    """
        This function is used to create the sanic app

    Returns:
        Sanic: Sanic app
    """
    app = Sanic("ScrapperBuscalibreTrack", config=config, strict_slashes=False)

    @app.get("/")
    async def index(request):
        """
            Return the index view for scrapper
        Returns:
            html: index.html
        """
        return response.html('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Buscalibre Tracker</title></head><body><style>*{ margin: 0; padding: 0; font-size: 16px;} .container{ width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center; background-color: #3C4048;} .d-block{ display: block;} .d-flex{ display: flex;} .justify-center{ justify-content: center;} .align-center{ align-items: center;} .w-100{ width: 100%;} .w-50{ width: 50%;} .m-2{ margin: 2rem;} .btn{ padding: 10px 20px; border: 0; border-radius: 5px;} .btn--primary{ background-color: #FF5959; color: white;} .form-control{ border: 0; border-radius: 5px; color: #3C4048; background-color: #f1f1f1; padding: 10px 20px;} </style><div class="container"><form class="w-50" action="/books" method="POST"><div class="input-field"><input class="d-block w-100 form-control" type="text" name="book_url" placeholder="https://buscalibre.com/..." required></div><div class="input-field d-flex justify-center m-2"><input class="d-block btn btn--primary" type="submit" value="Buscar..."></div></form></div></body></html>')
        

    app.blueprint(api_bp)


    return app
