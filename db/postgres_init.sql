CREATE TABLE book
(
    id uuid NOT NULL,
    name text NOT NULL,
    author text NOT NULL,
    isbn varchar (20),
    year integer,
    summary text,
    CONSTRAINT book_pkey PRIMARY KEY (id)
);

INSERT INTO book(id, name, author, isbn, year, summary) VALUES
 (
    '9bf3f41c-0d3c-4b88-943f-8c7b8c653cff',
    'asd',
    'asd',
    '978-3-598-21500-1',
    1999,
    'asdasdasd'
 );
