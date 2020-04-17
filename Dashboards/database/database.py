#!/usr/bin/env python

# author: Sam Nelson (samueljn)

###############################################
### API for interacting with RPCS DB Server ###
### ------------- DO NOT EDIT ------------- ###
###############################################

import os
import logging
from random import randrange
from ipdb import set_trace as debug
from sqlalchemy import create_engine
from logger import setup_logging
import colored_traceback.always
USERNAME = os.getenv('postgres', 'postgres')
PASSWORD = os.getenv('admin', 'HhmL0SWLuxPirhQO9dXD')
DB_NAME = os.getenv('engine_db', 'engine_db')
DB_HOST = os.getenv('localhost', 'rpcs.cvsc3wzxbc5v.us-west-2.rds.amazonaws.com')
DB_PORT = os.getenv('5432', '5432')

def get_db(db_name='engine_db'):
    """Get the DB engine

    Returns:
        slqalchemy.engine
    """
    database_uri = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(USERNAME,
                                                                 PASSWORD,
                                                                 DB_HOST,
                                                                 DB_PORT,
                                                                 db_name)
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info('Connecting to  postgresql+psycopg2://%s:*****@%s:%s/%s',
                USERNAME, DB_HOST, DB_PORT, db_name)

    engine = create_engine(database_uri)
    # debug()
    return engine


def validate_db(database, *db_names):
    if database.url.database not in db_names:
        logger = logging.getLogger(__name__)
        error_msg = 'Not connected to one of "{}"'.format(db_names)
        logger.error(error_msg)
        raise ValueError(error_msg)


def rows_to_dicts(rows):
    """Convert a row object to a list of dicts

    Args:
        rows (sqlalchemy.ResultProxy): Result from sqlalchemy query

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    dict_rows = []
    for row in rows:
        dict_rows.append(dict(row))
    return dict_rows

def single_row_to_dict(row):
    """Convert a row object to a list of dicts

    Args:
        row (sqlalchemy.ResultProxy): Result from sqlalchemy query

    Returns:
        dict: Dict with column names as keys. If no rows,
            an empty list is returned.
    """
    for the_row in row:
        return the_row
    return []


def find_gyro_by_id(db, _id):
    """find one row in the gyros table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from gyros table")

    query = '''
         SELECT *
           FROM gyros
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    return single_row_to_dict(result)

def find_accel_by_id(db, _id):
    """find one row in the accels table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from accels table")

    query = '''
         SELECT *
           FROM accels
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    return single_row_to_dict(result)

def find_biometric_by_id(db, _id):
    """find one row in the biometric table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from biometric table")

    query = '''
         SELECT *
           FROM biometric
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    return single_row_to_dict(result)

def find_game_by_id(db, _id):
    """find one row in the game table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from game table")

    query = '''
         SELECT *
           FROM game
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    return single_row_to_dict(result)

def find_test_by_id(db, _id):
    """find one row in the test table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from test table")

    query = '''
         SELECT *
           FROM test
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    return single_row_to_dict(result)

def find_emotion_by_id(db, _id):
    """find one row in the emotion table that matches the given id

    Args:
        db (slqalchemy.engine): the database engine
        _id (uuid): unique id for row

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from emotion table")

    query = '''
         SELECT *
           FROM emotion
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    return single_row_to_dict(result)

def find_personal_check_in_by_id(db, id):
    """find one row in the personal_check_in table that matches the given primary key id

    Args:
        db (slqalchemy.engine): the database engine
        _id (str(uuid)): unique id for row, same as the primary key

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from the personal_check_in table")

    query = '''
         SELECT *
           FROM personal_check_in
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    return single_row_to_dict(result)

def find_medication_by_id(db, id):
    """find one row in the medication table that matches the given primary key id

    Args:
        db (slqalchemy.engine): the database engine
        _id (str(uuid)): unique id for row, same as the primary key

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching one row from the medication table")

    query = '''
         SELECT *
           FROM medication
          WHERE id = %s;
    '''
    data = (_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    return single_row_to_dict(result)

def find_all_gyros(db):
    """find all rows in the gyros table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from gyros table")
    query = '''
         SELECT *
           FROM gyros;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_accels(db):
    """find all rows in the accels table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from accels table")
    query = '''
         SELECT *
           FROM accels;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_biometric(db):
    """find all rows in the biometric table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from biometric table")
    query = '''
         SELECT *
           FROM biometric;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_game(db):
    """find all rows in the game table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from game table")
    query = '''
         SELECT *
           FROM game;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_test(db):
    """find all rows in the test table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from test table")
    query = '''
         SELECT *
           FROM test;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_emotion(db):
    """find all rows in the emotion table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from emotion table")
    query = '''
         SELECT *
           FROM emotion;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_personal_check_in(db):
    """find all rows in the personal_check_in table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from personal_check_in table")
    query = '''
         SELECT *
           FROM personal_check_in;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def find_all_medication(db):
    """find all rows in the medication table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching all rows from medication table")
    query = '''
         SELECT *
           FROM medication;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts

def insert_gyro(db, gyro_id, description, patient_id, x, y, z):
    """insert row into the gyros table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into gyros table")

    query = '''
         INSERT INTO gyros (gyro_id, description, patient_id, x, y, z)
           VALUES (%s, %s, %s, %s, %s, %s);
    '''
    data = (gyro_id, description, patient_id, x, y, z)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for gyros table")
        raise ex
        return False

    return True

def insert_accel(db, accel_id, description, patient_id, x, y, z):
    """insert row into the accels table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into accels table")

    query = '''
         INSERT INTO accels (accel_id, description, patient_id, x, y, z)
           VALUES (%s, %s, %s, %s, %s, %s);
    '''
    data = (accel_id, description, patient_id, x, y, z)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for accels table")
        raise ex
        return False

    return True

def insert_biometric(db, patient_id, heart_rate, blood_pressure):
    """insert row into the biometric table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into biometric table")

    query = '''
         INSERT INTO biometric (patient_id, heart_rate, blood_pressure)
           VALUES (%s, %s, %s);
    '''
    data = (patient_id, heart_rate, blood_pressure)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for biometric table")
        raise ex
        return False

    return True

def insert_game(db, game_id, description, patient_id, left_hand_score, right_hand_score, time_played):
    """insert row into the game table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into game table")

    query = '''
         INSERT INTO game (game_id, description, patient_id, left_hand_score, right_hand_score, time_played)
           VALUES (%s, %s, %s, %s, %s, %s);
    '''
    data = (game_id, description, patient_id, left_hand_score, right_hand_score, time_played)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for game table")
        raise ex
        return False

    return True

def insert_test(db, test_id, description, patient_id, test_score):
    """insert row into the test table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into test table")

    query = '''
         INSERT INTO test (test_id, description, patient_id, test_score)
           VALUES (%s, %s, %s, %s);
    '''
    data = (test_id, description, patient_id, test_score)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for test table")
        raise ex
        return False

    return True

def insert_emotion(db, patient_id, dominant_emotion, neutral, anger, happiness, surprise, sadness):
    """insert row into the emotion table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into emotion table")

    query = '''
         INSERT INTO emotion (patient_id, dominant_emotion, neutral, anger, happiness, surprise, sadness)
           VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''
    data = (patient_id, dominant_emotion, neutral, anger, happiness, surprise, sadness)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for emotion table")
        raise ex
        return False

    return True

def insert_personal_check_in(db, patient_id, category, value):
    """insert row into the personal_check_in table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into personal_check_in table")

    query = '''
         INSERT INTO personal_check_in (patient_id, category, value)
           VALUES (%s, %s, %s);
    '''
    data = (patient_id, category, value)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for personal_check_in table")
        raise ex
        return False

    return True

def insert_medication(db, patient_id, device_id, scheduled_time, response):
    """insert row into the medication table

    Args:
        db (slqalchemy.engine): the database engine
        all table columns

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting row into medication table")

    query = '''
         INSERT INTO medication (patient_id, device_id, scheduled_time, response)
           VALUES (%s, %s, %s, %s);
    '''
    data = (patient_id, device_id, scheduled_time, response)

    try:
        db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute insert query for medication table")
        raise ex
        return False

    return True

def insert_many_gyros(db, rows):
    """insert many rows into the gyros table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into gyros table", len(rows))

    query = '''
         INSERT INTO gyros (gyro_id, description, patient_id, x, y, z)
           VALUES (%(gyro_id)s, %(description)s, %(patient_id)s, %(x)s, %(y)s, %(z)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for gyros table")
        raise ex
        return False

    return True

def insert_many_accels(db, rows):
    """insert many rows into the accel table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into accel table", len(rows))

    query = '''
         INSERT INTO accels (accel_id, description, patient_id, x, y, z)
           VALUES (%(accel_id)s, %(description)s, %(patient_id)s, %(x)s, %(y)s, %(z)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for accel table")
        raise ex
        return False

    return True

def insert_many_biometrics(db, rows):
    """insert many rows into the biometric table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into biometric table", len(rows))

    query = '''
         INSERT INTO biometric (patient_id, heart_rate, blood_pressure)
           VALUES (%(patient_id)s, %(heart_rate)s, %(blood_pressure)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for biometric table")
        raise ex
        return False

    return True

def insert_many_games(db, rows):
    """insert many rows into the game table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into game table", len(rows))

    query = '''
         INSERT INTO game (game_id, description, patient_id, left_hand_score, right_hand_score, time_played)
           VALUES (%(game_id)s, %(description)s, %(patient_id)s, %(left_hand_score)s, %(right_hand_score)s, %(time_played)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for game table")
        raise ex
        return False

    return True

def insert_many_tests(db, rows):
    """insert many rows into the test table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into test table", len(rows))

    query = '''
         INSERT INTO test (test_id, description, patient_id, test_score)
           VALUES (%(test_id)s, %(description)s, %(patient_id)s, %(test_score)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for test table")
        raise ex
        return False

    return True

def insert_many_emotions(db, rows):
    """insert many rows into the emotion table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into emotion table", len(rows))

    query = '''
         INSERT INTO emotion (patient_id, dominant_emotion, neutral, anger, happiness, surprise, sadness)
           VALUES (%(patient_id)s, %(dominant_emotion)s, %(neutral)s, %(anger)s, %(happiness)s, %(surprise)s, %(sadness)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for emotion table")
        raise ex
        return False

    return True

def insert_many_personal_check_ins(db, rows):
    """insert many rows into the personal_check_in table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into personal_check_in table", len(rows))

    query = '''
         INSERT INTO personal_check_in (patient_id, category, value)
           VALUES (%(patient_id)s, %(category)s, %(value)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for personal_check_in table")
        raise ex
        return False

    return True

def insert_many_medications(db, rows):
    """insert many rows into the medication table

    Args:
        db (slqalchemy.engine): the database engine
        rows list(dicts): a list of dictionaries, each dictionary represents a row.

    Returns:
            true on success, false on failure
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Inserting %s rows into medication table", len(rows))

    query = '''
         INSERT INTO medication (patient_id, device_id, scheduled_time, response)
           VALUES (%(patient_id)s, %(device_id)s, %(scheduled_time)s, %(response)s);
    '''

    try:
        db.execute(query, rows)
    except Exception as ex:
        logger.error("Failed to execute insert many query for medication table")
        raise ex
        return False

    return True

def find_gyro_by_patient_id(db, patient_id):
    """find all rows in the gyros table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the gyros table by patient_id")

    query = '''
         SELECT *
           FROM gyros
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_accels_by_patient_id(db, patient_id):
    """find all rows in the accels table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the accels table by patient_id")

    query = '''
         SELECT *
           FROM accels
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_biometric_by_patient_id(db, patient_id):
    """find all rows in the biometric table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the biometric table by patient_id")

    query = '''
         SELECT *
           FROM biometric
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_game_by_patient_id(db, patient_id):
    """find all rows in the game table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the game table by patient_id")

    query = '''
         SELECT *
           FROM game
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_test_by_patient_id(db, patient_id):
    """find all rows in the test table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the test table by patient_id")

    query = '''
         SELECT *
           FROM test
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_emotion_by_patient_id(db, patient_id):
    """find all rows in the emotion table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the emotion table by patient_id")

    query = '''
         SELECT *
           FROM emotion
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_personal_check_in_by_patient_id_and_category(db, patient_id, category):
    """find all rows in the personal_check_in table that matches the given patient_id and category

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (str(uuid)): id for patient
        category (str): string representing a category (i.e. "sports")

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the personal_check_in table by patient_id and category")

    query = '''
         SELECT *
           FROM personal_check_in
          WHERE patient_id = %s
          AND category = %s;
    '''
    data = (patient_id, category)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_medication_by_patient_id(db, patient_id):
    """find all rows in the medication table that matches the given patient_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the medication table by patient_id")

    query = '''
         SELECT *
           FROM medication
          WHERE patient_id = %s;
    '''
    data = (patient_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_medication_by_device_id(db, device_id):
    """find all rows in the medication table that matches the given device_id

    Args:
        db (slqalchemy.engine): the database engine
        patient_id (uuid): id for patient

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from the medication table by device_id")

    query = '''
         SELECT *
           FROM medication
          WHERE device_id = %s;
    '''
    data = (device_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_by_gyro_id(db, gyro_id):
    """find all rows in a given table that match the given gyro_id

    Args:
        db (slqalchemy.engine): the database engine
        gyro_id (uuid): id of the given gyroscope

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from gyros table by gryo_id")

    query = '''
         SELECT *
           FROM gyros
          WHERE gyro_id = %s;
    '''
    data = (gyro_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_by_accel_id(db, accel_id):
    """find all rows in a given table that match the given accel_id

    Args:
        db (slqalchemy.engine): the database engine
        accel_id (uuid): id of the given accelerometer

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from accels table by accel_id")

    query = '''
         SELECT *
           FROM accels
          WHERE accel_id = %s;
    '''
    data = (accel_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_by_game_id(db, game_id):
    """find all rows in a given table that match the given game_id

    Args:
        db (slqalchemy.engine): the database engine
        game_id (uuid): id of the given game

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from game table by game_id")

    query = '''
         SELECT *
           FROM game
          WHERE game_id = %s;
    '''
    data = (game_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_by_test_id(db, test_id):
    """find all rows in a given table that match the given test_id

    Args:
        db (slqalchemy.engine): the database engine
        test_id (uuid): id of the given test

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from test table by test_id")

    query = '''
         SELECT *
           FROM test
          WHERE test_id = %s;
    '''
    data = (test_id)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def find_by_dominant_emotion(db, dominant_emotion):
    """find all rows in the emotion table that match the given dominant_emotion

    Args:
        db (slqalchemy.engine): the database engine
        dominant_emotion (string): dominant emotion

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from emotion table by dominant_emotion")

    query = '''
         SELECT *
           FROM emotion
          WHERE dominant_emotion = %s;
    '''
    data = (dominant_emotion)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_gyros_by_time(db, start_time, end_time):
    """find all rows in gyros table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from gyros table by time")

    query = '''
         SELECT *
           FROM gyros
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_accels_by_time(db, start_time, end_time):
    """find all rows in accels table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from accels table by time")

    query = '''
         SELECT *
           FROM accels
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_biometric_by_time(db, start_time, end_time):
    """find all rows in biometric table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from biometric table by time")

    query = '''
         SELECT *
           FROM biometric
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_game_by_time(db, start_time, end_time):
    """find all rows in game table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from game table by time")

    query = '''
         SELECT *
           FROM game
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_test_by_time(db, start_time, end_time):
    """find all rows in test table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from test table by time")

    query = '''
         SELECT *
           FROM test
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_emotion_by_time(db, start_time, end_time):
    """find all rows in emotion table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from emotion table by time")

    query = '''
         SELECT *
           FROM emotion
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_personal_check_in_by_time(db, start_time, end_time):
    """find all rows in personal_check_in table that where recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from personal_check_in table by time")

    query = '''
         SELECT *
           FROM personal_check_in
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

def query_medication_by_time(db, start_time, end_time):
    """find all rows in medication table that were recorded between a given start and end time

    Args:
        db (slqalchemy.engine): the database engine
        start_time (timestamp)
        end_time (timestamp)

    Returns:
        list(dicts) | []: Dicts with column names as keys. If no rows,
            an empty list is returned.
    """
    logger = logging.getLogger(__name__)

    validate_db(db, 'engine_db')

    logger.info("Fetching rows from medication table by time")

    query = '''
         SELECT *
           FROM medication
          WHERE created_at BETWEEN %s AND %s;
    '''
    data = (start_time, end_time)

    try:
        result = db.execute(query, data)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex

    dicts = rows_to_dicts(result) 
    return dicts

# # # Find one functions are mainly for testing purposes, they are not optimized for performance # # #

def find_one_gyro(db):
    """find one random row in the gyros table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from gyros table")
    query = '''
         SELECT *
           FROM gyros;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result) 
    return dicts[randrange(len(dicts))]

def find_one_accel(db):
    """find one random row in the accels table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from accels table")
    query = '''
         SELECT *
           FROM accels;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result) 
    return dicts[randrange(len(dicts))]

def find_one_biometric(db):
    """find one random row in the biometric table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from biometric table")
    query = '''
         SELECT *
           FROM biometric;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result) 
    return dicts[randrange(len(dicts))]

def find_one_game(db):
    """find one random row in the game table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from game table")
    query = '''
         SELECT *
           FROM game;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result) 
    return dicts[randrange(len(dicts))]

def find_one_test(db):
    """find one random row in the test table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from test table")
    query = '''
         SELECT *
           FROM test;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts[randrange(len(dicts))]

def find_one_emotion(db):
    """find one random row in the emotion table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from emotion table")
    query = '''
         SELECT *
           FROM emotion;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts[randrange(len(dicts))]

def find_one_personal_check_in(db):
    """find one random row in the personal_check_in table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from personal_check_in table")
    query = '''
         SELECT *
           FROM personal_check_in;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts[randrange(len(dicts))]


def find_one_medication(db):
    """find one random row in the medication table

    Args:
        db (slqalchemy.engine): the database engine

    Returns:
        result(dict): Dict with column names as keys. If no row,
            an empty dict is returned.
    """
    logger = logging.getLogger(__name__)
    validate_db(db, 'engine_db')
    logger.info("Fetching random row from emotion table")
    query = '''
         SELECT *
           FROM medication;
    '''
    try:
        result = db.execute(query)
    except Exception as ex:
        logger.error("Failed to execute query")
        raise ex
    dicts = rows_to_dicts(result)
    return dicts[randrange(len(dicts))]