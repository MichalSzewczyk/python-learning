import re

pattern = 'RUN \d{6} COMPLETED. OUTPUT IN FILE \w+.dat. .*'
# ex1
with open('atoms.log') as atoms:
    for line in atoms:
        if re.search(pattern, line) is not None:
            print(line)

# ex2
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
pattern = '(\w{3} \d{2} \d{2}:\d{2}:\d{2}) noether sshd\[5805\]: Invalid user (\w+) from (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
result = 'Niepoprawna nazwa użytkownika: "{}", połaczenie z {} nawiązano {}'


def convert_to_pl_month(month):
    month = month.lower()
    if month == 'jan':
        return 'stycznia'
    elif month == 'feb':
        return 'lutego'
    elif month == 'mar':
        return 'marca'
    elif month == 'apr':
        return 'kwietnia'
    elif month == 'may':
        return 'maja'
    elif month == 'jun':
        return 'czerwca'
    elif month == 'jul':
        return 'lipca'
    elif month == 'oug':
        return 'sierpnia'
    elif month == 'sep':
        return 'wrzesnia'
    elif month == 'oct':
        return 'pazdziernika'
    elif month == 'now':
        return 'listopada'
    elif month == 'dec':
        return 'grudnia'
    else:
        print('fail')


def convert_date(date_string: str):
    result = ''
    result += date_string[4:6] + ' '
    result += convert_to_pl_month(date_string[0:3]) + ' o godzinie '
    result += date_string[7:12]
    return result


print(convert_date('Jun 29 20:18:40'))

with open('messages.txt') as messages:
    for line in messages:
        search_result = re.search(pattern, line)
        if search_result is not None:
            print(result.format(search_result.group(2), search_result.group(3), convert_date(search_result.group(1))))
