# LeagueProject
 League Of Legends - Champions Stats


-- create
CREATE TABLE CHAMPIONS (
  id text PRIMARY KEY,
  name text,
  role text,
  damage text
);

-- insert
INSERT INTO CHAMPIONS(id,name,role,damage) VALUES ('champion001', 'Aatrox', 'Toplaner', 'AD');
INSERT INTO CHAMPIONS(id,name,role,damage) VALUES ('champion002', 'Ahri', 'Midlaner', 'AP');
INSERT INTO CHAMPIONS(id,name,role,damage) VALUES ('champion003', 'Akali', 'Midlaner', 'AP');

-- fetch 
SELECT * FROM CHAMPIONS;

INSERT INTO CHAMPIONS JSON '{
    "id": "champion004",
    "name": "Akshan",
    "role": "Midlaner",
    "damage": "AD"
}';

CREATE TYPE champion (id text, name text, role text, damage text);

CREATE table player(playerId text, playerName text, playerRank text, playerPoolchamp frozen<champion>, primary key(id));

INSERT INTO player JSON '{
    "playerId": "player001",
    "playerName": "PLAYER001",
    "playerRank" "SILVER 3",
    "playerPoolchamp": {
        "id": "champion005",
        "name": "Alistar",
        "role": "Support",
        "damage": "AP"
    }
}';
