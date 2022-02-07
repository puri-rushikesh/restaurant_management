def get_engine():
    from sqlalchemy import create_engine
    from urllib.parse import quote
    from utils.config import db_config
    from utils.logger import logger

    try:
        logger(1, f'Establishing connection for database : {db_config["db"]}')
        db_url = f'''postgresql+psycopg2://{db_config["user"]}:{quote(db_config["password"])}@{db_config["host"]}:{db_config["port"]}/{db_config["db"]}'''
        engine = create_engine(db_url)
        logger(1, f'Success in connection for database : {db_config["db"]}')
        return engine
    except Exception as e:
        import traceback
        logger(3, 'Following error has been encountered - ' + str(e))
        logger(4, str(traceback.format_exc()))
