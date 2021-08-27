-- CREATE DATABASE agregacao;

 CREATE TABLE categorias(
	id SERIAL PRIMARY KEY,
 	nome VARCHAR(60) NOT NULL
 );

CREATE TABLE produtos(
	id SERIAL PRIMARY KEY, 
	descricao VARCHAR(60) NOT NULL,
	preco_venda DECIMAL(8,2) NOT NULL,
	preco_custo MONEY NOT NULL,
	id_categoria INT REFERENCES categorias(id) NOT NULL
 );

 INSERT INTO categorias (nome) VALUES ('Material Escolar');
 INSERT INTO categorias (nome) VALUES ('Acessório Informática');
 INSERT INTO categorias (nome) VALUES ('Material Escritório');
 INSERT INTO categorias (nome) VALUES ('Game');

 INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caderno', 5.45, 2.30, 1);
 INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caneta', 1.20, 0.45, 1);
 INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Pendrive 32GB', 120.54, 32.55, 2);
 INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Mouse', 17.00, 4.30, 2);
 
 select max(preco_venda) from produtos;
 select min(preco_venda) from produtos;
 
 
 select avg(preco_venda) from produtos;
 
 select round(avg(preco_venda)::numeric,2) from produtos; -- reduzindo para 2 casas decimais
 
 
 select count(preco_venda) as Quantidade from produtos where id_categoria = 1;
 
 
 
 -- group by
 select id_categoria, max(preco_venda) from produtos GROUP BY id_categoria; -- agrupando por id
 
 -- having
 select id_categoria, max(preco_venda) from produtos GROUP BY id_categoria HAVING MAX(preco_venda) > 10;
 