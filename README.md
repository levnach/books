# Translated Audiobooks

Books that (1) have an **audiobook** edition, (2) have an **English** edition, and (3) are translated into **at least 3 languages** — grouped by genre and ranked by an invented popularity counter.

**Interactive site:** https://levnach.github.io/books/ (filter, search, sort, tune the score weight)

## The score — Translation Popularity Index (TPI)

```
TPI = L + 25 × Σ log2(k)
```

* **L** — number of languages the book is translated into.
* **k** — number of distinct translations into the same language (summed over every language with k ≥ 2).

Multiple translations into the same language count very high: every *doubling* of translations in one language is worth 25 extra languages. Two English translations add 25; four add 50; eight add 75.

> Counts are curated, rounded estimates (from publishers, Index Translationum, Wikipedia and translation bibliographies). They are meant for ranking, not as exact bibliographic data. Corrections are welcome — edit `data/books.json` and run `python build.py`.

## Top 20 overall

| # | Book | Author | Genre | Languages | Retranslations | TPI |
|---|------|--------|-------|----------:|----------------|----:|
| 1 | The Bible | Various | Religion & Spirituality | 736 | English ×100, German ×30, French ×30, Spanish ×20, Russian ×10 | **1339** |
| 2 | The Little Prince | Antoine de Saint-Exupéry | Children's | 505 | English ×10, Italian ×8, German ×6, Russian ×6, Spanish ×5 | **850** |
| 3 | Tao Te Ching | Laozi | Philosophy | 250 | English ×100, German ×20, French ×15, Russian ×10, Spanish ×10 | **788** |
| 4 | Alice's Adventures in Wonderland | Lewis Carroll | Children's | 174 | Russian ×13, Japanese ×10, French ×8, German ×8, Hebrew ×4 | **550** |
| 5 | The Quran | — | Religion & Spirituality | 110 | English ×60, German ×15, French ×10, Russian ×8 | **513** |
| 6 | The Odyssey | Homer | Poetry & Epic | 60 | English ×60, German ×10, French ×8, Italian ×6, Russian ×3 | **470** |
| 7 | Don Quixote | Miguel de Cervantes | Classic Literature | 140 | English ×20, French ×10, German ×8, Russian ×4 | **456** |
| 8 | Bhagavad Gita | Vyasa (attr.) | Religion & Spirituality | 80 | English ×100, German ×10, French ×6, Russian ×5 | **452** |
| 9 | The Adventures of Pinocchio | Carlo Collodi | Children's | 260 | English ×15, German ×6, Russian ×2 | **447** |
| 10 | The Divine Comedy | Dante Alighieri | Poetry & Epic | 60 | English ×50, German ×15, French ×15, Russian ×4 | **446** |
| 11 | The Iliad | Homer | Poetry & Epic | 60 | English ×50, German ×8, French ×6, Russian ×4 | **391** |
| 12 | Grimms' Fairy Tales | Brothers Grimm | Children's | 160 | English ×20, French ×6, Russian ×4 | **383** |
| 13 | Hamlet | William Shakespeare | Drama | 80 | German ×20, French ×15, Russian ×10 | **369** |
| 14 | The Raven | Edgar Allan Poe | Poetry & Epic | 40 | Russian ×30, German ×10, Spanish ×8, French ×3 | **360** |
| 15 | Rubáiyát of Omar Khayyám | Omar Khayyám | Poetry & Epic | 80 | English ×30, Russian ×10, German ×6 | **350** |
| 16 | Andersen's Fairy Tales | Hans Christian Andersen | Children's | 125 | English ×20, German ×6, Russian ×4 | **348** |
| 17 | The Imitation of Christ | Thomas à Kempis | Religion & Spirituality | 90 | English ×15, French ×10, German ×8 | **346** |
| 18 | Romeo and Juliet | William Shakespeare | Drama | 80 | German ×12, French ×10, Russian ×8 | **328** |
| 19 | Faust | Johann Wolfgang von Goethe | Drama | 60 | English ×40, French ×6, Russian ×5 | **316** |
| 20 | The Metamorphosis | Franz Kafka | Modern Literary Fiction | 100 | English ×20, French ×6, Russian ×3 | **312** |

## By genre

* [Religion & Spirituality](#religion--spirituality) (7)
* [Children's](#childrens) (13)
* [Philosophy](#philosophy) (8)
* [Poetry & Epic](#poetry--epic) (11)
* [Classic Literature](#classic-literature) (14)
* [Drama](#drama) (8)
* [Modern Literary Fiction](#modern-literary-fiction) (14)
* [Adventure](#adventure) (8)
* [History & Non-fiction](#history--non-fiction) (9)
* [Dystopian](#dystopian) (6)
* [Mystery & Thriller](#mystery--thriller) (7)
* [Romance](#romance) (6)
* [Fantasy](#fantasy) (9)
* [Horror & Gothic](#horror--gothic) (5)
* [Science Fiction](#science-fiction) (10)
* [Self-help](#self-help) (5)

### Religion & Spirituality

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 1 | The Bible | Various | 500 BC | Hebrew / Greek | 736 | English ×100, German ×30, French ×30, Spanish ×20, Russian ×10 | **1339** |
| 5 | The Quran | — | 632 | Arabic | 110 | English ×60, German ×15, French ×10, Russian ×8 | **513** |
| 8 | Bhagavad Gita | Vyasa (attr.) | 200 BC | Sanskrit | 80 | English ×100, German ×10, French ×6, Russian ×5 | **452** |
| 17 | The Imitation of Christ | Thomas à Kempis | 1427 | Latin | 90 | English ×15, French ×10, German ×8 | **346** |
| 29 | The Dhammapada | Buddhist canon | 250 BC | Pali | 50 | English ×30, German ×6, French ×4 | **287** |
| 31 | The Pilgrim's Progress | John Bunyan | 1678 | English | 200 | French ×3, German ×3 | **279** |
| 35 | The Prophet | Kahlil Gibran | 1923 | English | 110 | Arabic ×8, French ×4, Russian ×3 | **275** |

### Children's

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 2 | The Little Prince | Antoine de Saint-Exupéry | 1943 | French | 505 | English ×10, Italian ×8, German ×6, Russian ×6, Spanish ×5 | **850** |
| 4 | Alice's Adventures in Wonderland | Lewis Carroll | 1865 | English | 174 | Russian ×13, Japanese ×10, French ×8, German ×8, Hebrew ×4 | **550** |
| 9 | The Adventures of Pinocchio | Carlo Collodi | 1883 | Italian | 260 | English ×15, German ×6, Russian ×2 | **447** |
| 12 | Grimms' Fairy Tales | Brothers Grimm | 1812 | German | 160 | English ×20, French ×6, Russian ×4 | **383** |
| 16 | Andersen's Fairy Tales | Hans Christian Andersen | 1835 | Danish | 125 | English ×20, German ×6, Russian ×4 | **348** |
| 63 | Pippi Longstocking | Astrid Lindgren | 1945 | Swedish | 77 | English ×3, Russian ×2, German ×2 | **167** |
| 69 | The Adventures of Tom Sawyer | Mark Twain | 1876 | English | 50 | Russian ×5, German ×4 | **158** |
| 76 | Heidi | Johanna Spyri | 1881 | German | 50 | English ×13 | **143** |
| 77 | Winnie-the-Pooh | A. A. Milne | 1926 | English | 50 | Russian ×3, German ×2, Hebrew ×2 | **140** |
| 84 | Charlie and the Chocolate Factory | Roald Dahl | 1964 | English | 55 | Russian ×3, German ×2 | **120** |
| 93 | The Jungle Book | Rudyard Kipling | 1894 | English | 40 | Russian ×3, French ×2 | **105** |
| 95 | The Wonderful Adventures of Nils | Selma Lagerlöf | 1906 | Swedish | 60 | English ×3 | **100** |
| 104 | Peter Pan | J. M. Barrie | 1911 | English | 40 | Russian ×3 | **80** |

### Philosophy

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 3 | Tao Te Ching | Laozi | 400 BC | Classical Chinese | 250 | English ×100, German ×20, French ×15, Russian ×10, Spanish ×10 | **788** |
| 24 | The Prince | Niccolò Machiavelli | 1532 | Italian | 60 | English ×25, French ×6, German ×5 | **299** |
| 33 | The Republic | Plato | 375 BC | Ancient Greek | 50 | English ×15, German ×6, French ×6 | **277** |
| 36 | The Art of War | Sun Tzu | 500 BC | Classical Chinese | 40 | English ×30, French ×5, Russian ×4 | **271** |
| 37 | Meditations | Marcus Aurelius | 180 | Ancient Greek | 40 | English ×15, French ×6, German ×5 | **260** |
| 40 | The Analects | Confucius | 475 BC | Classical Chinese | 40 | English ×20, German ×4, French ×4 | **248** |
| 42 | Thus Spoke Zarathustra | Friedrich Nietzsche | 1883 | German | 60 | English ×8, French ×5, Russian ×3 | **233** |
| 119 | Sophie's World | Jostein Gaarder | 1991 | Norwegian | 60 | — | **60** |

### Poetry & Epic

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 6 | The Odyssey | Homer | 700 BC | Ancient Greek | 60 | English ×60, German ×10, French ×8, Italian ×6, Russian ×3 | **470** |
| 10 | The Divine Comedy | Dante Alighieri | 1320 | Italian | 60 | English ×50, German ×15, French ×15, Russian ×4 | **446** |
| 11 | The Iliad | Homer | 750 BC | Ancient Greek | 60 | English ×50, German ×8, French ×6, Russian ×4 | **391** |
| 14 | The Raven | Edgar Allan Poe | 1845 | English | 40 | Russian ×30, German ×10, Spanish ×8, French ×3 | **360** |
| 15 | Rubáiyát of Omar Khayyám | Omar Khayyám | 1120 | Persian | 80 | English ×30, Russian ×10, German ×6 | **350** |
| 26 | Eugene Onegin | Alexander Pushkin | 1833 | Russian | 40 | English ×25, German ×10, French ×5 | **297** |
| 30 | The Aeneid | Virgil | 19 BC | Latin | 40 | English ×30, French ×6, German ×5 | **285** |
| 45 | Beowulf | Anonymous | 1000 | Old English | 35 | English (modern) ×40, German ×5 | **226** |
| 50 | The Epic of Gilgamesh | Anonymous | 1200 BC | Akkadian | 35 | English ×15, German ×4, Russian ×2 | **208** |
| 70 | Paradise Lost | John Milton | 1667 | English | 30 | French ×6, German ×5 | **153** |
| 90 | Leaves of Grass | Walt Whitman | 1855 | English | 30 | German ×3, French ×3 | **109** |

### Classic Literature

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 7 | Don Quixote | Miguel de Cervantes | 1605 | Spanish | 140 | English ×20, French ×10, German ×8, Russian ×4 | **456** |
| 22 | Crime and Punishment | Fyodor Dostoevsky | 1866 | Russian | 80 | English ×13, German ×7, French ×6 | **307** |
| 28 | Anna Karenina | Leo Tolstoy | 1878 | Russian | 60 | English ×12, German ×8, French ×6 | **289** |
| 32 | War and Peace | Leo Tolstoy | 1869 | Russian | 50 | English ×12, German ×8, French ×6 | **279** |
| 39 | The Brothers Karamazov | Fyodor Dostoevsky | 1880 | Russian | 60 | English ×8, German ×6, French ×5 | **258** |
| 43 | Madame Bovary | Gustave Flaubert | 1857 | French | 60 | English ×20, German ×6 | **233** |
| 52 | Moby-Dick | Herman Melville | 1851 | English | 30 | German ×6, Italian ×5, French ×4 | **203** |
| 56 | Les Misérables | Victor Hugo | 1862 | French | 60 | English ×8, German ×5 | **193** |
| 59 | Candide | Voltaire | 1759 | French | 50 | English ×10, German ×4 | **183** |
| 81 | Swann's Way (In Search of Lost Time) | Marcel Proust | 1913 | French | 40 | English ×4, German ×3 | **130** |
| 86 | Great Expectations | Charles Dickens | 1861 | English | 40 | French ×3, German ×3 | **119** |
| 88 | The Tale of Genji | Murasaki Shikibu | 1010 | Japanese | 30 | English ×5, French ×2 | **113** |
| 113 | Dream of the Red Chamber | Cao Xueqin | 1791 | Chinese | 25 | English ×3 | **65** |
| 114 | Romance of the Three Kingdoms | Luo Guanzhong | 1522 | Chinese | 25 | English ×3 | **65** |

### Drama

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 13 | Hamlet | William Shakespeare | 1603 | English | 80 | German ×20, French ×15, Russian ×10 | **369** |
| 18 | Romeo and Juliet | William Shakespeare | 1597 | English | 80 | German ×12, French ×10, Russian ×8 | **328** |
| 19 | Faust | Johann Wolfgang von Goethe | 1808 | German | 60 | English ×40, French ×6, Russian ×5 | **316** |
| 23 | Oedipus Rex | Sophocles | 429 BC | Ancient Greek | 40 | English ×30, German ×8, French ×6 | **302** |
| 27 | Macbeth | William Shakespeare | 1623 | English | 70 | German ×10, French ×8, Russian ×6 | **293** |
| 58 | The Cherry Orchard | Anton Chekhov | 1904 | Russian | 40 | English ×15, German ×4 | **188** |
| 61 | A Doll's House | Henrik Ibsen | 1879 | Norwegian | 50 | English ×10, German ×3 | **173** |
| 126 | Waiting for Godot | Samuel Beckett | 1953 | French | 50 | — | **50** |

### Modern Literary Fiction

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 20 | The Metamorphosis | Franz Kafka | 1915 | German | 100 | English ×20, French ×6, Russian ×3 | **312** |
| 38 | The Great Gatsby | F. Scott Fitzgerald | 1925 | English | 42 | German ×10, French ×7, Spanish ×6 | **260** |
| 62 | Ulysses | James Joyce | 1922 | English | 40 | Spanish ×3, Italian ×3, French ×2, German ×2 | **169** |
| 64 | The Trial | Franz Kafka | 1925 | German | 60 | English ×6, French ×3 | **164** |
| 66 | The Stranger | Albert Camus | 1942 | French | 70 | English ×4, German ×3 | **160** |
| 67 | The Master and Margarita | Mikhail Bulgakov | 1967 | Russian | 40 | English ×7, German ×4 | **160** |
| 75 | Siddhartha | Hermann Hesse | 1922 | German | 60 | English ×5, French ×2 | **143** |
| 83 | The Catcher in the Rye | J. D. Salinger | 1951 | English | 30 | German ×3, French ×2, Russian ×2 | **120** |
| 98 | Lolita | Vladimir Nabokov | 1955 | English | 40 | French ×2, German ×2 | **90** |
| 99 | To Kill a Mockingbird | Harper Lee | 1960 | English | 40 | French ×2, German ×2 | **90** |
| 100 | The Old Man and the Sea | Ernest Hemingway | 1952 | English | 40 | German ×2, French ×2 | **90** |
| 102 | The Alchemist | Paulo Coelho | 1988 | Portuguese | 88 | — | **88** |
| 103 | Norwegian Wood | Haruki Murakami | 1987 | Japanese | 36 | English ×2, Chinese ×2 | **86** |
| 130 | One Hundred Years of Solitude | Gabriel García Márquez | 1967 | Spanish | 46 | — | **46** |

### Adventure

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 21 | Robinson Crusoe | Daniel Defoe | 1719 | English | 100 | German ×10, French ×8, Russian ×4 | **308** |
| 46 | Gulliver's Travels | Jonathan Swift | 1726 | English | 50 | German ×6, French ×5, Russian ×4 | **223** |
| 49 | Treasure Island | Robert Louis Stevenson | 1883 | English | 60 | German ×5, Russian ×4, French ×4 | **218** |
| 71 | The Three Musketeers | Alexandre Dumas | 1844 | French | 50 | English ×8, Russian ×2 | **150** |
| 79 | Around the World in Eighty Days | Jules Verne | 1872 | French | 60 | English ×8 | **135** |
| 80 | The Count of Monte Cristo | Alexandre Dumas | 1844 | French | 50 | English ×5, Russian ×2 | **133** |
| 105 | Journey to the West | Wu Cheng'en | 1592 | Chinese | 30 | English ×4 | **80** |
| 108 | The Call of the Wild | Jack London | 1903 | English | 50 | Russian ×2 | **75** |

### History & Non-fiction

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 25 | The Communist Manifesto | Karl Marx & Friedrich Engels | 1848 | German | 200 | Russian ×5, English ×3 | **298** |
| 47 | The Histories | Herodotus | 430 BC | Ancient Greek | 30 | English ×12, German ×4, French ×4 | **220** |
| 72 | On the Origin of Species | Charles Darwin | 1859 | English | 30 | German ×3, French ×3, Russian ×3 | **149** |
| 74 | The Wealth of Nations | Adam Smith | 1776 | English | 30 | German ×6, French ×4 | **145** |
| 85 | The Diary of a Young Girl | Anne Frank | 1947 | Dutch | 70 | English ×2, German ×2 | **120** |
| 118 | Sapiens | Yuval Noah Harari | 2011 | Hebrew | 65 | — | **65** |
| 124 | Night | Elie Wiesel | 1958 | French (from Yiddish) | 30 | English ×2 | **55** |
| 127 | Man's Search for Meaning | Viktor Frankl | 1946 | German | 50 | — | **50** |
| 136 | A Brief History of Time | Stephen Hawking | 1988 | English | 40 | — | **40** |

### Dystopian

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 34 | Nineteen Eighty-Four | George Orwell | 1949 | English | 65 | German ×6, Russian ×5, Spanish ×4, French ×3 | **277** |
| 44 | Animal Farm | George Orwell | 1945 | English | 70 | Russian ×5, German ×4, French ×4 | **228** |
| 94 | We | Yevgeny Zamyatin | 1924 | Russian | 30 | English ×7 | **100** |
| 97 | Brave New World | Aldous Huxley | 1932 | English | 30 | German ×3, Russian ×2 | **95** |
| 123 | Fahrenheit 451 | Ray Bradbury | 1953 | English | 33 | Russian ×2 | **58** |
| 135 | The Handmaid's Tale | Margaret Atwood | 1985 | English | 40 | — | **40** |

### Mystery & Thriller

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 41 | The Hound of the Baskervilles | Arthur Conan Doyle | 1902 | English | 70 | German ×6, Russian ×4, French ×4 | **235** |
| 78 | And Then There Were None | Agatha Christie | 1939 | English | 50 | Russian ×3, German ×2, French ×2 | **140** |
| 101 | Murder on the Orient Express | Agatha Christie | 1934 | English | 50 | Russian ×3 | **90** |
| 128 | Perfume | Patrick Süskind | 1985 | German | 49 | — | **49** |
| 129 | The Name of the Rose | Umberto Eco | 1980 | Italian | 47 | — | **47** |
| 132 | The Girl with the Dragon Tattoo | Stieg Larsson | 2005 | Swedish | 44 | — | **44** |
| 133 | The Da Vinci Code | Dan Brown | 2003 | English | 44 | — | **44** |

### Romance

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 48 | Pride and Prejudice | Jane Austen | 1813 | English | 40 | French ×8, German ×6, Russian ×3 | **219** |
| 54 | Jane Eyre | Charlotte Brontë | 1847 | English | 57 | French ×8, German ×6 | **197** |
| 73 | Wuthering Heights | Emily Brontë | 1847 | English | 40 | French ×5, German ×4 | **148** |
| 91 | Gone with the Wind | Margaret Mitchell | 1936 | English | 40 | Russian ×3, German ×2 | **105** |
| 107 | Sense and Sensibility | Jane Austen | 1811 | English | 35 | French ×3 | **75** |
| 115 | Doctor Zhivago | Boris Pasternak | 1957 | Russian | 40 | English ×2 | **65** |

### Fantasy

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 51 | The Hobbit | J. R. R. Tolkien | 1937 | English | 60 | Russian ×5, German ×3, French ×2, Swedish ×2 | **208** |
| 60 | The Lord of the Rings | J. R. R. Tolkien | 1954 | English | 38 | Russian ×7, German ×2, French ×2, Swedish ×2 | **183** |
| 68 | Harry Potter and the Philosopher's Stone | J. K. Rowling | 1997 | English | 85 | Russian ×2, Chinese ×2, Portuguese ×2 | **160** |
| 89 | The Lion, the Witch and the Wardrobe | C. S. Lewis | 1950 | English | 47 | Russian ×3, German ×2 | **112** |
| 109 | A Game of Thrones | George R. R. Martin | 1996 | English | 47 | German ×2 | **72** |
| 110 | A Wizard of Earthsea | Ursula K. Le Guin | 1968 | English | 30 | Russian ×3 | **70** |
| 131 | The Neverending Story | Michael Ende | 1979 | German | 45 | — | **45** |
| 138 | The Last Wish (The Witcher) | Andrzej Sapkowski | 1993 | Polish | 37 | — | **37** |
| 139 | The Colour of Magic | Terry Pratchett | 1983 | English | 37 | — | **37** |

### Horror & Gothic

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 53 | Frankenstein | Mary Shelley | 1818 | English | 50 | French ×5, German ×4, Russian ×3 | **198** |
| 55 | The Picture of Dorian Gray | Oscar Wilde | 1890 | English | 50 | German ×6, Russian ×3, French ×3 | **194** |
| 65 | Dracula | Bram Stoker | 1897 | English | 44 | Russian ×3, German ×3, French ×3 | **163** |
| 106 | Strange Case of Dr Jekyll and Mr Hyde | Robert Louis Stevenson | 1886 | English | 40 | Russian ×3 | **80** |
| 120 | The Shining | Stephen King | 1977 | English | 35 | Russian ×2 | **60** |

### Science Fiction

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 57 | Twenty Thousand Leagues Under the Seas | Jules Verne | 1870 | French | 70 | English ×10, Russian ×3 | **193** |
| 82 | Dune | Frank Herbert | 1965 | English | 25 | Russian ×4, German ×2, French ×2 | **125** |
| 87 | Solaris | Stanisław Lem | 1961 | Polish | 40 | English ×2, Russian ×2, German ×2 | **115** |
| 92 | The War of the Worlds | H. G. Wells | 1898 | English | 40 | Russian ×3, French ×2 | **105** |
| 96 | The Hitchhiker's Guide to the Galaxy | Douglas Adams | 1979 | English | 30 | Russian ×3, German ×2 | **95** |
| 111 | Roadside Picnic | Arkady & Boris Strugatsky | 1972 | Russian | 20 | English ×2, German ×2 | **70** |
| 112 | Foundation | Isaac Asimov | 1951 | English | 30 | Russian ×3 | **70** |
| 116 | The Time Machine | H. G. Wells | 1895 | English | 40 | Russian ×2 | **65** |
| 117 | Neuromancer | William Gibson | 1984 | English | 25 | Russian ×3 | **65** |
| 134 | The Three-Body Problem | Liu Cixin | 2008 | Chinese | 40 | — | **40** |

### Self-help

| # | Book | Author | Year | Original | Languages | Retranslations | TPI |
|---|------|--------|------|----------|----------:|----------------|----:|
| 121 | How to Win Friends and Influence People | Dale Carnegie | 1936 | English | 35 | Russian ×2 | **60** |
| 122 | Atomic Habits | James Clear | 2018 | English | 60 | — | **60** |
| 125 | Rich Dad Poor Dad | Robert Kiyosaki | 1997 | English | 51 | — | **51** |
| 137 | The 7 Habits of Highly Effective People | Stephen R. Covey | 1989 | English | 40 | — | **40** |
| 140 | The Power of Now | Eckhart Tolle | 1997 | English | 33 | — | **33** |

## Rebuild

```
python build.py
```
