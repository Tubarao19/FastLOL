-- llenado de bd
INSERT INTO "CHAMPIONS" ("CHAMPS_ID", "CHAMPS_NAME", "CHAMPS_HEALTH", "CHAMPS_AD", "CHAMPS_AP", "CHAMPS_MP", "CHAMPS_MANA")
VALUES 
(3, 'Vex', 600, 54, 9, 523, 490),
(4, 'Katarina', 682, 58, 9, 523, 0),
(5, 'Fiddletsticks', 660, 55, 9, 523, 500);

INSERT INTO "SKILLS" ("SKILL_ID", "SKILL_NAME", "SKILL_MANA_COST", "CHAMPS_ID")
VALUES 
(1, 'rebobinador de tiempo', 50, 1),
(2, 'convergencia paralela', 30, 1),
(3, 'salto de fase', 40, 1),
(4, 'cronoruptura', 100, 1),
(5, 'shuriken trueno', 60, 2),
(6, 'tension electrica', 40, 2),
(7, 'impulso relampago', 80, 2),
(8, 'tempestad cercenante', 0, 2),
(9, 'descarga mistral', 45, 3),
(10, 'espacio personal', 75, 3),
(11, 'amenaza umbria', 70, 3),
(12, 'haz lo tuyo sombra', 100, 3),
(13, 'hoja rebotante', 11, 4),
(14, 'preparacion', 15, 4),
(15, 'shunpo', 12, 4),
(16, 'loto mortal', 70, 4),
(17, 'aterrorizar', 65, 5),
(18, 'extraccion abundante', 60, 5),
(19, 'cosechar', 40, 5),
(20, 'tormenta de cuervos', 100, 5);