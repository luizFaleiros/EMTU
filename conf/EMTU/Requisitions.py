from src.conf.EMTU.Settings import URL, SENHA, USUARIO

import requests
from requests.auth import HTTPBasicAuth


class Requisistions(object):


    def Line(self, line):
        """
        :param line: aqui vai o numero da linha que o usuario pediu
        :return: ela vai retornar None caso a linha não seja encontrada ou um array de diciionario com todas as linhas e o sentido delas e quantos onibus tem em cada linha
        """
        url = URL + "rest/usuarios/v2?linha="+line
        requisition = requests.get(url, auth=(USUARIO, SENHA))
        if requisition.status_code == 200 and len(requisition.json()) !=0:
            response = requisition.json()
            response = response['linhas']
        else:
            response = None
        return response

    def Position(self, lon, lat):
        """

        :param lon: Longitude do usuario
        :param lat: latitude do usuario
        :return: retorna todos os onibus que passam no ponto em que o usuario se encontra, em caso de não haver onibus, ou o usuario estiver longe do ponto, retornara None
        """
        url = f"/rest/usuarios/v2?mode=ponto&distancia=maisProximo&latitude={lat}&longitude={lon}"
        url = URL+url
        requisition = requests.get(url, auth=(USUARIO, SENHA))
        if requisition.status_code == 200 and len(requisition.json()) !=0:
            response = requisition.json()
            response = response['linhas']
        else:
            response = None
        return response

