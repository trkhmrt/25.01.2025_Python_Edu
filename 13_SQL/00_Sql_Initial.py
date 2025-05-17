"""
SQL(Structured Query Language)
Verilerin saklanabilmesi için kullanılan uygulamalardır.


Docker üzerinden mssql ayağa kaldırılacak.

1-Docker kurulumu
Docker indirilir ve kurulur
https://www.docker.com/products/docker-desktop/

Ardından terminalde bu komutlar sırayla çalıştırılır.

Mssql image'ı docker'a indirmek için
docker pull mcr.microsoft.com/mssql/server


Mssql ayağa kaldırmak için
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=yourStrong" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest

Azure data studio
https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio?tabs=win-install%2Cwin-user-install%2Credhat-install%2Cwindows-uninstall%2Credhat-uninstall
"""