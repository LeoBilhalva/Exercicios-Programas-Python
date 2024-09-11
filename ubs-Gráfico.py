import folium
from folium.plugins import MarkerCluster
unidades = {}
with open("Faculdade\\Exercicios-Programas-Python\\Unidades_Basicas_Saude-UBS.csv") as csv:
    csv.readline()
    for linha in csv:
        aux = linha[:-1].split(";")
        lat = aux[6]
        lon = aux[7]
        uf = aux[1]
        if lat != '' and lon != '' and uf == "43":
            nome = aux[3][1:-1]
            logr = aux[4][1:-1]
            bairro = aux[5][1:-1]
            lat = float(lat.replace(",", "."))
            lon = float(lon.replace(",", "."))

            unidades[nome] = (logr, bairro, lat, lon)
ubs = input("Digite o nome da unidade: ").upper()
if ubs in unidades:
    print(unidades[ubs])
else:
    for nome in unidades.keys():
        if ubs in nome:
            print("Unidade encontrada: ", nome, unidades[nome])
map = folium.Map(location=[-30.7135040, -52.6904297], zoom_start=6.7, min_zoom=5)
marker_cluster = MarkerCluster().add_to(map)
for aux in unidades.values():
    folium.CircleMarker(radius=1, location=[
                        aux[2], aux[3]]).add_to(marker_cluster)
map.show_in_browser()