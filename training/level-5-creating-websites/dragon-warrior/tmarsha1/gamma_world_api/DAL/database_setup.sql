DROP TABLE if EXISTS tech_level;
DROP TABLE if EXISTS equipment;
DROP VIEW if EXISTS equipment_view;

create table tech_level (
  id INTEGER PRIMARY KEY,
  short_description text not null,
  long_description text
);

create table equipment (
  id integer primary key autoincrement,
  name text not null,
  complexity text not null,
  tech_level_fk INTEGER not null,
  price REAL not null,
  weight REAL NOT NULL,
  value REAL not null,
  FOREIGN KEY(tech_level_fk) REFERENCES tech_level(id)
);

CREATE VIEW equipment_view AS
  SELECT
    equipment.id,
    equipment.name,
    equipment.complexity,
    tech_level.short_description AS tech_level,
    equipment.price,
    equipment.weight,
    equipment.value
  FROM equipment
  INNER JOIN tech_level
  ON equipment.tech_level_fk=tech_level.id;

INSERT INTO tech_level (id, short_description)
VALUES  (1, 'I');

INSERT INTO tech_level (id, short_description)
VALUES  (2, 'II');

INSERT INTO tech_level (id, short_description)
VALUES  (3, 'III');

INSERT INTO equipment(name, complexity, tech_level_fk, price, weight, value)
VALUES ('Accelra Dose', 'E', 2, 100, .1, 100);

COMMIT;