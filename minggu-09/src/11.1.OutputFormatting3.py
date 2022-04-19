import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252' (Output)
conv = locale.localeconv()          # mendapatkan pemetaan konvensi
x = 1234567.8
locale.format("%d", x, grouping=True)
# '1,234,567' (Output)
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
# '$1,234,567.80' (Output)