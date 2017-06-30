CREATE TABLE categoria (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    qtde_anunciantes INTEGER,
    imagem TEXT
);
CREATE TABLE anunciante (
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    razao_social TEXT,
    nome_fantasia TEXT,
    logradouro TEXT,
    numero TEXT,
    telefone TEXT,
    celular TEXT,
    email TEXT,
    id_categoria INTEGER, guid TEXT, bairro text, cidade text, uf text,
    FOREIGN KEY (id_categoria) REFERENCES categoria(_id) 
);

CREATE TABLE publicacao ( 
   guid            TEXT    NOT NULL PRIMARY KEY,
   guid_anunciante TEXT    NOT NULL,
   id_categoria    INTEGER NOT NULL,
   titulo          TEXT    NOT NULL,
   descricao       TEXT,
   data_publicacao INTEGER NOT NULL,
   data_validade   INTEGER NOT NULL,
   imagem          TEXT,
   publicado       INTEGER, -- Publicado no Firebase
   FOREIGN KEY (guid_anunciante) REFERENCES anunciante(guid),
   FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

