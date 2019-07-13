from src.conf.EMTU.Requisitions import Requisistions
from geopy.geocoders import Nominatim


class Response(Requisistions):

    def ResponseLine(self, line):
        r = self.Line(line)
        sentidoIndo = 0
        sentidoVolta = 0
        locationida = []
        locationvolta = []
        geolocator = Nominatim(user_agent="https://nominatim.openstreetmap.org/")
        msg = '-------------------------------------------------- \n'
        if r is not None:
            for i in range(len(r)):
                name = r[i]['codigo']
                qnt = len(r[i]['veiculos'])
                for j in range(len(r[i]['veiculos'])):
                    veiculos = r[i]['veiculos']
                    if veiculos[j]['sentidoLinha'] == 'ida' and veiculos[j]['dentroRota'] == True:
                        sentidoIndo += 1
                        latlon = f"{veiculos[j]['latitude']}, {veiculos[j]['longitude']}"
                        locationida.append(geolocator.reverse(latlon))

                    elif veiculos[j]['sentidoLinha'] == 'volta' and veiculos[j]['dentroRota'] == True:
                        sentidoVolta += 1
                        latlon = f"{veiculos[j]['latitude']}, {veiculos[j]['longitude']}"
                        locationvolta.append(geolocator.reverse(latlon))

                msg += f"Linha: {name}\n"
                msg += f"quatidade de onibus ativos: {qnt}\n"
                msg += f"Quantidade de onibus indo: {sentidoIndo}\n"
                msg += f"Quantidade de onibus voltando: {sentidoVolta}\n"
                msg += '-------------------------------------------------- \n'
                msg += '\n\n'
                msg += 'posição dos onibus indo para o destino\n\n'
                for i in range(len(locationida)):
                    msg += f'{locationida[i]}\n\n'
                msg += '-------------------------------------------------- \n'
                msg += '\n\n'
                msg += 'posição dos onibus Voltando para o destino\n\n'
                for i in range(len(locationida)):
                    msg += f'{locationvolta[i]}\n\n'
            return msg
        else:
            return "Onibus não encontrado"

    def ResponsePosition(self, lon, lat):
        r = self.Position(lon, lat)
        sentidoIndo = 0
        sentidoVolta = 0
        locationida = []
        locationvolta = []
        geolocator = Nominatim(user_agent="https://nominatim.openstreetmap.org/")
        msg = '-------------------------------------------------- \n'
        res = []
        msg = '-------------------------------------------------- \n'
        if r is not None:
            for i in range(len(r)):
                name = r[i]['codigo']
                qnt = len(r[i]['veiculos'])
                for j in range(len(r[i]['veiculos'])):
                    veiculos = r[i]['veiculos']
                    if veiculos[j]['sentidoLinha'] == 'ida' and veiculos[j]['dentroRota'] == True:
                        sentidoIndo += 1
                        latlon = f"{veiculos[j]['latitude']}, {veiculos[j]['longitude']}"
                        locationida.append(geolocator.reverse(latlon))

                    elif veiculos[j]['sentidoLinha'] == 'volta' and veiculos[j]['dentroRota'] == True:
                        sentidoVolta += 1
                        latlon = f"{veiculos[j]['latitude']}, {veiculos[j]['longitude']}"
                        locationvolta.append(geolocator.reverse(latlon))

                msg += f"Linha: {name}\n"
                msg += f"quatidade de onibus ativos: {qnt}\n"
                msg += f"Quantidade de onibus indo: {sentidoIndo}\n"
                msg += f"Quantidade de onibus voltando: {sentidoVolta}\n"
                msg += '-------------------------------------------------- \n'
                msg += '\n\n'
                msg += 'posição dos onibus indo para o destino\n\n'
                for i in range(len(locationida)):
                    msg += f'{locationida[i]}\n\n'
                msg += '-------------------------------------------------- \n'
                msg += '\n\n'
                msg += 'posição dos onibus Voltando para o destino\n\n'
                for i in range(len(locationida)):
                    msg += f'{locationvolta[i]}\n\n'
                if qnt > 0:
                    res.append(msg)
                else:
                    res.append(f"{name} Não esta programado para passar perto da sua posição")
            return res
        else:
            res = ['Onibus não encontrado']
            return res


