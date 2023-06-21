from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test")

DBsession = sessionmaker(bind=engine)

# 存数据
# try:
#     session = DBsession()

#     user = User(id="5", name="zyp")
#     session.add(user)
#     session.commit()
# except Exception as e:
#     print("error: {}".format(e))
# finally:
#     session.close()

# 取数据
try:
    session = DBsession()

    user = session.query(User).filter(User.id=="5").one()

    print(type(user))
    print(user.name)
except Exception as e:
    print("error: {}".format(e))
finally:
    session.close()

