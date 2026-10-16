import sqlite3

conn = sqlite3.connect("mercadillo.db")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE IF NOT EXISTS items (
    id        INTEGER PRIMARY KEY,
    nombre    TEXT NOT NULL,
    nivel     INTEGER,
    tipo      TEXT
);

CREATE TABLE IF NOT EXISTS recetas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id     INTEGER NOT NULL REFERENCES items(id),
    ingrediente_id  INTEGER NOT NULL REFERENCES items(id),
    cantidad        INTEGER NOT NULL,
    oficio          TEXT,
    UNIQUE (producto_id, ingrediente_id)
);

CREATE TABLE IF NOT EXISTS recolecta (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id         INTEGER NOT NULL REFERENCES items(id),
    oficio          TEXT NOT NULL,
    nivel_minimo    INTEGER,
    UNIQUE (item_id, oficio)
);

CREATE TABLE IF NOT EXISTS drops (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    monstruo      TEXT NOT NULL,
    item_id       INTEGER NOT NULL REFERENCES items(id),
    probabilidad  REAL,
    UNIQUE (monstruo, item_id)
);

CREATE TABLE IF NOT EXISTS cotizaciones (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id   INTEGER NOT NULL REFERENCES items(id),
    fecha     TEXT NOT NULL,
    periodo   TEXT NOT NULL,   -- '24h', '7d' o '30d'
    mediana   INTEGER,
    media     INTEGER,
    vendidos  INTEGER
);

CREATE TABLE IF NOT EXISTS precios_compra (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id    INTEGER NOT NULL REFERENCES items(id),
    fecha      TEXT NOT NULL,
    lote       INTEGER NOT NULL,   -- 1, 10, 100...
    precio     INTEGER NOT NULL
);
""")

conn.commit()

# Comprobación: listar las tablas creadas
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
print("Tablas creadas:")
for fila in cur.fetchall():
    print(" -", fila[0])

conn.close()