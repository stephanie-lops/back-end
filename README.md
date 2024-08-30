# Minha API - Stephanie Lopes

Este pequeno projeto é o meu MVP da Sprint 1 do curso de **Desenvolvimento Full Stack Básico** 

O objetivo aqui é listar os produtos de uma loja de roupas, com o intuito de registrar um inventário dos itens.

Utilizando 3 informações: Nome do item, tamanho e quantidade.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Criar ambiente virtual env

```
python3 -m venv env
```

Ativar ambiente virtual env (Windows)

```
.\env\Scripts\activate
```

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.



https://jpn01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fe2.udemymail.com%2Fls%2Fclick%3Fupn%3Du001.jFOE0QPBHjKVAlFBmmJE1CrCFEF-2FMIjtbqbLdw3wnkY1RwXZwpxymh73alPYnPhTuVGt2TZUmiWbEfyIw02z-2BYlXnRNskpTpAn3u07MAILWnPBYEoe6WHNOiVQxldjG3ZmoWJ8sL2kbgrozjZx3yYLxNvTUyYZmDLkbv2GiVxajdyHmOpgognw-2F3pyI0XNbh-2BSv6TmKj-2FhLoVk9uNoYfVuS-2BpNk-2BApZk3CX8qFQX-2FeuLsErkyHt-2BdHrxkEo9vJLQat4HSMfblH3v3s6upHan5FfZ9s-2BtN86xSAM3wWraz2mTXzZKxuxfSTeziflUGyqsU6Ey_uoJNvF-2FASjth9StXKTRb2CW4hWKpwtP12hDgTu5zRmvNG6YK7Yj7J8KYh1Tq1OoUqpRB6EKTXsSjosxYx7rUI0kKio7qJfQnLO-2FO4-2F7TkWnE08cMxEA4yYoQ5fjkc8J56dEM5sZKIPCBadmEh6us632Gvbdfsfhnjjk2SPjh3RI0IX-2FRYWulvwp1NyZhVmNm6lmLDqmwuLBAxFvz7nGUGcUPIsDghadjdBUh0pC6i1EuG0-2F2Ox0cqRZgbs-2BWUjjQYX6VYgjc8WWN-2BYSU9XOltdtgAziqbVJypjC8TlObxpTMF4uhSNi9oKs1VwFpLgt-2Byjsa-2FZX3MIODNkZ79bRojwpl6dK3imm-2F4PGV-2BZ2NLaNgT2M2lIurp8MW27gAhKFE&data=05%7C02%7Cstephanie.barros%40yamaha-motor.com.br%7Ccef20c6640db48cce6a108dcc897ae6c%7C76684a67d81643ce93f929b6f72f823f%7C1%7C0%7C638605801031314948%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=V%2BD7JxOHnc1lJ1gp3hLWofb82jroP3KjhMYfEU9xeP4%3D&reserved=0
