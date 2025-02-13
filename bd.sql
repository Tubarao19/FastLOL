-- llenado de bd / create - post
INSERT INTO "CHAMPIONS" ("CHAMPS_NAME", "CHAMPS_HEALTH", "CHAMPS_AD", "CHAMPS_AP", "CHAMPS_MP", 
"CHAMPS_MANA")
VALUES 
('Ekko', 665, 58, 9, 340, 280),
('Kennen', 590, 48, 9, 523, 200),
('Vex', 600, 54, 9, 523, 490),
('Katarina', 682, 58, 9, 523, 0),
('Fiddletsticks', 660, 55, 9, 523, 500);


INSERT INTO "SKILLS" ("SKILL_NAME", "SKILL_MANA_COST", "CHAMPS_ID")
VALUES 
('rebobinador de tiempo', 50, 1),
('convergencia paralela', 30, 1),
('salto de fase', 40, 1),
('cronoruptura', 100, 1),
('shuriken trueno', 60, 2),
('tension electrica', 40, 2),
('impulso relampago', 80, 2),
('tempestad cercenante', 0, 2),
('descarga mistral', 45, 3),
('espacio personal', 75, 3),
('amenaza umbria', 70, 3),
('haz lo tuyo sombra', 100, 3),
('hoja rebotante', 11, 4),
('preparacion', 15, 4),
('shunpo', 12, 4),
('loto mortal', 70, 4),
('aterrorizar', 65, 5),
('extraccion abundante', 60, 5),
('cosechar', 40, 5),
('tormenta de cuervos', 100, 5);

CREATE TABLE "CHAMPIONS" (
  "CHAMPS_ID" SERIAL PRIMARY KEY,
  "CHAMPS_NAME" VARCHAR,
  "CHAMPS_HEALTH" INT,
  "CHAMPS_AD" INT,
  "CHAMPS_AP" INT,
  "CHAMPS_MP" INT,
  "CHAMPS_MANA" INT
);

CREATE TABLE "SKILLS" (
  "SKILL_ID" SERIAL PRIMARY KEY,
  "SKILL_NAME" VARCHAR,
  "SKILL_MANA_COST" INT,
  "CHAMPS_ID" INT NOT NULL,
  CONSTRAINT "CHAMPS_FK" FOREIGN KEY ("CHAMPS_ID") REFERENCES "CHAMPIONS"("CHAMPS_ID")
  ON DELETE CASCADE 
  ON UPDATE CASCADE
);
--no agregar datos a los id cuando son autoincrementables o desincronizan las tablas

-- insert into - values / create - post

-- select / read - get

-- alter / update - put

-- delete



