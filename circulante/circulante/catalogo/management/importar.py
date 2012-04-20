# coding: utf-8

import io

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<arq_delimitado_por_tabs>'
    help = 'Importa massa de dados da livraria'

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError('Informe o nome do arquivo a Importar')
        nome_arq = args
        with io.open(nomme_arq) as arq_ent:
            linhas = arq_ent.readlines() 
        self.stdout.write('Importando: %s linhas \n' % len(linhas)) 
   
