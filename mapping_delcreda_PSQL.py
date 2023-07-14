# TODO ПРОПИСАТЬ ЛОГИКУ CRUD + реализовать Valid_from / Valid_to  и Date_actualization (архивные данные)
#  - AuthorizedCapital

import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Index, Integer, BigInteger, String, ForeignKey, Text, Date, Float, Numeric, ARRAY, JSON, \
    VARCHAR, DateTime, LargeBinary, Boolean
import psycopg2

import reference_info

config = configparser.ConfigParser()
config.read('config.ini')  # 86.62.76.242

delcreda_global_engine = create_engine(config['PSQL']['global_engine'])
# local_engine = create_engine(config['PSQL']['local_engine'])
local_engine = create_engine(
    'postgresql+psycopg2://postgres:freedom@127.0.0.1:5432/postgres'
)

Base = declarative_base()


class History(Base):
    """История изменения основных полей - записей"""

    __tablename__ = 'history'  # (!) Хранить корректировки БО (текущий код "N", после добавятся новые строки, текущий год перезаписать и поставить "F")
                               # Квартальные: С квартальными, просто выгрузка, без хранения истории (!)
    history_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    p_table_id = Column(Integer, ForeignKey('p_table.p_table_id'))
    Row_id = Column(BigInteger)  # Идентификатор строки, которая уходит в историю
    Column_name = Column(VARCHAR(length=50))  # Название колонки, в которой происходит изменение

    value = Column(VARCHAR)
    type_value = Column(VARCHAR)

    valid_from = Column(Date)
    valid_to = Column(Date)

    date_creating_history_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    p_table = relationship("PTable", back_populates="history")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index('history_idx', p_table_id, Row_id),
    )

class PTable(Base):  # СМ. StructureTable (реализовать подобную структуру)
    """Схемы таблиц БД"""

    __tablename__ = 'p_table'

    p_table_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Table_name = Column(VARCHAR(length=50))
    Table_description = Column(VARCHAR(length=250))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    history = relationship("History", back_populates='p_table')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Company(Base):
    """Информация о ЮЛ"""

    __tablename__ = 'company'

    company_id = Column(BigInteger, primary_key=True)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country_registration_id = Column(Integer, ForeignKey('country.country_id'))
    Name_national_registration_number = Column(VARCHAR(length=100))
    Registration_number = Column(VARCHAR(length=50))
    Name_national_tax_number = Column(VARCHAR(length=100))
    Tax_number = Column(VARCHAR(length=50))

    Status = Column(Text)

    Full_company_name = Column(Text)
    Short_company_name = Column(Text)
    Full_company_name_en = Column(Text)
    Short_company_name_en = Column(Text)

    Founding_date = Column(Date)  # Дата основания
    Termination_date = Column(Date)
    Company_activity_period = Column(Float)

    Important_information = Column(Text)


    date_actualization = Column(Date)
    date_creating_company_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country = relationship("Country", back_populates="company")
    authorized_capital = relationship("AuthorizedCapital", back_populates="company")
    company_classifier_row = relationship("CompanyClassifierRow", back_populates="company")
    financial_statement = relationship("FinancialStatement", back_populates="company")
    # financial_ratios = relationship('FinancialRatios', back_populates='company')
    license = relationship("License", back_populates="company")
    manager = relationship("Manager", back_populates="company")
    company_shareholder = relationship("Shareholder", back_populates="company_shareholder",
                                       foreign_keys="Shareholder.company_shareholder_id")
    company_share = relationship("Shareholder", back_populates="company_share",
                                 foreign_keys="Shareholder.company_share_id")
    sanctions = relationship("Sanctions", back_populates="company")
    contact_information = relationship("ContactInformation", back_populates="company")
    address = relationship("Address", back_populates="company")
    company_activity = relationship("CompanyActivity", back_populates="company")
    event = relationship("Event", back_populates='company')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    __table_args__ = (
        Index('company_idx', Registration_number, Tax_number, Status, country_registration_id),
    )

class AuthorizedCapital(Base):
    """Информация о капитале ЮЛ"""

    __tablename__ = 'authorized_capital'

    authorized_capital_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))

    Value = Column(BigInteger)

    Date_authorized_capital = Column(Date)

    date_actualization = Column(Date)
    date_creating_authorized_capital_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="authorized_capital")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index('authorized_capital_idx', company_id),
    )

# TODO _________________________________________________________________________________________________________________

class CompanyClassifierRow(Base):
    """Информация о кодах классификаторов ЮЛ"""

    __tablename__ = 'company_classifier_row'

    company_classifier_row_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))

    Classifier_name = Column(VARCHAR(length=250))
    Classifier_value = Column(VARCHAR(length=50))

    date_actualization = Column(Date)
    date_creating_classifier_row_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="company_classifier_row")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index('company_classifier_row_idx', company_id),
    )

# TODO _________________________________________________________________________________________________________________

# todo Report_type _____________________________________________________________________________________________________
class ReportType(Base):
    """Справочник видов отчетов"""

    __tablename__ = 'report_type'

    report_type_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Report_type_name_ru = Column(VARCHAR(length=300))
    Report_type_name_en = Column(VARCHAR(length=300))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    report_type_row = relationship("ReportTypeRow", back_populates="report_type")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ReportTypeRow(Base):
    """Расшифровка строк БО"""

    __tablename__ = 'report_type_row'

    report_type_row_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    report_type_id = Column(Integer, ForeignKey('report_type.report_type_id'))
    Code = Column(VARCHAR(length=30))
    Name = Column(VARCHAR(length=200))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    report_type = relationship("ReportType", back_populates="report_type_row")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# todo Report_type _____________________________________________________________________________________________________

# todo Financial_statement _____________________________________________________________________________________________
class FinancialStatement(Base):
    """Информация о наличии записей БО ЮЛ за определенный период"""

    __tablename__ = 'financial_statement'

    financial_statement_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))
    report_type_id = Column(Integer, ForeignKey('report_type.report_type_id'))

    Report_period = Column(Date)

    date_actualization = Column(Date)
    date_creating_financial_statement_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="financial_statement")
    financial_statement_row = relationship("FinancialStatementRow", back_populates="financial_statement")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index('financial_statement_idx', company_id, report_type_id, Report_period),
    )

class FinancialStatementRow(Base):
    """Строка БО ЮЛ"""

    __tablename__ = 'financial_statement_row'

    financial_statement_row_id = Column(BigInteger, primary_key=True)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    financial_statement_id = Column(BigInteger, ForeignKey('financial_statement.financial_statement_id',
                                                           ondelete="CASCADE", onupdate="CASCADE"))

    Code_name = Column(VARCHAR(length=100))
    Code_value = Column(BigInteger)

    date_creating_financial_statement_row_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    financial_statement = relationship("FinancialStatement", back_populates="financial_statement_row")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("financial_statement_row_idx", financial_statement_id),
    )

# todo Financial_statement _____________________________________________________________________________________________

class Person(Base):
    """Информация о ФЛ"""

    __tablename__ = 'person'

    person_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=True)

    Surname = Column(VARCHAR)  # Фамилия
    Name = Column(VARCHAR)  # Имя
    Patronymic = Column(VARCHAR)  # Отчество
    Date_birth = Column(Date)

    Gender = Column(VARCHAR(length=35))
    Citizenship = Column(VARCHAR(length=250))

    Individual_identifier_type = Column(VARCHAR(length=150))
    Individual_identifier_number = Column(VARCHAR(length=100))
    Individual_identifier_sub_type = Column(VARCHAR(length=150))
    Individual_identifier_sub_number = Column(VARCHAR(length=100))

    Important_information = Column(Text)

    date_actualization = Column(Date)
    date_creating_person_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    manager = relationship("Manager", back_populates="person")
    contact_information = relationship("ContactInformation", back_populates="person")
    address = relationship("Address", back_populates="person")
    sanctions = relationship("Sanctions", back_populates="person")
    shareholder = relationship("Shareholder", back_populates="person")
    country = relationship("Country", back_populates="person")
    event = relationship("Event", back_populates='person')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("person_idx", Individual_identifier_type,
              Individual_identifier_number,
              Individual_identifier_sub_number,),
    )

class Manager(Base):
    """Информация о менеджменте ЮЛ"""

    __tablename__ = 'manager'

    manager_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    person_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"))
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))

    Job_title = Column(VARCHAR(100))
    Supervisor = Column(Boolean)
    Appointment_date = Column(Date)

    Important_information = Column(Text)

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_manager_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    person = relationship("Person", back_populates="manager")
    company = relationship("Company", back_populates="manager")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("manager_idx", person_id, company_id, status_info),
    )

class Shareholder(Base):
    """Информация о долях ЮЛ и ФЛ в ЮЛ"""

    __tablename__ = 'shareholder'

    shareholder_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_shareholder_id = Column(BigInteger,
                                    ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"),
                                    nullable=True)
    person_shareholder_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"),
                                   nullable=True)
    company_share_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))

    Share_percent = Column(Float)
    Share_current = Column(VARCHAR(length=20))
    Share_value = Column(BigInteger)
    Purchase_date = Column(Date)

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_shareholder_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_shareholder = relationship("Company", foreign_keys=[company_shareholder_id],
                                       back_populates="company_shareholder")
    company_share = relationship("Company", foreign_keys=[company_share_id], back_populates="company_share")
    person = relationship("Person", back_populates="shareholder")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("shareholder_idx", company_shareholder_id, person_shareholder_id, company_share_id, status_info),
    )

class Country(Base):
    """Справочник стран"""

    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Country_name = Column(VARCHAR(length=200))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    person = relationship("Person", back_populates="country")
    company = relationship("Company", back_populates="country")

    address = relationship("Address", back_populates="country")

    sanctions = relationship("Sanctions", back_populates="country")

    activity_edition = relationship("ActivityEdition", back_populates="country")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("country_idx", Country_name),
    )

# todo КОНТАКТНАЯ ИНФОРМАЦИЯ ___________________________________________________________________________________________
class ContactInformation(Base):
    """Информация о контактных данных ФЛ/ЮЛ"""

    __tablename__ = 'contact_information'

    contact_information_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"),
                        nullable=True)
    person_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"),
                       nullable=True)

    contact_type_id = Column(Integer, ForeignKey('contact_type.contact_type_id'))
    value = Column(VARCHAR)

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_contact_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="contact_information")
    person = relationship("Person", back_populates="contact_information")
    contact_type = relationship("ContactType", back_populates="contact_information")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("contact_information_idx", company_id, person_id, status_info),
    )

class ContactType(Base):
    """Типы контактных данных"""

    __tablename__ = 'contact_type'

    contact_type_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Name_contact_type = Column(VARCHAR)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    contact_information = relationship("ContactInformation", back_populates="contact_type")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# todo _________________________________________________________________________________________________________________

class Address(Base):
    """Информация об адресах ФЛ и ЮЛ"""

    __tablename__ = 'address'

    address_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country_id = Column(Integer, ForeignKey('country.country_id'))

    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"),
                        nullable=True)
    person_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"),
                       nullable=True)

    Address_type = Column(VARCHAR(length=70))
    Region_code = Column(VARCHAR(length=50))
    Address_ZIP = Column(VARCHAR(length=50))
    Full_address = Column(VARCHAR(length=450))
    Region = Column(VARCHAR(length=150))
    Area = Column(VARCHAR(length=150))
    Locality = Column(VARCHAR(length=150))
    Street = Column(VARCHAR(length=350))
    House = Column(VARCHAR(length=50))
    Frame = Column(VARCHAR(length=50))
    Room = Column(VARCHAR(length=50))
    Address_date = Column(Date)

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_address_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country = relationship("Country", back_populates="address")
    company = relationship("Company", back_populates="address")
    person = relationship("Person", back_populates="address")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("address_idx", company_id, person_id, status_info),
    )


# TODO _________________________________________________________________________________________________________________
class ActivityEdition(Base):
    """Стандарты(документы) регламентирующие типы деятельности ЮЛ"""

    __tablename__ = 'activity_edition'

    activity_edition_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country_id = Column(Integer, ForeignKey('country.country_id'))

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    country = relationship("Country", back_populates="activity_edition")
    activity_type = relationship("ActivityType", back_populates="activity_edition")
    company_activity = relationship("CompanyActivity", back_populates="activity_edition")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class ActivityType(Base):
    """Справочник видов деятельности (для различных стран)"""

    __tablename__ = 'activity_type'

    activity_type_id = Column(Integer, primary_key=True)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    activity_edition_id = Column(Integer, ForeignKey('activity_edition.activity_edition_id'))
    activity_type_code = Column(VARCHAR(length=50))
    activity_type_name = Column(VARCHAR(length=450))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    activity_edition = relationship("ActivityEdition", back_populates="activity_type")
    company_activity = relationship("CompanyActivity", back_populates="activity_type")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("activity_type_idx", activity_edition_id, activity_type_code),
    )



class CompanyActivity(Base):
    """Записи видов деятельности ЮЛ"""

    __tablename__ = 'company_activity'

    company_activity_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    company_id = Column(BigInteger, ForeignKey("company.company_id"))
    activity_edition_id = Column(Integer, ForeignKey('activity_edition.activity_edition_id'))
    activity_type_id = Column(Integer, ForeignKey('activity_type.activity_type_id'))
    activity_type_code = Column(VARCHAR(length=50))

    Main = Column(Boolean)
    Company_activity_date = Column(Date)

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_activity_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    activity_edition = relationship("ActivityEdition", back_populates="company_activity")
    activity_type = relationship("ActivityType", back_populates="company_activity")
    company = relationship("Company", back_populates="company_activity")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("company_activity_idx", company_id, activity_type_id, activity_type_code, status_info,),
    )

# TODO _________________________________________________________________________________________________________________


class License(Base):
    """Лицензии ЮЛ"""

    __tablename__ = 'license'

    license_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"))
    License_number = Column(VARCHAR(length=150))
    License_type_activity = Column(Text)
    Licensee = Column(VARCHAR(600))  # Лицензиат

    valid_from = Column(Date)
    valid_to = Column(Date)
    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_license_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="license")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("license_idx", company_id, status_info),
    )

class Event(Base):
    """События связанные с ФЛ или ЮЛ"""

    __tablename__ = 'event'

    event_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"),
                        nullable=True)
    person_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"),
                       nullable=True)

    Event_date = Column(Date)
    Event_description = Column(Text)

    date_creating_event_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates='event')
    person = relationship("Person", back_populates='event')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("event_idx", company_id, person_id, Event_date, Event_description),
    )


class Sanctions(Base):
    """Санкции к ЮЛ и ФЛ"""

    __tablename__ = 'sanctions'

    sanctions_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company_id = Column(BigInteger, ForeignKey('company.company_id', ondelete="CASCADE", onupdate="CASCADE"),
                        nullable=True)
    person_id = Column(BigInteger, ForeignKey('person.person_id', ondelete="CASCADE", onupdate="CASCADE"),
                       nullable=True)

    sanction_country_id = Column(BigInteger, ForeignKey('country.country_id'))

    status_info = Column(VARCHAR(length=1))

    date_actualization = Column(Date)
    date_creating_sanctions_info = Column(Date)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    company = relationship("Company", back_populates="sanctions")
    person = relationship("Person", back_populates="sanctions")
    country = relationship("Country", back_populates="sanctions")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("sanctions_idx", company_id, person_id, sanction_country_id, status_info),
    )


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________

# todo REQUESTS
class RequestData(Base):  # todo (???) ТИПЫ ДАННЫХ КОЛОНОК / ИНДЕКСАЦИЯ
    """Запросы к обработке сервисом мониторинга и парсинга данных"""

    __tablename__ = 'request_data'

    request_data_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    request_status_type_id = Column(Integer, ForeignKey("request_status_type.request_status_type_id"))

    Request_datetime = Column(DateTime)
    mandant_reg_number = Column(VARCHAR)  # Идентификатор запрашивающей стороны(???)  ОГРН компании, которая подает запрос

    service_agreement_id = Column(BigInteger)  # Пока будет заполняться None (Договор с мандантом на оказание услуги)
    User = Column(VARCHAR(length=50))  # Конкретный пользователь внутри компании(Login в системе)

    Country_requested_company = Column(Integer)
    Registration_number = Column(VARCHAR(length=100))  # ОГРН
    # __________________________________________________________________________________________________________________

    Request_processing_result = Column(VARCHAR(length=70))  # Текущее состояние запросы

    Expected_completion_date = Column(DateTime)  # Ожидаемое время выполнения запроса (???)
    Completed = Column(Boolean)  # Закрыта ли заявка
    Date_last_data_update = Column(Date)  # На вход - пустое, заполняется в процессе исполнения запроса(ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ целевой информации)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    request_status_type = relationship("RequestStatusType", back_populates='request_data')
    request_handling_process = relationship("RequestHandlingProcess", back_populates='request_data')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("request_data_idx", Registration_number, mandant_reg_number, Request_processing_result),
    )

class RequestStatusType(Base):
    """Типы статусов заявок"""

    __tablename__ = "request_status_type"

    request_status_type_id = Column(Integer, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Status_name = Column(VARCHAR(length=100))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    request_data = relationship("RequestData", back_populates='request_status_type')
    request_handling_process = relationship("RequestHandlingProcess", back_populates='request_status_type')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class RequestHandlingProcess(Base):
    """Ход обработки запросов"""

    __tablename__ = "request_handling_process"

    request_handling_process_id = Column(BigInteger, primary_key=True)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    request_data_id = Column(BigInteger, ForeignKey("request_data.request_data_id"), nullable=True)
    request_status_type_id = Column(BigInteger, ForeignKey('request_status_type.request_status_type_id'), nullable=True)

    Responsible_person = Column(VARCHAR(length=50))  # Если скрипт, то ставить пометку
    Time_status = Column(DateTime)
    Status_comment = Column(Text)  # текст лога (???)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    request_data = relationship("RequestData", back_populates="request_handling_process")
    request_status_type = relationship("RequestStatusType", back_populates='request_handling_process')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    __table_args__ = (
        Index("request_handling_process_idx", request_data_id, request_status_type_id, Responsible_person),
    )



if __name__ == '__main__':
    Base.metadata.create_all(local_engine)
    reference_info.upload_reference_info()

