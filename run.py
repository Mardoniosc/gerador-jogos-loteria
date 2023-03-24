import collections
from collections import abc
collections.MutableMapping = abc.MutableMapping
from app import app

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')

def create_app():
  return app