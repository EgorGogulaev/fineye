class CreditLimitCalculator:
    """Класс рассчета кредитного лимита, на основе рейтинга и финансовых показателей компании/группы"""

    def __init__(self, dict_with_reports):
        self.dict_with_reports = dict_with_reports

    @staticmethod
    def calculate_credit_limit(dict_with_reports):
        # TODO выработать методологию рассчета кредитного лемита

        return dict_with_reports

    def get_dict_with_credit_limite_for_company_or_group(self):
        dict_with_credit_limite_for_company_or_group = self.calcalculate_credit_limit(
            self.dict_with_reports)

        return dict_with_credit_limite_for_company_or_group