CREATE or replace VIEW `view_pos_liste` AS
    SELECT 
        p.id_pos as id_pos 
        ,b.id_betrag as id_betrag 
        ,a.aname as art
        ,p.pos_betrag as betrag
	,p.bemerkung as bemerkung
    FROM
       betrag b
       ,position p
       ,art a
    WHERE
        p.id_betrag = b.id_betrag and
        a.id_art = p.id_art
