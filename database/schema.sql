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
CREATE TABLE anuncio ( 
    _id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    titulo TEXT, 
    descricao TEXT, 
    valido_ate TEXT, 
    imagem TEXT, 
    id_categoria INTEGER, 
    publicado INTEGER, 
    id_anunciante integer, 
    guid_anunciante text, 
    guid TEXT
);
