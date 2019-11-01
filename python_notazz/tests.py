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
