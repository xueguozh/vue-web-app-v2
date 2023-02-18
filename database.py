from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://d4o1ymx10hbgtwcjh4l9:pscale_pw_nQlzMCJ8KLrs8S5rWgbh9al85BzMFt4jgqq7ZAANKqW@ap-southeast.connect.psdb.cloud/jackiezhang?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                        "ssl_ca": "/etc/ssl/cert.pem"
                       }})
