import configparser

import sqlalchemy
from sqlalchemy.orm import sessionmaker

import mapping_delcreda_PSQL as mpdp



def get_company_id(session: sqlalchemy.orm.Session, OGRN: str) -> int | None:
    """
    Функция для запроса id компании по её ОГРН
    :param session: sqlalchemy.orm.Session
    :param OGRN: str ОГРН искомой компании
    :return: int|NoneType id компании
    """

    company_object: int = session.query(mpdp.Company).filter(mpdp.Company.Registration_number == OGRN).first()
    if company_object:
        return company_object.company_id


def get_company_financial_statments(session: sqlalchemy.orm.Session, company_id: int) -> dict | None:

    list_financial_statment_objects: list[sqlalchemy.orm.Query] = session.query(
        mpdp.FinancialStatement).filter(mpdp.FinancialStatement.company_id == company_id)

    if not list_financial_statment_objects:
        print("Отчеты по компании не найдены.")
        return None

    else:
        result_dict = {}

        for financial_statment in list_financial_statment_objects:
            result_dict[financial_statment.Report_period.year] = [financial_statment.id, {}]
            # TODO



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')




