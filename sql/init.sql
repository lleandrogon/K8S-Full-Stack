CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

INSERT INTO produtos (
    nome,
    preco
) VALUES
    ('Notebook', 3500.00),
    ('Mouse', 100.00),
    ('Teclado', 250.00);