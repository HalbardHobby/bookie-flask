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

INSERT INTO book(id, name, author, year, summary) VALUES
(
    '9bf3f41c-0d3c-4b88-943f-8c7b8c653cff',
    'Cosmos: A Personal Voyage',
    'Carl Sagan',
    1980,
    'Cosmos is one of the bestselling science books of all time.'
),
(
    'fbb3eb9c-928f-4bbe-9dd1-da51c5043fd0',
    'Star Wars: Heir to the Empire',
    'Timothy Zahn',
    1991,
    'Heir to the Empire follows the adventures of Luke Skywalker, Han Solo, and Princess Leia after they led the Rebel Alliance to victory in Star Wars: Episode VI Return of the Jedi.'
),
(
    '6a6db5d3-9d33-4361-8128-e0fc3b2d523e',
    'How to Be Miserable: 40 Strategies You Already Use',
    'Randy J. Paterson PhD',
    2016,
    'In How to Be Miserable, psychologist Randy Paterson outlines 40 specific behaviors and habits which - if followed - are sure to lead to a lifetime of unhappiness. On the other hand, if you do the opposite, you may yet join the ranks of happy people everywhere!'
);
