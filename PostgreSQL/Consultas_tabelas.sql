select * from tipos_produto;

select p.codigo as Codigo, p.descricao as Descricao, p.preco as Preco, tp.descricao as Tipo
	from produtos As p, tipos_produto AS tp
	WHERE p.codigo_tipo = tp.codigo;