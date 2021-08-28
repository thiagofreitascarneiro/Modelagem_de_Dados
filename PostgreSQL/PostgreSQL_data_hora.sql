-- data atual 
select current_date as Data_atual;

-- Hora atual 
select current_time as Hora_atual;

-- Calcular data futura
select current_date + interval '13 day' as Data_vencimento;

--Data passada
select current_date - interval '13 day' as Data_antiga;

-- Diferença entre datas

select date_part('year', '2021-01-01'::date) - date_part('year', '2018-10-02'::date) as em_anos;

-- extraindo o mes corrente 
select extract(month from current_timestamp) as Numero_do_mes;


