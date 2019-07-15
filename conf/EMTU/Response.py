from conf.EMTU.Requisitions import Requisistions


class Response(Requisistions):

    def ResponseLine(self, line):
        r = self.Line(line)
        sentidoIndo = 0
        sentidoVolta = 0
        ida = []
        volta = []
        msg = '-------------------------------------------------- \n'
        if r is not None:
            for i in range(len(r)):
                name = r[i]['codigo']
                qnt = len(r[i]['veiculos'])
                msg += f"Linha: {name}\n"
                msg += f"quatidade de onibus ativos: {qnt}\n"
                for j in range(qnt):
                    veiculos = r[i]['veiculos']
                    if veiculos[j]['sentidoLinha'] == 'ida' and veiculos[j]['dentroRota'] == True:
                        sentidoIndo += 1
                        ida.append([veiculos[j]['latitude'], veiculos[j]['longitude']])
                    elif veiculos[j]['sentidoLinha'] == 'volta' and veiculos[j]['dentroRota'] == True:
                        sentidoVolta += 1
                        volta.append([veiculos[j]['latitude'], veiculos[j]['longitude']])
                msg += f"Quantidade de onibus indo: {sentidoIndo}\n"
                msg += f"Quantidade de onibus voltando: {sentidoVolta}\n"
                msg += '-------------------------------------------------- \n'
            return msg, ida, volta

        else:
            return "Onibus não encontrado"

    def ResponsePosition(self, lon, lat):
        r = self.Position(lon, lat)
        msg = '-------------------------------------------------- \n'
        msg +="Onibus que passam Nesse ponto\n"
        if r is not None:
            for i in range(len(r)):
                name = r[i]['codigo']
                msg += f"Numero da linha: {name}\n"
            msg += '-------------------------------------------------- \n'
            return msg
        else:

            return "Onibus não encontrado"



