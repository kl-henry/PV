CREATE or replace VIEW `view_liste_positionen` AS
select  b.datum as datum, b.betrag_total, z.zname as z, p.bemerkung
      ,p.pos_betrag, a.aname as produkt, extract(year from b.datum) as Year, extract(month from b.datum) as Month
from betrag as b,
zahlung as z,
position as p,
art as a
where b.id_zahlung = z.id_zahlung
and   b.id_betrag = p.id_betrag
and   a.id_art = p.id_art
order by datum
