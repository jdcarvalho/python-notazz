from notazz.base import NotazzBase, NotazzException
from datetime import datetime


class NFSeWrapper(NotazzBase):

    PEOPLE_KIND_SINGLE = 'F'
    PEOPLE_KIND_COMPANY = 'J'
    PEOPLE_KIND_FOREIGN = 'E'

    ISS_KIND_RETAINED = '1'
    ISS_KIND_NOT_RETAINED = '0'

    def create_nfse(
            self, name, document, people_kind, address,
            add_no, add_complement, neighborhood, city,
            province, zip_code, phone, email, receivers,
            doc_base_value, doc_desc, doc_iss_rate,
            external_id, ie='', im='', sale_id=None,
            doc_competence=None, doc_cnae=None,
            doc_lc116=None, doc_iss_kind=None,
            city_service_code=None, city_service_desc=None
    ):
        """
        This method allows to create a Brazilian NFSe with NOTAZZ APP
        :param name: Nome do Cliente
        :param document: Documento do Cliente CPF ou CNPJ
        :param ie: Inscrição Estadual
        :param im: Inscrição Municipal
        :param people_kind: Tipo de Pessoa. (Ver Constantes PEOPLE_KIND)
        :param address: Endereço
        :param add_no: Numero do Endereço
        :param add_complement: Complemento de Endereço
        :param neighborhood: Bairro
        :param city: Cidade (Sem abreviações)
        :param province: Estado
        :param zip_code: CEP
        :param phone: Telefone
        :param email: Email
        :param receivers: Lista Python de e-mails para a NFSe ser enviada
        :param doc_base_value: Valor base da Nota Fiscal de Serviço
        :param doc_desc: Descrição da Nota Fiscal de Serviço
        :param doc_iss_rate: Percentual de ISS
        :param external_id: Identificador Externo
        :param sale_id: Identificador da Venda (Opcional)
        :param doc_competence: Data da Competência (Opcional)
        :param doc_cnae: CNAE (Opcional)
        :param doc_lc116: Código LC116 (Opcional)
        :param doc_iss_kind: Tipo de ISS (Ver constantes ISS_KIND) Opcional
        :param city_service_code: Código de serviço do Municipio
        :param city_service_desc: Descrição de serviço do Municipio
        :return:
        """
        name = name.strip()
        try:
            idoc = [str(s) for s in document.split() if s.isdigit()]
            document = ''.join(idoc)
        except:
            raise NotazzException('Documento inválido')

        address = address.strip()
        add_no = add_no.strip()

        neighborhood = neighborhood.strip()
        city = city.strip()
        province = province.strip()

        try:
            izip = [str(s) for s in zip_code.split() if s.isdigit()]
            zip_code = ''.join(izip)
        except:
            raise NotazzException('CEP Inválido')

        if people_kind not in [
            NFSeWrapper.PEOPLE_KIND_COMPANY,
            NFSeWrapper.PEOPLE_KIND_SINGLE,
            NFSeWrapper.PEOPLE_KIND_FOREIGN]:
            raise NotazzException('Erro de Programação: Tipo de pessoa Inválido')

        payload = {
            'API_KEY': self.api_key,
            'METHOD': 'create_nfse',
            'DESTINATION_NAME': name,
            'DESTINATION_TAXID': document,
            'DESTINATION_TAXTYPE': people_kind,
            'DESTINATION_STREET': address,
            'DESTINATION_NUMBER': add_no,
            'DESTINATION_DISTRICT': neighborhood,
            'DESTINATION_CITY': city,
            'DESTINATION_UF': province,
            'DESTINATION_ZIPCODE': zip_code,
            'DOCUMENT_BASEVALUE': doc_base_value,
            'DOCUMENT_DESCRIPTION': doc_desc,
            'EXTERNAL_ID': external_id,
        }
        if add_complement:
            add_complement = add_complement.strip()
            payload.update({
                'DESTINATION_COMPLEMENT': add_complement,
            })

        if ie:
            iie = [str(s) for s in ie.split() if s.isdigit()]
            ie = ''.join(iie)
            payload.update({
                'DESTINATION_IE': ie,
            })
        if im:
            iim = [str(s) for s in im.split() if s.isdigit()]
            im = ''.join(iim)
            payload.update({
                'DESTINATION_IM': im,
            })
        if phone:
            iphone = [str(s) for s in phone.split() if s.isdigit()]
            phone = ''.join(iphone)
            payload.update({
                'DESTINATION_PHONE': phone,
            })
        if email:
            iemail = [str(s) for s in email.split() if s.isdigit()]
            email = ''.join(iemail)
            payload.update({
                'DESTINATION_EMAIL': email
            })
        if receivers:
            if not isinstance(receivers, list):
                raise NotazzException('"receivers" precisa ser do tipo lista')
            resultset = dict()

            i = 1
            for r in receivers:
                resultset[str(i)] = {
                    'EMAIL': r,
                }
                i = i + 1
        if doc_competence:
            if isinstance(doc_competence, datetime):
                payload.update({
                    'DOCUMENT_COMPETENCE': doc_competence.strftime('%Y-%m-%d')
                })
        if doc_cnae:
            i_cnae = [str(s) for s in doc_cnae.split() if s.isdigit()]
            doc_cnae = ''.join(i_cnae)
            payload.update({
                'DOCUMENT_CNAE': doc_cnae,
            })
        if doc_lc116:
            doc_lc116 = doc_lc116.strip()
            payload.update({
                'SERVICE_LIST_LC116': doc_lc116,
            })

        if doc_iss_kind:
            if doc_iss_kind not in [
                NFSeWrapper.ISS_KIND_NOT_RETAINED,
                NFSeWrapper.ISS_KIND_RETAINED
            ]:
                raise NotazzException('Tipo de ISS Inválido')
            payload.update({
                'WITHHELD_ISS': doc_iss_kind,
            })
        if city_service_code:
            payload.update({
                'CITY_SERVICE_CODE': city_service_code,
            })
        if city_service_desc:
            payload.update({
                'CITY_SERVICE_DESCRIPTION': city_service_desc,
            })
        if sale_id:
            payload.update({
                'SALE_ID': sale_id,
            })
        payload.update({
            'ALIQUOTAS': {
                'ISS': doc_iss_rate,
                # TODO: Onde o buraco é mais embaixo
            }
        })
        r = self.do_post_request(NFSeWrapper.PRD_URI, params=payload)
        return r

    def update_nfse(self):
        pass

    def get_by_id(self):
        pass

    def query_nfse(self):
        pass

    def delete_nfse(self):
        pass

    def cancel_nfse(self):
        pass

    def unlink(self):
        pass

    def list_cities(self):
        pass