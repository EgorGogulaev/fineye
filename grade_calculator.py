class GradeCalculator:
    """Класс, рассчитывающий рейтинг компании/группы"""

    def __init__(self, dict_with_reports):
        self.dict_with_reports = dict_with_reports

    @staticmethod
    def calculate_grade(dict_with_reports):

        # todo Блок оценки компаний с учетом динамики и весом в группе
        for OGRN in dict_with_reports[list(dict_with_reports)[0]]:

            # тут можно обрабатывать данные по отдельной компании/COMBINED  # TODO
            for year in list(dict_with_reports[list(dict_with_reports)[0]][OGRN])[-2:]:
                company_data_for_a_specific_year = dict_with_reports[list(dict_with_reports)[0]][OGRN][year]

                # БЛОК РАНЖИРОВАНИЯ ФИНАНСОВЫХ ПОКАЗАТЕЛЕЙ
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                1-9
                fin_ratios_keys = ['Financial leverage', 'Current ratio', 'ICR', 'Debt / EBIT', 'CCC', 'DSO, days',
                                   'DIO, days', 'DPO, days']
                financial_amounts = ['Revenue', 'Net profit', 'EBIT', 'Gross debt', 'Borrowed funds (long-term)',
                                     'Borrowed funds (short-term)', 'FCF', 'Total operating costs',
                                     'TOTAL ASSETS', 'CAPITAL AND RESERVES', 'Net profit', 'Gross profit (loss)']
                financial_shares = ['Net profitability', 'EBIT margin', 'Debt / Assets', 'Equity ratio', 'Gross margin',
                                    'Costs / Revenue']
                company_group_share = ['Revenue', 'EBIT', 'Gross debt', 'Total operating costs', 'Net profit']
                important_keys = ['Revenue', 'Gross debt']

                fin_gearing_assesment = {
                    0: 'negative',
                    0.5: 'low level',
                    1.5: 'moderate level',
                    2.2: 'acceptable level',
                    3.5: 'high level',
                    4: 'very high level'}

                equity_level_assesment = {
                    0: 'negative',
                    15: 'low level',
                    35: 'moderate level',
                    55: 'acceptable level',
                    56: 'high level'}

                current_ratio_assesment = {
                    0: 'negative',
                    0.5: 'very low level',
                    1.0: 'low level',
                    2.5: 'medium level',
                    3: 'high level'}

                interest_coverage_assesment = {
                    0: 'negative',
                    1.9: 'low level',
                    3: 'moderate level',
                    6: 'high level',
                    7: 'very high level'}

                net_profitability_assesment = {
                    0: 'negative',
                    3.5: 'low level',
                    10: 'moderate level',
                    15: 'high level',
                    16: 'very high level'}

                debt_assets_assesment = {
                    0: 'negative',
                    20: 'low level',
                    40: 'moderate level',
                    60: 'high level',
                    70: 'very high level',
                }

                ccc_assesment = {
                    0: 'negative',
                    10: 'very short',
                    25: 'short',
                    50: 'average',
                    90: 'long',
                    100: 'very long'}

                revenue_assesment = {
                    0: 'negative',
                    50_000_000: 'very small',
                    450_000_000: 'small',
                    2_500_000_000: 'medium',
                    50_000_000_000: 'large',
                    55_000_000_000: 'very large'}

                revenue_dynamic_assesment = {
                    -0.15: 'drop',
                    0: 'decline',
                    0.05: 'stagnation',
                    0.1: 'modest',
                    0.2: 'medium',
                    0.4: 'high',
                    0.5: 'very high'}

                debt_ebit_assesment = {
                    0: 'negative',
                    0.5: 'very low',
                    2: 'low',
                    3.8: 'acceptable',
                    6: 'high',
                    7: 'very high'}

                age_assesment = {
                    0: 'negative',
                    1: 'new established',
                    3: 'young',
                    8: 'average',
                    20: 'long established',
                    25: 'mature'}

                assesments_keys = {'Net profitability': net_profitability_assesment,
                                   'Equity ratio': equity_level_assesment,
                                   'Debt / Assets': debt_assets_assesment, 'Current ratio': current_ratio_assesment,
                                   'ICR': interest_coverage_assesment, 'Financial leverage': fin_gearing_assesment,
                                   'CCC': ccc_assesment, 'Revenue': revenue_assesment,
                                   'Company age in years': age_assesment,
                                   'Debt / EBIT': debt_ebit_assesment, 'Revenue dynamic': revenue_dynamic_assesment}

                def get_assesment_text(number, assesment_dict):

                    for size_range in sorted(assesment_dict.keys()):

                        if isinstance(number, (int, float)) and number <= size_range:
                            return assesment_dict[size_range]

                        elif not number:
                            return None

                    return assesment_dict[max(sorted(assesment_dict.keys()))]

                INCOME_STATEMENT_RUS = ['Выручка', 'Валовая прибыль (убыток)', 'Валовая маржа',
                                        'Общие операционные расходы', 'Расходы / Выручка',
                                        'EBIT', 'EBIT маржа', 'Коэфф.покрытия процентов', 'Чистая прибыль (убыток)',
                                        'Чистая рентабельность']

                BALANCE_STATEMENT_RUS = ['Общий долг', 'Заёмные средства (долгосрочные)',
                                         'Заёмные средства (краткосрочные)', 'Долг / Активы', 'Фин. левередж',
                                         'Капитал и резервы',
                                         'Текущая ликвидность', ]

                RATIO_ANALYSYS_RUS = ['Денежный цикл', 'Оборачиваемость ДЗ, дни', 'Оборачиваемость запасов, дни',
                                      'Оборачиваемость КЗ, дни']

                INCOME_STATEMENT = ['Revenue', 'Gross profit (loss)', 'Gross margin', 'Total operating costs',
                                    'Costs / Revenue',
                                    'EBIT', 'EBIT margin', 'ICR', 'Net profit', 'Net profitability']

                BALANCE_STATEMENT = ['Gross debt', 'Borrowed funds (long-term)', 'Borrowed funds (short-term)',
                                     'Debt / Assets',
                                     'Financial leverage', 'CAPITAL AND RESERVES', 'Equity ratio', 'Current ratio']

                RATIO_ANALYSYS = ['CCC', 'DSO, days', 'DIO, days', 'DPO, days']

                COMPANY_GROUP_SHARE_TEST = ['Revenue', 'EBIT', 'Gross debt', 'Total operating costs', 'Net profit']

                COMPANY_GROUP_SHARE = ['Revenue share', 'EBIT share', 'Gross debt share', 'Total operating costs share',
                                       'Net profit share']
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
                I
                II
                III
                IV
                V
                VI
                VII
                VIII
                IX
                # ________________________________________

                # company_data = {'total_assets': 1111111111, 'fixed_assets': 1111111111, 'long_term_investments': 1111111111,
                #            'total_long_term_assets': 1111111111, 'inventories': 1111111111,
                #            'accounts_receivable': 1111111111,
                #            'cash': 1111111111, 'short_term_investments': 1111111111,
                #            'total_short_term_assets': 1111111111,
                #            'equity': 1111111111, 'long_term_debt': 1111111111,
                #            'total_long_term_liabilities': 1111111111,
                #            'short_term_debt': 1111111111, 'total_short_term_liabilities': 1111111111,
                #            'accounts_payable': 1111111111,
                #            'revenue': 1111111111, 'cost_of_goods_sold': 1111111111,
                #            'gross_financial_result': 1111111111,
                #            'administrative_expanses': 1111111111, 'commercial_expanses': 1111111111,
                #            'operating_financial_result': 1111111111, 'other_operating_income': 1111111111,
                #            'other_opreating_expanses': 1111111111, 'financial_result_before_tax': 1111111111,
                #            'income_tax': 1111111111,
                #            'net_financial_result': 1111111111, 'cashflow_from_operations': 1111111111,
                #            'capital_expenses': 1111111111,
                #            'gross_debt': 2222222222, 'equity_ratio': 1.0, 'current_ratio': 1.0, 'debt_to_equity': 2.0,
                #            'gross_margin': 1.0, 'operating_margin': 1.0, 'return_on_assets': 1.0,
                #            'return_on_equity': 1.0}

            # тут можно выставлять рейтинг отдельной компании из группы
        # todo Блок оценки группы с учетом всех весов компаний в группе

        # todo Блок оценки рассматриваемой компании из группы с учетом грейда компании и группы
        return dict_with_reports

    def get_dict_with_company_grade(self):
        dict_with_company_grade = self.calculate_grade(self.dict_with_reports)
        return dict_with_company_grade