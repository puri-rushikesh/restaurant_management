def insert_data():
    import pandas as pd
    from utils.config import db_config
    from utils.connection import get_engine

    engine = get_engine()
    df = pd.read_csv(fname, sep=',')

    query = f'''CREATE TABLE IF NOT EXISTS {db_config["schema"]}.{db_config["table"]}(id serial4 NOT NULL,restaurant
     varchar(100) NOT NULL, type_of_food varchar(100) NOT NULL, cuisine varchar(100) NOT NULL, price varchar(20)
      NOT NULL, specialties varchar(100) NOT NULL, CONSTRAINT {db_config["table"]}_pkey PRIMARY KEY (id))'''
    engine.execute(query)
    df.to_sql(db_config["table"], engine, schema=db_config["schema"], if_exists="append", index=False)


if __name__ == '__main__':
    fname = 'data.csv'
    insert_data()
