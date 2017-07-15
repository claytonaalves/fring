CREATE TABLE cidade (
    id_cidade INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    uf TEXT NOT NULL
);

CREATE TABLE categoria (
    id_categoria INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_cidade INTEGER,
    descricao TEXT NOT NULL,
    imagem TEXT
);

CREATE TABLE anunciante (
    guid_anunciante TEXT NOT NULL PRIMARY KEY, 
    id_categoria INTEGER NOT NULL,
    razao_social TEXT,
    nome_fantasia TEXT,
    telefone TEXT,
    celular TEXT,
    email TEXT,
    logradouro TEXT,
    numero TEXT,
    cidade text, 
    bairro text, 
    uf text,
    data_cadastro INTEGER NOT NULL DEFAULT (strftime('%s', 'now', 'localtime')),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) 
);

CREATE TABLE publicacao ( 
   guid_publicacao TEXT    NOT NULL PRIMARY KEY,
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

