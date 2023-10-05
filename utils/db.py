import asyncio
from sqlalchemy import create_engine, Column, Integer, String, Text, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from localization.message_texts import MessageText

from localization.translating import check_lang

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    lang = Column(Text, unique=False, nullable=False, default='eng')
    user_fname = Column(Text, unique=False, nullable=False)
    user_lname = Column(Text, unique=False, nullable=False)
    user_inst = Column(Text, default='-')

class UserClickerData(Base):
    __tablename__ = 'game_data'
    user_id = Column(Integer, primary_key=True)
    user_level = Column(Integer, default=0)
    bamboo_balance = Column(FLOAT, default=0)
    diamond_balance = Column(Integer, default=0)
    click_count = Column(Integer, default=0)
    spin_count = Column(Integer, default=0)
    user_inventory = Column(Text, nullable=False, default="")


class Database():
    def __init__(self):
        self.db_url = 'sqlite:///sam_database.db'
        self.engine = create_engine(self.db_url)

    def create_database(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, message, bot):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(user_id=message.from_user.id).first()
        if not user:
            if message.from_user.last_name != None:
                new_user = User(user_id=message.from_user.id, user_fname=message.from_user.first_name, user_lname=message.from_user.last_name)
            else: 
                last_name = ''
                new_user = User(user_id=message.from_user.id, user_fname=message.from_user.first_name, user_lname=last_name)
            new_clicker_data = UserClickerData(user_id=message.from_user.id)
            session.add(new_user)
            session.add(new_clicker_data)
            session.commit()

        session.close()

    def get_user_name(self, user_id):
        try: 
            Session = sessionmaker(bind=self.engine)
            session = Session()

            user = session.query(User).filter_by(user_id=user_id).first()
            username = [user.user_fname, user.user_lname]
            return username
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    def get_user_inst(self, user_id):
        try: 
            Session = sessionmaker(bind=self.engine)
            session = Session()

            user = session.query(User).filter_by(user_id=user_id).first()
            user_inst = user.user_inst
            return user_inst
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    def get_lang(self, user_id):
        try: 
            Session = sessionmaker(bind=self.engine)
            session = Session()

            user = session.query(User).filter_by(user_id=user_id).first()
            return user.lang
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    def change_user_lang(self, user_id, lang):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            user = session.query(User).filter_by(user_id=user_id).first()

            user.lang = lang
            session.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    async def user_click(self, message, bot, user_id, lang):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            clicker_data = session.query(UserClickerData).filter_by(user_id=user_id).first()
            if clicker_data.user_level == 0:
                clicker_data.bamboo_balance += 0.1
                mes = await message.answer(f'<em>0.1 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 1:
                clicker_data.bamboo_balance += 0.2
                mes = await message.answer(f'<em>0.2 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 2:
                clicker_data.bamboo_balance += 0.5
                mes = await message.answer(f'<em>0.5 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 3:
                clicker_data.bamboo_balance += 1
                mes = await message.answer(f'<em>1 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 4:
                clicker_data.bamboo_balance += 1.5
                mes = await message.answer(f'<em>1.5 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 5:
                clicker_data.bamboo_balance += 3
                mes = await message.answer(f'<em>3 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 6:
                clicker_data.bamboo_balance += 5
                mes = await message.answer(f'<em>5 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 7:
                clicker_data.bamboo_balance += 10
                mes = await message.answer(f'<em>10 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 8:
                clicker_data.bamboo_balance += 20
                mes = await message.answer(f'<em>20 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 9:
                clicker_data.bamboo_balance += 50
                mes = await message.answer(f'<em>50 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            elif clicker_data.user_level == 10:
                clicker_data.bamboo_balance += 150
                mes = await message.answer(f'<em>150 {check_lang(MessageText.collected_text, lang)}</em>🎋', parse_mode='HTML')
            
            await asyncio.sleep(1)
            await bot.delete_message(chat_id=message.from_user.id, message_id=mes.message_id - 1)
            await bot.delete_message(chat_id=message.from_user.id, message_id=mes.message_id)
            clicker_data.click_count += 1

            session.commit()
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    def get_user_balance(self, user_id):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            clicker_data = session.query(UserClickerData).filter_by(user_id=user_id).first()
            balance = [clicker_data.bamboo_balance, clicker_data.diamond_balance]
            return balance
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            session.close()

    def get_top_bamboo_users(self, limit=10):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            top_users = session.query(UserClickerData).order_by(UserClickerData.bamboo_balance.desc()).limit(limit).all()
            return top_users
        
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            session.close()

    def get_top_diamond_users(self, limit=10):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            top_users = session.query(UserClickerData).order_by(UserClickerData.diamond_balance.desc()).limit(limit).all()
            return top_users
        
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            session.close()