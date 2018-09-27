import argparse
import errno
import sys
from csv import reader as csv_reader
from BrowserController import BrowserController
from Status import Status


browser = BrowserController()

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('csv', metavar='csv', type=str, nargs='?',
                    help='Arquivo csv com números e mensagens', default='contatos.csv')

args = parser.parse_args()
if args.csv:
    print('Csv carregado!')
else:
    print('Falha ao carregar csv!')
    print('Abortando operação.')
    sys.exit(errno.ENODEV)

status = []

with open(args.csv, newline='', encoding='utf-8') as file:
    rows = csv_reader(file)
    print('Escaneie o QR code do whats web antes de prosseguir')
    input('Press Enter to continue...')
    for row in rows:
        num = row[0].replace('+', '')
        msg = row[1]
        browser.send_message(num=num, msg=msg)
        Status(num=num, suceesso=True)

    browser.close()

with open('resultados.csv', 'w+') as file:
    for status in Status.list:
        file.write(status.to_csv()+'\n')
