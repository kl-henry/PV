CREATE or replace VIEW `view_person_liste` AS
    SELECT 
        p.id_person as id_person, a.anrede as anrede, concat(p.vorname," ",p.nachname) as Name
    FROM
        person p,
        anrede a
    WHERE
        p.id_anrede = a.id_anrede
