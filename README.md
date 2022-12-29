# Geo 3DR

Geotagger para logs da 3DR, </br>
O script irá:
- pegar todas a CAM messages do logs
- excluir as repetidas 
- excluir as linhas em que a altitude é muito menor que a altitude média de voo (diferença maior que 50m)

## Set-up

Em uma pasta, colocar o arquivo **3DR_geotagger.py**, criar uma pasta **logs**,
colocar o log dentro com o nome **raw.log**
e dentro da pasta **logs** criar um arquivo vazio chamado **geo.txt**

Na **linha 10** do **3DR_geotagger.py** colocar o número da primeira imagem:
```py
# Colocar o número da primeira  imagem ex:   DSC00013.JPG -> 13   DSC00135.JPG -> 135
image_number = 13
```

Na **linha 12** colocar a altitude média em relação ao nível do mar:
```py
# Colocar o altitude média do voo em relação ao mar
flight_altitude = 1200
```
Caso você não saiba a altitude, poderá rodar o script uma primeira vez com um valor teste de altitude e no Terminal serão impressas as altitudes. </br>
Você deve pegar o valor médio dessas altitudes (não precisa ser exato).

Rodar o programa no terminal com o comando:
```
py 3DR_geotagger.py
```