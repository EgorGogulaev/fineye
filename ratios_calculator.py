class CalculatorRatiosAndDynamic:
    def __init__(self, dict_with_reports: dict[dict]):
        self.dict_with_reports = dict_with_reports


    @staticmethod
    def calculate_ratios(dict_with_reports):
        """
        Расчет финасовых показателей
        :param dict_with_reports: dict[dict]
        :return: dict[dict]
        """
        for OGRN in list(dict_with_reports[list(dict_with_reports)[0]]):
            for report_period in list(dict_with_reports[list(dict_with_reports)[0]][OGRN]):

                # __________________________________________________________________________________________________________
                # BALANCE SHEET RATIOS
                period: int = report_period
                total_assets = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("total_assets", None)                                # Общая сумма АКТИВЫ == Общая сумма ПАССИВЫ | Валюта БАЛАНСА

                # assets
                fixed_assets = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("fixed_assets", None)                                # Долгосрочные активы
                long_term_investments = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("long_term_investments", None)              # Долгосрочные вложения
                total_long_term_assets = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("total_long_term_assets", None)            # Общая сумма всех долгосрочных активов
                inventories = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("inventories", None)                                  # Запасы
                accounts_receivable = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("accounts_receivable", None)                  # Дебиторская задолженность                 | то, что должны "мне"
                cash = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("cash", None)                                                # Деньги на расчетном счете                 | наиболее ликвидный актив
                short_term_investments = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("short_term_investments", None)            # Краткосрочные вложения                    | вложение денег в пользование
                total_short_term_assets = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("total_short_term_assets", None)          # Общая сумма краткосрочных активов

                # equity & liabilities
                equity = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("equity", None)                                            # Собственный капитал компании              | Складывается из капиталов компании
                long_term_debt = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("long_term_debt", None)                            # Долгосрочные займы/кредиты от третьих лиц (свыше кода)
                total_long_term_liabilities = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("total_long_term_liabilities", None)  # Долгосрочные обязательства
                short_term_debt = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("short_term_debt", None)                          # Краткосрочные займы/кредиты от третьих лиц
                total_short_term_liabilities = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("total_short_term_liabilities", None)# Краткосрочные обязательства
                accounts_payable = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("accounts_payable", None)                        # Кредиторская задолженность поставщикам

                gross_debt = long_term_debt + short_term_debt \
                    if long_term_debt and short_term_debt else long_term_debt \
                    if long_term_debt and not short_term_debt else short_term_debt \
                    if short_term_debt and not long_term_debt else None

                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["gross_debt"] = gross_debt


                # PROFI & LOSS RATIOS
                revenue = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("revenue", None)                                          # Выручка                                    | Продажи за период
                cost_of_goods_sold = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("cost_of_goods_sold", None)                    # Себестоимость проданных товаров/услуг      | Затраты на товары/услуги
                gross_financial_result = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("gross_financial_result", None)            # Валовая прибыль                            | Прибыль (Без учета себестоимости)
                administrative_expanses = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("administrative_expanses", None)          # Административные расходы                   | Организационные затраты производства
                commercial_expanses = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("commercial_expanses", None)                  # Коммерческие расходы                       | Расходы на продажу товаров
                operating_financial_result = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("operating_financial_result", None)    # Операционный результат(прибыль/убыток)     | Результат от основной деятельности
                other_operating_income = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("other_operating_income", None)            # Прочие доходы                              | Ситуативные доходы
                other_opreating_expanses = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("other_opreating_expanses", None)        # Прочие расходы                             | Ситуативные расходы
                financial_result_before_tax = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("financial_result_before_tax", None)  # Результат до налогов                       | До вычета налогов, сколько компания получила(прибыли/убытков)
                income_tax = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("income_tax", None)                                    # Налог на прибыль
                net_financial_result = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("net_financial_result", None)                # Чистая прибыль/убыток                      | Результат, после вычета всех налогов (при прибыли -> нераспределенный капитал)


                # CASHFLOW RATIOS
                cashflow_from_operations = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("cashflow_from_operations", None)  # Денежный поток от текущей операционной деятельности (CFO)
                capital_expenses = dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get("capital_expenses", None)  # Капитальные расходы
                # __________________________________________________________________________________________________________

                # FINANCIAL RATIOS
                # Автономия капитала
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["equity_ratio"] = equity / total_assets if equity and total_assets and total_assets > 0 else None

                # Текущая ликвидность                       | Норма - 1
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["current_ratio"] = total_short_term_assets / total_short_term_liabilities \
                    if total_short_term_liabilities and total_short_term_assets and total_short_term_assets > 0 else None

                # Финансовый рычаг                          | Отношение всего долга к капиталу (Норма - до 2)
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["debt_to_equity"] = gross_debt / equity if gross_debt and equity and equity > 0 else None

                # Валовая маржа                             | Норма ~ 0.15-0.25
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["gross_margin"] = gross_financial_result / revenue \
                    if gross_financial_result and revenue and revenue > 0 and gross_financial_result >= 0 else 0 \
                    if gross_financial_result < 0 and revenue > 0 else None

                # Оперативная валовая маржа                 | Норма ~ 0.05-0.1
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["operating_margin"] = operating_financial_result / revenue \
                    if operating_financial_result and revenue and revenue > 0 and operating_financial_result >= 0 else 0 \
                    if operating_financial_result < 0 and revenue > 0 else None

                # Рентабельность активов к активам компании | Норма -> Зависит от типа деятельности (чем больше тем лучше)
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["return_on_assets"] = net_financial_result / total_assets \
                    if net_financial_result and total_assets and total_assets > 0 else None

                # Рентабельность активов к капиталу         | Норма -> Зависит от типа деятельности (чем больше тем лучше)
                dict_with_reports[list(dict_with_reports)[0]][OGRN][period]["return_on_equity"] = net_financial_result / equity \
                    if net_financial_result and equity and equity > 0 else None

            return dict_with_reports

    @staticmethod
    def calculate_dynamics(dict_with_reports):
        """
        Метод расчета динамики показателей. Результат сохраняется ввиде десятичной дроби по каждому показателю
        :param dict_with_reports: dict[dict]
        :return: dict[dict]
        """

        # TODO Сделать логику сбора данных текущего и предыдущего года
        for OGRN in dict_with_reports[list(dict_with_reports)[0]]:
            if len(dict_with_reports[list(dict_with_reports)[0]][OGRN]) == 1:
                dict_with_reports['dynamic'] = False
                return dict_with_reports
            else:

                for report_period in list(dict_with_reports[list(dict_with_reports)[0]][OGRN])[1:]:
                    period: int = report_period

                    # BALANCE_DYNAMIC
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['fixed_assets_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['fixed_assets'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['fixed_assets']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('fixed_assets', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('fixed_assets', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['long_term_investments_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['long_term_investments'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['long_term_investments']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('long_term_investments', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('long_term_investments', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_long_term_assets_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_long_term_assets'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['total_long_term_assets']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('total_long_term_assets', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('total_long_term_assets', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['inventories_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['inventories'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['inventories']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('inventories', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('inventories', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['accounts_receivable_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['accounts_receivable'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['accounts_receivable']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('accounts_receivable', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('accounts_receivable', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cash_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cash'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['cash']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('cash', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('cash', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['short_term_investments_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['short_term_investments'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['short_term_investments']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('short_term_investments', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('short_term_investments', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_short_term_assets_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_short_term_assets'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['total_short_term_assets']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('total_short_term_assets', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('total_short_term_assets', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['equity_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['equity'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['equity']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('equity', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('equity', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['long_term_debt_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['long_term_debt'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['long_term_debt']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('long_term_debt', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('long_term_debt', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_long_term_liabilities_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_long_term_liabilities'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['total_long_term_liabilities']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('total_long_term_liabilities', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('total_long_term_liabilities', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['short_term_debt_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['short_term_debt'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['short_term_debt']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('short_term_debt', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('short_term_debt', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['accounts_payable_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['accounts_payable'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['accounts_payable']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('accounts_payable', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('accounts_payable', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_short_term_liabilities_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['total_short_term_liabilities'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['total_short_term_liabilities']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('total_short_term_liabilities', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('total_short_term_liabilities', None) else None
                    # p & l
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['revenue_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['revenue'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['revenue']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('revenue', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('revenue', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cost_of_goods_sold_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cost_of_goods_sold'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['cost_of_goods_sold']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('cost_of_goods_sold', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('cost_of_goods_sold', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['gross_financial_result_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['gross_financial_result'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['gross_financial_result']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('gross_financial_result', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('gross_financial_result', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['administrative_expanses_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['administrative_expanses'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['administrative_expanses']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('administrative_expanses', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('administrative_expanses', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['commercial_expanses_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['commercial_expanses'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['commercial_expanses']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('commercial_expanses', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('commercial_expanses', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['operating_financial_result_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['operating_financial_result'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['operating_financial_result']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('operating_financial_result', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('operating_financial_result', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['other_operating_income_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['other_operating_income'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['other_operating_income']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('other_operating_income', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('other_operating_income', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['other_opreating_expanses_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['other_opreating_expanses'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['other_opreating_expanses']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('other_opreating_expanses', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('other_opreating_expanses', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['financial_result_before_tax_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['financial_result_before_tax'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['financial_result_before_tax']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('financial_result_before_tax', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('financial_result_before_tax', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['income_tax_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['income_tax'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['income_tax']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('income_tax', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('income_tax', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['net_financial_result_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['net_financial_result'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['net_financial_result']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('net_financial_result', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('net_financial_result', None) else None

                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cashflow_from_operations_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['cashflow_from_operations'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['cashflow_from_operations']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('cashflow_from_operations', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('cashflow_from_operations', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['capital_expenses_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['capital_expenses'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['capital_expenses']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('capital_expenses', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('capital_expenses', None) else None

                    # RATIOS_DYNAMICS (!!!)
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['equity_ratio_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['equity_ratio'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['equity_ratio']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('equity_ratio', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('equity_ratio', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['current_ratio_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['current_ratio'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['current_ratio']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('current_ratio', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('current_ratio', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['debt_to_equity_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['debt_to_equity'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['debt_to_equity']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('debt_to_equity', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('debt_to_equity', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['gross_margin_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['gross_margin'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['gross_margin']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('gross_margin', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('gross_margin', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['operating_margin_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['operating_margin'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['operating_margin']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('operating_margin', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('operating_margin', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['return_on_assets_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['return_on_assets'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['return_on_assets']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('return_on_assets', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('return_on_assets', None) else None
                    dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['return_on_equity_dynamics'] = (dict_with_reports[list(dict_with_reports)[0]][OGRN][period]['return_on_equity'] / dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1]['return_on_equity']) - 1 if dict_with_reports[list(dict_with_reports)[0]][OGRN][period - 1].get('return_on_equity', None) and dict_with_reports[list(dict_with_reports)[0]][OGRN][period].get('return_on_equity', None) else None
                    # ______________________________________________________________________________________________________
            dict_with_reports['dynamic'] = True
            return dict_with_reports

    def get_dict_with_ratios_and_dynamics(self):
        dict_with_ratios_and_dynamics = self.calculate_dynamics(self.calculate_ratios(self.dict_with_reports))
        return dict_with_ratios_and_dynamics
