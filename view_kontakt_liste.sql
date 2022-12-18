CREATE or replace VIEW `view_kontakt_liste` AS
    SELECT 
        k.id_kontakt as id_kontakt, a.anrede as anrede, concat(p.vorname," ",p.nachname) as Name,
	k.plz as plz, concat(k.strasse, " ", k.hausnr) as strasse, k.ort as ort, k. email, k.telefon as telefon, k.mobil as mobil
    FROM
        person p,
        anrede a,
        kontakt k
    WHERE
        (p.id_anrede = a.id_anrede) and
	(k.id_person = p.id_person)
