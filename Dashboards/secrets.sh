#!/bin/bash
# AWS and DB connection secrets

# Remote connection
export USERNAME=postgres
export PASSWORD=HhmL0SWLuxPirhQO9dXD
export DB_NAME=engine_db
export DB_HOST=rpcs.cvsc3wzxbc5v.us-west-2.rds.amazonaws.com
export DB_PORT=5432

# Local connection
export LOCAL_PG_USER='postgres'
export LOCAL_PG_PASSWORD='admin'
export LOCAL_DB_NAME='engine_db'
export LOCAL_PG_HOST='localhost'
export LOCAL_PG_PORT='5432'
