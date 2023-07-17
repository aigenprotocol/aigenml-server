from dotenv import load_dotenv

load_dotenv()
import os

from server import globals as g

if __name__ == '__main__':
    g.app.run(debug=True, host=os.environ.get("HOST"), port=os.environ.get("PORT"))
