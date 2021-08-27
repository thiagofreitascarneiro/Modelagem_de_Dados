CREATE TABLE tipos_produto(
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(50) NOT NULL
	
);

CREATE TABLE PRODUTOS(
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(50) NOT NULL,
	preco MONEY NOT NULL,
	codigo_tipo INT REFERENCES tipos_produto(codigo) NOT NULL
);

INSERT INTO tipos_produto (descricao) VALUES ('Computador');
INSERT INTO tipos_produto (descricao) VALUES ('Impressora');


INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('desktop', 1200, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Notebook', 1800, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('imp Laser', 300, 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Imp Jato tinta', 500, 2);


select * from tipos_produto where codigo = 1;

select * from tipos_produto where codigo = 2;

select * from produtos;

select * from produtos where preco <= 'R$1000';





