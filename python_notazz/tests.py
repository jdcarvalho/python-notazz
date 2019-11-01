from unittest import TestCase
import os

from notazz.nfse import NFSeWrapper
from notazz.notazz import NotazzWrapper


class TestNotazz(TestCase):

    def setUp(self):
        NotazzWrapper.load_testing_env_variables()
        api_token = os.environ.get('API_TOKEN')
        self.notazz = NotazzWrapper(api_token)

    def test_create_nfse_pra_o_muneo(self):
        import uuid

        r = self.notazz.nfse.create_nfse(
            'Jorge Muneo Nakagawa',
            '626.179.730-77',
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            'Rua Maria das Bolas',
            '1334',
            'Em frente a casa de tio Toinho',
            'Centro',
            'São Paulo',
            'SP',
            '35.560-000',
            '11.98833-3322',
            'muneo@maestrus.com',
            ['muneo@maestrus.com', 'joao.carvalho@maestrus.com'],
            1.99,
            'Serviço de Pintura de Janelas',
            2, uuid.uuid4().hex,
        )
        resposta = r.json()
        self.assertTrue(all(
            [r.status_code == 200,
             resposta.get('codigoProcessamento') == '000']
        ))

    def test_update_nfse_pra_o_muneo(self):
        import uuid

        r = self.notazz.nfse.create_nfse(
            'Titio Avô',
            '626.179.730-77',
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            'Rua Maria das Bolas',
            '1334',
            'Em frente a casa de tio Toinho',
            'Centro',
            'São Paulo',
            'SP',
            '35.560-000',
            '11.98833-3322',
            'titio@avo.com',
            ['titio@avo.com', 'tigresa@avo.com'],
            1.99,
            'Serviço de remoção do Steve Pizza',
            2, uuid.uuid4().hex,
        )
        resposta = r.json()

        r1 = self.notazz.nfse.update_nfse(
            resposta.get('id'),
            'Buzz Lightyear',
            '626.179.730-77',
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            'Rua Maria das Bolas',
            '1334',
            'Em frente a casa de tio Toinho',
            'Centro',
            'São Paulo',
            'SP',
            '35.560-000',
            '11.98833-3322',
            'buzz@commando.com',
            ['buzz@commando.com', 'woody@commando.com'],
            2.99,
            'Serviço de Guincho Espacial',
            2, external_id=None,
        )

        resposta1 = r1.json()

        self.assertTrue(all(
            [r.status_code == 200,
             resposta.get('codigoProcessamento') == '000',
             r1.status_code == 200,
             resposta1.get('codigoProcessamento') == '000']
        ))

    def test_consultar_nfse(self):
        import uuid
        r = self.notazz.nfse.create_nfse(
            'Ana Boleta',
            '954.145.330-91',
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            'Rua Fala Fiote',
            '1334',
            'Ta Bao',
            'Centro',
            'São Paulo',
            'SP',
            '35.560-000',
            '11.98833-3322',
            'boleta@bola.com',
            ['boleta@bola.com', 'bonecojosias@boleta.com'],
            1.99,
            'Serviço de Fala Fiote',
            2, uuid.uuid4().hex,
        )
        r_create = r.json()

        r1 = self.notazz.nfse.get_by_id(r_create.get('id'))
        r_query = r1.json()

        self.assertTrue(all(
            [
                r.status_code == 200,
                r_create.get('codigoProcessamento') == '000',
                r1.status_code == 200,
                r_query.get('codigoProcessamento') == '000',
             ]
        ))

    def test_delete_nfse(self):
        import uuid
        r = self.notazz.nfse.create_nfse(
            'Ana Boleta',
            '954.145.330-91',
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            'Rua Fala Fiote',
            '1334',
            'Ta Bao',
            'Centro',
            'São Paulo',
            'SP',
            '35.560-000',
            '11.98833-3322',
            'muneo@maestrus.com',
            ['muneo@maestrus.com', 'joao.carvalho@maestrus.com'],
            1.99,
            'Serviço de Fala Fiote',
            2, uuid.uuid4().hex,
        )
        r_create = r.json()

        r1 = self.notazz.nfse.delete_nfse(r_create.get('id'))
        r_query = r1.json()

        self.assertTrue(all(
            [
                r.status_code == 200,
                r_create.get('codigoProcessamento') == '000',
                r1.status_code == 200,
                r_query.get('codigoProcessamento') == '000',
             ]
        ))
