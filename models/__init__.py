from models.engine import file_storage

"""initialization of models module"""

storage = file_storage.FileStorage()
storage.reload()
