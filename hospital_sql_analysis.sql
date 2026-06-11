-- ============================================
-- HOSPITAL DATABASE ANALYSIS
-- SQL Portfolio Project — Mihaela Tepes
-- github.com/mihaelaadela-eng
-- ============================================

-- SETUP: Create Tables
CREATE TABLE IF NOT EXISTS spital_pacienti (
    id INTEGER PRIMARY KEY,
    nume TEXT,
    varsta INTEGER,
    gen TEXT,
    diagnostic TEXT,
    tensiune INTEGER,
    colesterol INTEGER,
    zile_internare INTEGER,
    id_sectie INTEGER,
    readmis TEXT
);

INSERT INTO spital_pacienti VALUES 
(1, 'Ana Ionescu', 67, 'F', 'hipertensiune', 145, 230, 3, 1, 'Nu'),
(2, 'Ion Pop', 45, 'M', 'diabet', 120, 180, 5, 2, 'Nu'),
(3, 'Maria Rus', 72, 'F', 'hipertensiune', 160, 260, 7, 1, 'Da'),
(4, 'Petre Dima', 38, 'M', 'anxietate', 118, 155, 2, 3, 'Nu'),
(5, 'Elena Stoica', 55, 'F', 'hipertensiune', 155, 240, 4, 1, 'Da'),
(6, 'Gheorghe Marin', 81, 'M', 'diabet', 122, 190, 10, 2, 'Nu'),
(7, 'Ioana Vlad', 63, 'F', 'hipertensiune', 148, 220, 6, 1, 'Da'),
(8, 'Mihai Constantin', 49, 'M', 'diabet', 119, 175, 3, 2, 'Nu'),
(9, 'Rodica Popa', 70, 'F', 'hipertensiune', 165, 255, 8, 1, 'Da'),
(10, 'Vasile Dumitrescu', 58, 'M', 'diabet', 125, 200, 4, 2, 'Nu');

CREATE TABLE IF NOT EXISTS spital_sectii (
    id_sectie INTEGER PRIMARY KEY,
    nume_sectie TEXT,
    cost_zi INTEGER,
    nr_paturi INTEGER
);

INSERT INTO spital_sectii VALUES 
(1, 'Cardiologie', 300, 20),
(2, 'Diabet', 250, 15),
(3, 'Psihiatrie', 200, 10);

-- ============================================
-- RAPORT 1: Statistici generale
-- ============================================
SELECT 
    COUNT(*) as total_pacienti,
    ROUND(AVG(varsta), 1) as varsta_medie,
    ROUND(AVG(tensiune), 1) as tensiune_medie,
    SUM(CASE WHEN readmis = 'Da' THEN 1 ELSE 0 END) as total_readmisi
FROM spital_pacienti;

-- ============================================
-- RAPORT 2: Costuri per sectie
-- ============================================
SELECT 
    s.nume_sectie,
    COUNT(p.id) as nr_pacienti,
    ROUND(AVG(p.zile_internare), 1) as zile_medii,
    SUM(p.zile_internare * s.cost_zi) as cost_total,
    ROUND(AVG(p.zile_internare * s.cost_zi), 0) as cost_mediu_pacient
FROM spital_pacienti p
JOIN spital_sectii s ON p.id_sectie = s.id_sectie
GROUP BY s.nume_sectie
ORDER BY cost_total DESC;

-- ============================================
-- RAPORT 3: Analiza readmisiilor
-- ============================================
SELECT 
    s.nume_sectie,
    COUNT(*) as total_pacienti,
    SUM(CASE WHEN p.readmis = 'Da' THEN 1 ELSE 0 END) as nr_readmisi,
    ROUND(AVG(CASE WHEN p.readmis = 'Da' THEN 1.0 ELSE 0 END) * 100, 1) as procent_readmisi,
    ROUND(AVG(CASE WHEN p.readmis = 'Da' THEN p.varsta END), 1) as varsta_medie_readmisi
FROM spital_pacienti p
JOIN spital_sectii s ON p.id_sectie = s.id_sectie
GROUP BY s.nume_sectie
ORDER BY procent_readmisi DESC;

-- ============================================
-- RAPORT 4: Pacienti risc inalt
-- ============================================
SELECT 
    p.nume,
    p.varsta,
    p.tensiune,
    p.colesterol,
    s.nume_sectie,
    p.zile_internare,
    p.readmis,
    CASE 
        WHEN p.varsta > 65 AND p.tensiune > 150 THEN 'Risc Inalt'
        WHEN p.varsta > 55 OR p.tensiune > 140 THEN 'Risc Mediu'
        ELSE 'Risc Scazut'
    END as categorie_risc
FROM spital_pacienti p
JOIN spital_sectii s ON p.id_sectie = s.id_sectie
ORDER BY p.tensiune DESC;