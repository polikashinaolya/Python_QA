from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt, sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "filename"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_strint(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbol) for i in range(random.randrange(maxlen))])


def random_month():
    return random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                          'September', 'October', 'November', 'December'])


def random_phone_number():
    symbol_for_phone_number = string.digits + '+' + ' ' + '-'
    return ''.join([random.choice(symbol_for_phone_number) for i in range(16)])


testdata = [
    Contact(firstname=random_strint('firstname', 10), middlename=random_strint('', 10),
            lastname=random_strint('lastname', 10), nickname=random_strint('', 10), title=random_strint('', 10),
            company=random_strint('company', 10), address=random_strint('', 10), phone_home=random_phone_number(),
            phone_mobile=random_phone_number(), phone_work=random_phone_number(), fax=random_phone_number(),
            email=random_strint('email', 10), email2=random_strint('', 10), email3=random_strint('', 10),
            homepage=random_strint('', 10), address2=random_strint('', 10), phone2=random_phone_number(),
            notes=random_strint('', 10), bday=random.choice(range(31)), bmonth=random_month(),
            byear=random.choice(range(3000)), aday=random.choice(range(31)), amonth=random_month(),
            ayear=random.choice(range(3000)))
            for i in range(n)
            ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as f_json:
    jsonpickle.set_encoder_options('json', indent=2)
    f_json.write(jsonpickle.encode(testdata))