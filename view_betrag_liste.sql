CREATE or replace VIEW `view_betrag_liste` AS
    SELECT 
        b.id_betrag as id_betrag 
        ,b.e_a as EA 
	,a.anrede as anrede 
	,concat(p.vorname," ",p.nachname) as Name
        ,b.betrag_total as betrag
	,b.datum as datum
	,b.bemerkung as bemerkung
	,z.zname as zname
	,q.qname as qname
	,z.id_zahlung as z_id
	,q.id_quelle as q_id
    FROM
        person p
       ,anrede a
       ,betrag b
       ,quelle q
       ,zahlung z
    WHERE
        p.id_anrede = a.id_anrede and
        b.id_person = p.id_person and
        b.id_quelle = q.id_quelle and
        b.id_zahlung = z.id_zahlung
