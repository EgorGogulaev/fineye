class CombinedFinancialCalculator:
    """Класс, суммирующий финансовые показатели и коэффициенты, выдающий комбинированный финансовый очет"""

    def __init__(self, dict_with_reports):
        self.dict_with_reports = dict_with_reports

    @staticmethod
    def calculate_combined_financial(dict_with_reports):
        dict_with_reports[list(dict_with_reports)[0]]["COMBINED"] = {}
        for OGRN in list(dict_with_reports[list(dict_with_reports)[0]]):  # Рассчет "COMBINED"
            if OGRN != "COMBINED":
                for year in list(dict_with_reports[list(dict_with_reports)[0]][OGRN]):
                    if not dict_with_reports[list(dict_with_reports)[0]]["COMBINED"].get(year, None):
                        dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year] = {}
                    for item in list(dict_with_reports[list(dict_with_reports)[0]][OGRN][year]):
                        if dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year].get(item, None):  # Если отсутствует показатель, то он не суммируется в "COMBINED"
                            if dict_with_reports[list(dict_with_reports)[0]][OGRN][year].get(item, None) or isinstance(dict_with_reports[list(dict_with_reports)[0]][OGRN][year].get(item, None), (int, float)):
                                if dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year][item] == "n/a":
                                    dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year][item] = 0
                                dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year][item] += dict_with_reports[list(dict_with_reports)[0]][OGRN][year][item]
                        else:
                            dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year][item] = dict_with_reports[list(dict_with_reports)[0]][OGRN][year][item] if dict_with_reports[list(dict_with_reports)[0]][OGRN][year][item] else "n/a"

        for year_combined in list(dict_with_reports[list(dict_with_reports)[0]]["COMBINED"]):  # Приведение строк 'n/a' к общему виду "пустоты" - None
            for item_combined in dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year_combined]:
                if dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year_combined][item_combined] == "n/a":
                    dict_with_reports[list(dict_with_reports)[0]]["COMBINED"][year_combined][item_combined] = None

        return dict_with_reports

    def get_dict_with_reports_and_combined_report(self):
        dict_with_reports_and_combined_report = self.calculate_combined_financial(
            self.dict_with_reports)
        return dict_with_reports_and_combined_report