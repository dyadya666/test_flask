#!myvenv/bin/python3

from migrate.versioning import api

from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, version - 1)

print('Current version: ' + str(version))