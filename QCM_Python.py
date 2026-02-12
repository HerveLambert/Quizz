
import random

# Liste de 50 questions
questions = [
    {
        "question": "1. En Python, comment déclare-t-on une classe nommée `Voiture` avec un constructeur initialisant un attribut `marque` ?",
        "options": [
            "a) class Vociture(marque): pass",
            "b) class Voiture: def __init__(self, marque): self.marque = marque",
            "c) class Voiture: init(marque): self.marque = marque",
            "d) class Voiture: def __constructor__(marque): self.marque = marque"
        ],
        "answer": "b"
    },
    {
        "question": "2. En Pandas, comment afficher les 5 premières lignes d’un DataFrame `df` ?",
        "options": [
            "a) df.head(5)",
            "b) df.first(5)",
            "c) df.top(5)",
            "d) df.rows(5)"
        ],
        "answer": "a"
    },
    {
        "question": "3. Quelle est la sortie de `sorted([3, 1, 4, 1], reverse=True)` ?",
        "options": [
            "a) [1, 1, 3, 4]",
            "b) [4, 3, 1, 1]",
            "c) [1, 3, 1, 4]",
            "d) [4, 1, 3, 1]"
        ],
        "answer": "b"
    },
    {
        "question": "4. Quelle méthode permet de supprimer un attribut d’une instance d’une classe Python ?",
        "options": [
            "a) del self.attribut",
            "b) del instance.attribut",
            "c) self.remove(attribut)",
            "d) del(attribut)"
        ],
        "answer": "b"
    },
    {
        "question": "5. En Pandas, comment remplacer les valeurs NaN d'une colonne par la moyenne des valeurs existantes ?",
        "options": [
            "a) df['colonne'].fillna('mean')",
            "b) df['colonne'] = df['colonne'].replace('mean')",
            "c) df['colonne'] = df['colonne'].fillna(df['colonne'].mean())",
            "d) df['colonne'] = df['colonne'].mean()"
        ],
        "answer": "c"
    },
    {
        "question": "6. Quel est le rôle de la méthode spéciale `__str__()` dans une classe Python ?",
        "options": [
            "a) Permet de convertir l'objet en chaîne de caractères.",
            "b) Permet d'obtenir une représentation officielle de l'objet.",
            "c) Permet de modifier l'objet directement.",
            "d) Permet de créer une copie de l'objet."
        ],
        "answer": "a"
    },
    {
        "question": "7. En Python, que retourne la fonction `zip([1, 2], ['a', 'b'])` ?",
        "options": [
            "a) [(1, 'a'), (2, 'b')]",
            "b) [[1, 'a'], [2, 'b']]",
            "c) zip object",
            "d) None of the above"
        ],
        "answer": "c"
    },
    {
        "question": "8. Quelle est la sortie de cette expression : `[x**2 for x in range(5) if x % 2 == 0]` ?",
        "options": [
            "a) [0, 4, 16]",
            "b) [0, 1, 4, 9, 16]",
            "c) [0, 2, 4, 6]",
            "d) [1, 4, 16]"
        ],
        "answer": "a"
    },
    {
        "question": "9. Quelle fonction Python renvoie un objet itérable au lieu d'une liste ?",
        "options": [
            "a) map()",
            "b) range()",
            "c) filter()",
            "d) Toutes les réponses ci-dessus"
        ],
        "answer": "d"
    },
    {
        "question": "10. Que fait `@staticmethod` dans une classe Python ?",
        "options": [
            "a) Crée une méthode de classe qui ne dépend pas de l'instance.",
            "b) Crée une méthode qui modifie les attributs de classe.",
            "c) Permet d'accéder uniquement à `self`.",
            "d) Supprime une méthode existante."
        ],
        "answer": "a"
    },
    {
        "question": "11. En Pandas, que fait la méthode `.pivot()` sur un DataFrame ?",
        "options": [
            "a) Crée une vue plate du DataFrame.",
            "b) Réorganise les données en fonction de colonnes spécifiques.",
            "c) Regroupe les données en clusters.",
            "d) Trie les données par index."
        ],
        "answer": "b"
    },
    {
        "question": "12. Quelle est la sortie de : `bool([])` ?",
        "options": [
            "a) True",
            "b) False",
            "c) Erreur",
            "d) None"
        ],
        "answer": "b"
    },
    {
        "question": "13. Comment créer un index multi-niveau sur un DataFrame Pandas ?",
        "options": [
            "a) pd.MultiIndex.from_tuples()",
            "b) df.create_multi_index()",
            "c) df.multi_index()",
            "d) index.multi_level"
        ],
        "answer": "a"
    },
    {
        "question": "14. Quelle est la sortie de ce code ? `'{:.2f}'.format(3.14159)`",
        "options": [
            "a) '3.14'",
            "b) '3.14159'",
            "c) '3.141'",
            "d) '3.15'"
        ],
        "answer": "a"
    },
    {
        "question": "15. En Python, que fait l'instruction `assert` ?",
        "options": [
            "a) Exécute un bloc si la condition est fausse.",
            "b) Lève une exception si la condition est fausse.",
            "c) Ignore les erreurs dans le programme.",
            "d) Vérifie les erreurs syntaxiques."
        ],
        "answer": "b"
    },
    # Questions sur Pandas
    {
        "question": "16. Comment convertir une colonne d’un DataFrame Pandas en type datetime ?",
        "options": [
            "a) df['colonne'].astype('datetime')",
            "b) pandas.to_datetime(df['colonne'])",
            "c) df['colonne'].convert_to('datetime')",
            "d) df['colonne'].datetime()"
        ],
        "answer": "b"
    },
    {
        "question": "17. Que fait la méthode `df.iloc[2:5, 1:3]` en Pandas ?",
        "options": [
            "a) Sélectionne les lignes 2 à 5 et les colonnes 1 à 3 inclusivement.",
            "b) Sélectionne les lignes 2 à 5 et les colonnes 1 à 3 exclusives.",
            "c) Sélectionne uniquement la colonne 1 des lignes 2 à 5.",
            "d) Sélectionne les colonnes 2 à 5 inclusivement pour toutes les lignes."
        ],
        "answer": "b"
    },
    {
        "question": "18. Comment fusionner deux DataFrames Pandas `df1` et `df2` par une colonne `id` ?",
        "options": [
            "a) df1.concat(df2, on='id')",
            "b) df1.join(df2, on='id')",
            "c) pandas.merge(df1, df2, on='id')",
            "d) df1.merge(df2)"
        ],
        "answer": "c"
    },
    {
        "question": "19. Que fait `df.set_index('colonne')` en Pandas ?",
        "options": [
            "a) Ajoute une colonne d'index supplémentaire.",
            "b) Définit la colonne spécifiée comme index du DataFrame.",
            "c) Remplace la colonne existante par l’index.",
            "d) Trie les données par la colonne spécifiée."
        ],
        "answer": "b"
    },
    {
        "question": "20. Comment remplir les valeurs manquantes dans un DataFrame Pandas avec une valeur constante `0` ?",
        "options": [
            "a) df.replace(0)",
            "b) df.fillna(0)",
            "c) df.fill_missing(0)",
            "d) df.replace_missing(0)"
        ],
        "answer": "b"
    },
    {
        "question": "21. Que fait la méthode `df.groupby('colonne').sum()` en Pandas ?",
        "options": [
            "a) Trie le DataFrame par la colonne spécifiée.",
            "b) Crée un groupe basé sur une colonne et somme les valeurs des autres colonnes.",
            "c) Crée une nouvelle colonne appelée 'sum'.",
            "d) Retourne un DataFrame vide."
        ],
        "answer": "b"
    },
    {
        "question": "22. Quelle méthode Pandas permet de réinitialiser l'index d'un DataFrame ?",
        "options": [
            "a) df.reset()",
            "b) df.reindex()",
            "c) df.reset_index()",
            "d) df.reinitialize_index()"
        ],
        "answer": "c"
    },
    {
        "question": "23. Que fait `df.describe()` en Pandas ?",
        "options": [
            "a) Affiche des statistiques descriptives pour les colonnes numériques.",
            "b) Trie les données par ordre croissant.",
            "c) Filtre les colonnes de type chaîne.",
            "d) Renvoie un histogramme des valeurs."
        ],
        "answer": "a"
    },
    {
        "question": "24. Comment trier un DataFrame Pandas par une colonne en ordre décroissant ?",
        "options": [
            "a) df.sort_values(by='colonne', ascending=True)",
            "b) df.sort(by='colonne', reverse=True)",
            "c) df.sort_values(by='colonne', ascending=False)",
            "d) df.sort(by='colonne', descending=True)"
        ],
        "answer": "c"
    },
    {
        "question": "25. Quelle méthode Pandas est utilisée pour supprimer les lignes dupliquées dans un DataFrame ?",
        "options": [
            "a) df.drop_duplicates()",
            "b) df.remove_duplicates()",
            "c) df.clean_duplicates()",
            "d) df.delete_duplicates()"
        ],
        "answer": "a"
    },

    # Questions sur la programmation orientée objet
    {
        "question": "26. Quelle est la méthode spéciale utilisée pour initialiser un objet en Python ?",
        "options": [
            "a) __init__()",
            "b) __start__()",
            "c) __create__()",
            "d) __constructor__()"
        ],
        "answer": "a"
    },
    {
        "question": "27. En Python, quel décorateur est utilisé pour définir une méthode de classe ?",
        "options": [
            "a) @staticmethod",
            "b) @classmethod",
            "c) @class",
            "d) @staticmethod_class"
        ],
        "answer": "b"
    },
    {
        "question": "28. Quelle est la différence entre `is` et `==` ?",
        "options": [
            "a) `is` compare les valeurs et `==` compare les références.",
            "b) `is` compare les références et `==` compare les valeurs.",
            "c) Ils sont identiques en Python.",
            "d) `is` est utilisé uniquement pour les objets immuables."
        ],
        "answer": "b"
    },
    {
        "question": "29. Que fait le mot-clé `del` ?",
        "options": [
            "a) Supprime un objet.",
            "b) Désalloue la mémoire pour un objet.",
            "c) Supprime un élément d'une liste ou d'un dictionnaire.",
            "d) Toutes les réponses ci-dessus."
        ],
        "answer": "d"
    },
    {
        "question": "30. Quelle méthode est appelée pour obtenir une représentation lisible d’un objet ?",
        "options": [
            "a) __str__()",
            "b) __repr__()",
            "c) __call__()",
            "d) __print__()"
        ],
        "answer": "a"
    },
    {
        "question": "31. Que fait le mot-clé `super()` ?",
        "options": [
            "a) Appelle le constructeur d’une classe parente.",
            "b) Appelle une méthode de la classe parente.",
            "c) Accède à un attribut privé de la classe parente.",
            "d) a et b."
        ],
        "answer": "d"
    },
    {
        "question": "32. Quelle méthode est appelée lorsque vous utilisez `len(obj)` ?",
        "options": [
            "a) __size__()",
            "b) __length__()",
            "c) __len__()",
            "d) __count__()"
        ],
        "answer": "c"
    },
    {
        "question": "33. Que fait `@property` en Python ?",
        "options": [
            "a) Crée une méthode publique.",
            "b) Crée une méthode privée.",
            "c) Transforme une méthode en un attribut accessible en lecture seule.",
            "d) Définit une méthode statique."
        ],
        "answer": "c"
    },
    {
        "question": "34. Quelle méthode permet de comparer deux objets en Python ?",
        "options": [
            "a) __compare__()",
            "b) __eq__()",
            "c) __hash__()",
            "d) __cmp__()"
        ],
        "answer": "b"
    },
    {
        "question": "35. Quelle est la principale caractéristique de l'héritage multiple ?",
        "options": [
            "a) Une classe peut hériter de plusieurs classes parentes.",
            "b) Toutes les méthodes parentes sont automatiquement héritées.",
            "c) Une classe peut avoir plusieurs constructeurs.",
            "d) Les classes parentes doivent être abstraites."
        ],
        "answer": "a"
    }
]

extra_questions = [
    {
        "question": "31. Que renvoie la fonction `zip()` en Python ?",
        "options": [
            "a) Une liste contenant les paires des éléments des itérables donnés.",
            "b) Un dictionnaire associant les clés et valeurs des itérables donnés.",
            "c) Un objet zip qui est un itérateur de tuples.",
            "d) Une chaîne représentant les éléments zippés."
        ],
        "answer": "c"
    },
    {
        "question": "32. Que se passe-t-il si les itérables passés à `zip()` ont des longueurs différentes ?",
        "options": [
            "a) Une exception est levée.",
            "b) Les éléments manquants sont remplacés par `None`.",
            "c) Le résultat a la longueur du plus court itérable.",
            "d) Le résultat a la longueur du plus long itérable."
        ],
        "answer": "c"
    },
    {
        "question": "33. Quelle est la sortie de `list(zip([1, 2], ['a', 'b', 'c']))` ?",
        "options": [
            "a) [(1, 'a'), (2, 'b'), ('c',)]",
            "b) [(1, 'a'), (2, 'b')]",
            "c) [(1, 'a', 'c'), (2, 'b', 'c')]",
            "d) [(1, 'a', 'b', 'c')]"
        ],
        "answer": "b"
    },
    {
        "question": "34. Que fait l'opérateur `*` lorsqu'il est utilisé avec une liste comme `*my_list` ?",
        "options": [
            "a) Crée un nouvel itérable.",
            "b) Décompose la liste en ses éléments individuels.",
            "c) Copie la liste.",
            "d) Multiplie les éléments de la liste."
        ],
        "answer": "b"
    },
    {
        "question": "35. Quelle est la sortie de `a, *b, c = [1, 2, 3, 4]` ?",
        "options": [
            "a) a = 1, b = [2], c = 3",
            "b) a = 1, b = [2, 3], c = 4",
            "c) a = [1, 2], b = 3, c = 4",
            "d) a = 1, b = [3, 4], c = 2"
        ],
        "answer": "b"
    },
    {
        "question": "36. Quelle méthode permet d'obtenir uniquement les clés d'un dictionnaire en Python ?",
        "options": [
            "a) dict.keys()",
            "b) dict.items()",
            "c) dict.values()",
            "d) dict.get_keys()"
        ],
        "answer": "a"
    },
    {
        "question": "37. Quelle est la complexité temporelle moyenne pour rechercher une clé dans un dictionnaire ?",
        "options": [
            "a) O(1)",
            "b) O(log n)",
            "c) O(n)",
            "d) O(n log n)"
        ],
        "answer": "a"
    },
    {
        "question": "38. Quelle est la principale différence entre un tuple et une liste en Python ?",
        "options": [
            "a) Les tuples sont immuables, les listes sont mutables.",
            "b) Les listes sont immuables, les tuples sont mutables.",
            "c) Les tuples sont plus rapides à trier que les listes.",
            "d) Les tuples ne peuvent contenir que des types numériques."
        ],
        "answer": "a"
    },
    {
        "question": "39. Que fait la méthode `dict.update({key: value})` en Python ?",
        "options": [
            "a) Ajoute une nouvelle paire clé-valeur au dictionnaire sans écraser les anciennes.",
            "b) Écrase la clé existante avec la nouvelle valeur ou l'ajoute si elle n'existe pas.",
            "c) Remplace entièrement le dictionnaire par la mise à jour.",
            "d) Ne modifie rien si la clé existe déjà."
        ],
        "answer": "b"
    },
    {
        "question": "40. Quelle est la sortie de `tuple([1, 2, 3]) + (4, 5)` ?",
        "options": [
            "a) [1, 2, 3, 4, 5]",
            "b) (1, 2, 3, 4, 5)",
            "c) TypeError",
            "d) (4, 5, 1, 2, 3)"
        ],
        "answer": "b"
    }
]

extra_generator_iterator_questions = [
    {
        "question": "41. Quelle est la différence principale entre un générateur et une fonction normale ?",
        "options": [
            "a) Un générateur renvoie une liste complète, une fonction normale renvoie un seul élément.",
            "b) Un générateur utilise `yield` au lieu de `return` pour produire des valeurs paresseusement.",
            "c) Un générateur ne peut pas être réutilisé.",
            "d) Un générateur est plus lent qu'une fonction normale."
        ],
        "answer": "b"
    },
    {
        "question": "42. Que fait la méthode `next()` sur un itérateur en Python ?",
        "options": [
            "a) Retourne l'élément suivant ou lève une exception si l'itérateur est terminé.",
            "b) Ajoute un nouvel élément à l'itérateur.",
            "c) Réinitialise l'itérateur au début.",
            "d) Extrait le dernier élément de l'itérateur."
        ],
        "answer": "a"
    },
    {
        "question": "43. Que se passe-t-il lorsque l'itérateur est épuisé et qu'on appelle `next()` ?",
        "options": [
            "a) Retourne `None`.",
            "b) Redémarre l'itérateur.",
            "c) Lève une exception `StopIteration`.",
            "d) Lève une exception `ValueError`."
        ],
        "answer": "c"
    },
    {
        "question": "44. Comment transformer une fonction normale en générateur ?",
        "options": [
            "a) Remplacer `return` par `yield` dans la fonction.",
            "b) Ajouter un décorateur `@generator` à la fonction.",
            "c) Utiliser `def` au lieu de `generator`.",
            "d) Créer une fonction avec une boucle explicite."
        ],
        "answer": "a"
    },
    {
        "question": "45. Quelle est la sortie de : `gen = (x**2 for x in range(3)); print(list(gen))` ?",
        "options": [
            "a) [0, 1, 4]",
            "b) (0, 1, 4)",
            "c) [0, 1, 4, 9]",
            "d) Une erreur est levée."
        ],
        "answer": "a"
    },
    {
        "question": "46. Que fait la méthode spéciale `__iter__()` dans une classe en Python ?",
        "options": [
            "a) Elle initialise un itérateur.",
            "b) Elle rend un objet iterable.",
            "c) Elle termine l'itération.",
            "d) Elle transforme une liste en itérateur."
        ],
        "answer": "b"
    },
    {
        "question": "47. Quelle est la sortie de : `def gen(): yield 1; yield 2; print(next(gen()))` ?",
        "options": [
            "a) 1",
            "b) 2",
            "c) TypeError",
            "d) StopIteration"
        ],
        "answer": "c"
    },
    {
        "question": "48. Quelle méthode permet d'utiliser un générateur à l'infini sans lever une exception ?",
        "options": [
            "a) `cycle` du module `itertools`.",
            "b) `repeat` du module `itertools`.",
            "c) `yield` dans une boucle infinie.",
            "d) Toutes les réponses ci-dessus."
        ],
        "answer": "d"
    },
    {
        "question": "49. Quelle est la principale différence entre un itérateur et un iterable ?",
        "options": [
            "a) Un itérateur est épuisable, un iterable ne l'est pas.",
            "b) Un iterable est un objet contenant une méthode `__iter__`, un itérateur contient aussi `__next__`.",
            "c) Un iterable produit une liste et un itérateur produit un dictionnaire.",
            "d) Il n'y a aucune différence."
        ],
        "answer": "b"
    },
    {
        "question": "50. Quelle fonction permet de transformer un générateur en liste directement ?",
        "options": [
            "a) list()",
            "b) iter()",
            "c) tuple()",
            "d) generator()"
        ],
        "answer": "a"
    }
]

extra_context_decorator_questions = [
    {
        "question": "51. Quel mot-clé Python est utilisé pour définir un gestionnaire de contexte ?",
        "options": [
            "a) @context",
            "b) @contextmanager",
            "c) with",
            "d) open"
        ],
        "answer": "b"
    },
    {
        "question": "52. Que fait l'instruction `with` en Python ?",
        "options": [
            "a) Elle remplace une boucle.",
            "b) Elle garantit une libération correcte des ressources.",
            "c) Elle accélère l'exécution d'une fonction.",
            "d) Elle vérifie les exceptions dans un bloc."
        ],
        "answer": "b"
    },
    {
        "question": "53. Que retourne la méthode `__enter__()` d’un gestionnaire de contexte personnalisé ?",
        "options": [
            "a) Une exception si une erreur survient.",
            "b) L'objet de contexte utilisé dans le bloc `with`.",
            "c) Rien, elle est vide.",
            "d) Un itérateur."
        ],
        "answer": "b"
    },
    {
        "question": "54. Quelle méthode est appelée lorsque le bloc `with` se termine ?",
        "options": [
            "a) __close__()",
            "b) __exit__()",
            "c) __finalize__()",
            "d) __destroy__()"
        ],
        "answer": "b"
    },
    {
        "question": "55. Quelle bibliothèque fournit le décorateur `@contextmanager` ?",
        "options": [
            "a) functools",
            "b) contextlib",
            "c) itertools",
            "d) os"
        ],
        "answer": "b"
    },
    {
        "question": "56. Comment définir un décorateur Python basique ?",
        "options": [
            "a) Avec `@decorator` au-dessus d'une fonction.",
            "b) Avec une fonction imbriquée et un retour de fonction.",
            "c) Avec une classe dérivée d'object.",
            "d) Toutes les réponses ci-dessus."
        ],
        "answer": "b"
    },
    {
        "question": "57. Quel module contient `@lru_cache` pour la mise en cache d'une fonction ?",
        "options": [
            "a) functools",
            "b) collections",
            "c) cachetools",
            "d) decorators"
        ],
        "answer": "a"
    },
    {
        "question": "58. Quelle est la sortie de : `@decorator def f(x): return x**2` si le décorateur retourne 0 ?",
        "options": [
            "a) Le résultat est 0 pour tous les appels.",
            "b) La fonction f retourne son carré.",
            "c) Le décorateur ne modifie rien.",
            "d) Une erreur est levée."
        ],
        "answer": "a"
    },
    {
        "question": "59. Quel mot-clé permet d'utiliser un décorateur pour modifier une méthode d'instance ?",
        "options": [
            "a) @instance",
            "b) @staticmethod",
            "c) @classmethod",
            "d) Rien n'est requis."
        ],
        "answer": "d"
    },
    {
        "question": "60. Quelle est l'utilité principale des gestionnaires de contexte ?",
        "options": [
            "a) Gérer les ressources comme les fichiers ou les connexions réseau.",
            "b) Réduire le temps d'exécution des fonctions.",
            "c) Empêcher les exceptions dans un bloc donné.",
            "d) Vérifier les types d'arguments passés aux fonctions."
        ],
        "answer": "a"
    }
]

extra_design_pattern_questions = [
    {
        "question": "61. Quel design pattern est implémenté par une méthode qui retourne toujours la même instance d'une classe ?",
        "options": [
            "a) Singleton",
            "b) Factory",
            "c) Prototype",
            "d) Observer"
        ],
        "answer": "a"
    },
    {
        "question": "62. Quel design pattern permet de créer une famille d'objets sans spécifier leur classe concrète ?",
        "options": [
            "a) Abstract Factory",
            "b) Builder",
            "c) Factory Method",
            "d) Adapter"
        ],
        "answer": "a"
    },
    {
        "question": "63. À quoi sert le design pattern Decorator en Python ?",
        "options": [
            "a) Ajouter dynamiquement des fonctionnalités à un objet.",
            "b) Remplacer un objet existant par un autre.",
            "c) Gérer plusieurs instances d'une même classe.",
            "d) Définir des méthodes statiques."
        ],
        "answer": "a"
    },
    {
        "question": "64. Quel design pattern correspond à une chaîne d'objets où chacun traite ou passe la requête au suivant ?",
        "options": [
            "a) Chain of Responsibility",
            "b) Iterator",
            "c) Proxy",
            "d) Composite"
        ],
        "answer": "a"
    },
    {
        "question": "65. Quel design pattern utilise des objets pour représenter des opérations à exécuter ?",
        "options": [
            "a) Command",
            "b) Mediator",
            "c) Observer",
            "d) Prototype"
        ],
        "answer": "a"
    },
    {
        "question": "66. Quel design pattern permet de substituer un objet complexe par un objet simple pour différer un traitement ?",
        "options": [
            "a) Proxy",
            "b) Flyweight",
            "c) Composite",
            "d) Decorator"
        ],
        "answer": "a"
    },
    {
        "question": "67. Quel design pattern est utilisé pour traverser une structure d'objets sans en révéler les détails ?",
        "options": [
            "a) Iterator",
            "b) Visitor",
            "c) Composite",
            "d) Factory"
        ],
        "answer": "a"
    },
    {
        "question": "68. Quel est l'objectif principal du design pattern Observer ?",
        "options": [
            "a) Permettre à des objets de réagir aux changements d'un autre objet.",
            "b) Optimiser l'utilisation des ressources.",
            "c) Diviser un problème complexe en plusieurs objets simples.",
            "d) Gérer dynamiquement la création d'instances."
        ],
        "answer": "a"
    },
    {
        "question": "69. Quel design pattern est utilisé pour encapsuler un algorithme dans une classe distincte et interchangeable ?",
        "options": [
            "a) Strategy",
            "b) Builder",
            "c) Template Method",
            "d) Prototype"
        ],
        "answer": "a"
    },
    {
        "question": "70. Quel est l'objectif principal du design pattern Factory Method ?",
        "options": [
            "a) Fournir une interface pour créer des objets sans spécifier leur classe exacte.",
            "b) Structurer une hiérarchie d'objets complexes.",
            "c) Ajouter dynamiquement des fonctionnalités aux objets.",
            "d) Optimiser les performances d'accès aux objets."
        ],
        "answer": "a"
    }
]

extra_metaprogramming_questions = [
    {
        "question": "71. Quelle fonction permet d'obtenir ou de définir dynamiquement un attribut dans une classe Python ?",
        "options": [
            "a) setattr()",
            "b) getattr()",
            "c) setattr() et getattr()",
            "d) property()"
        ],
        "answer": "c"
    },
    {
        "question": "72. Que fait la méthode spéciale `__getattr__` dans une classe Python ?",
        "options": [
            "a) Elle est appelée lorsque l'attribut demandé n'existe pas.",
            "b) Elle renvoie la liste de tous les attributs de l'objet.",
            "c) Elle est appelée lorsqu'on définit un attribut.",
            "d) Elle est utilisée pour supprimer un attribut."
        ],
        "answer": "a"
    },
    {
        "question": "73. À quoi sert la méthode spéciale `__setattr__` ?",
        "options": [
            "a) Elle est appelée pour intercepter toutes les définitions d'attributs.",
            "b) Elle définit les méthodes statiques.",
            "c) Elle est utilisée pour récupérer un attribut inexistant.",
            "d) Elle permet de supprimer un attribut."
        ],
        "answer": "a"
    },
    {
        "question": "74. Quelle est la différence principale entre `__getattr__` et `__getattribute__` ?",
        "options": [
            "a) `__getattribute__` est appelée pour tous les accès aux attributs, alors que `__getattr__` est appelée uniquement pour les attributs inexistants.",
            "b) `__getattr__` est plus rapide que `__getattribute__`.",
            "c) `__getattribute__` ne fonctionne qu'avec des classes anciennes.",
            "d) `__getattr__` est utilisée pour définir un attribut."
        ],
        "answer": "a"
    },
    {
        "question": "75. Quelle méthode permet de contrôler dynamiquement la création d'instances dans une classe ?",
        "options": [
            "a) __new__()",
            "b) __init__()",
            "c) __call__()",
            "d) __create__()"
        ],
        "answer": "a"
    },
    {
        "question": "76. Que permet de faire la fonction `type()` lorsqu'elle est utilisée avec trois arguments ?",
        "options": [
            "a) Créer une classe dynamiquement.",
            "b) Modifier le type d'une instance.",
            "c) Accéder aux attributs d'une classe.",
            "d) Définir des méthodes spéciales."
        ],
        "answer": "a"
    },
    {
        "question": "77. Que fait un metaclass en Python ?",
        "options": [
            "a) Contrôle la création et le comportement des classes.",
            "b) Définit les méthodes d'instance pour une classe.",
            "c) Remplace les méthodes d'un objet spécifique.",
            "d) Associe les classes à des types particuliers."
        ],
        "answer": "a"
    },
    {
        "question": "78. Quel est l'effet du décorateur `@staticmethod` dans une classe ?",
        "options": [
            "a) Il rend une méthode indépendante de l'instance.",
            "b) Il transforme la méthode en une propriété.",
            "c) Il empêche une méthode d'être surchargée.",
            "d) Il associe une méthode à un attribut statique."
        ],
        "answer": "a"
    },
    {
        "question": "79. Quelle est la différence entre `@staticmethod` et `@classmethod` ?",
        "options": [
            "a) `@staticmethod` ne prend pas de référence à la classe, contrairement à `@classmethod`.",
            "b) `@classmethod` est lié à une instance, `@staticmethod` ne l'est pas.",
            "c) Les deux sont identiques.",
            "d) `@classmethod` ne peut pas accéder aux attributs statiques."
        ],
        "answer": "a"
    },
    {
        "question": "80. Quelle méthode spéciale est appelée lorsqu'un objet est utilisé comme une fonction ?",
        "options": [
            "a) __call__()",
            "b) __invoke__()",
            "c) __exec__()",
            "d) __run__()"
        ],
        "answer": "a"
    }
]

tricky_python_questions = [
    {
        "question": "81. Quelle est la sortie de ce code ?\n\n"
                    "def func(a, b=[]):\n"
                    " b.append(a)\n"
                    " return b\n\n"
                    "print(func(1))\n"
                    "print(func(2))",
        "options": [
            "a) [1], [2]",
            "b) [1], [1, 2]",
            "c) [1], [2]",
            "d) Une erreur est levée"
        ],
        "answer": "b"
    },
    {
        "question": "82. Quelle est la sortie de ce code ?\n\n"
                    "a = [1, 2, 3]\n"
                    "b = a\n"
                    "b.append(4)\n"
                    "print(a)",
        "options": [
            "a) [1, 2, 3]",
            "b) [1, 2, 3, 4]",
            "c) Une erreur est levée",
            "d) None"
        ],
        "answer": "b"
    },
    {
        "question": "83. Quelle est la sortie de ce code ?\n\n"
                    "def extendList(val, list=[]):\n"
                    " list.append(val)\n"
                    " return list\n\n"
                    "list1 = extendList(10)\n"
                    "list2 = extendList(123, [])\n"
                    "list3 = extendList('a')\n\n"
                    "print(list1, list2, list3)",
        "options": [
            "a) [10] [123] ['a']",
            "b) [10, 'a'] [123] [10, 'a']",
            "c) [10, 'a'] [123] ['a']",
            "d) Une erreur est levée"
        ],
        "answer": "b"
    },
    {
        "question": "84. Quelle est la sortie de ce code ?\n\n"
                    "x = 0\n"
                    "def incr():\n"
                    " global x\n"
                    " x += 1\n"
                    " return x\n\n"
                    "print(incr(), incr())",
        "options": [
            "a) 1, 1",
            "b) 1, 2",
            "c) Une erreur est levée",
            "d) 2, 2"
        ],
        "answer": "b"
    },
    {
        "question": "85. Quelle est la sortie de ce code ?\n\n"
                    "for i in range(3):\n"
                    " print(i)\n"
                    " i += 10\n",
        "options": [
            "a) 0, 1, 2",
            "b) 10, 11, 12",
            "c) 0, 11, 22",
            "d) 0, 1, 2 avec i modifié à chaque itération"
        ],
        "answer": "a"
    },
    {
        "question": "86. Quelle est la sortie de ce code ?\n\n"
                    "x = (i*i for i in range(3))\n"
                    "print(list(x))\n"
                    "print(list(x))",
        "options": [
            "a) [0, 1, 4], [0, 1, 4]",
            "b) [0, 1, 4], []",
            "c) [], []",
            "d) Une erreur est levée"
        ],
        "answer": "b"
    },
    {
        "question": "87. Que fait ce code ?\n\n"
                    "try:\n"
                    " 1/0\n"
                    "except ZeroDivisionError:\n"
                    " raise ValueError('Erreur personnalisée')",
        "options": [
            "a) Attrape l'erreur et affiche 'Erreur personnalisée'.",
            "b) Lève une exception ZeroDivisionError.",
            "c) Lève une exception ValueError avec un message.",
            "d) Rien, le programme s'arrête."
        ],
        "answer": "c"
    },
    {
        "question": "88. Quelle est la sortie de ce code ?\n\n"
                    "def test(val, lst=[]):\n"
                    " lst.append(val)\n"
                    " return lst\n\n"
                    "print(test(1))\n"
                    "print(test(2, []))\n"
                    "print(test(3))",
        "options": [
            "a) [1] [2] [3]",
            "b) [1, 3] [2] [1, 3]",
            "c) [1] [2] [1, 3]",
            "d) [1, 3] [2] [3]"
        ],
        "answer": "c"
    },
    {
        "question": "89. Quelle est la sortie de ce code ?\n\n"
                    "x = [1, 2, 3]\n"
                    "y = x[:]\n"
                    "y[0] = 10\n"
                    "print(x)",
        "options": [
            "a) [1, 2, 3]",
            "b) [10, 2, 3]",
            "c) Une erreur est levée",
            "d) Rien"
        ],
        "answer": "a"
    },
    {
        "question": "90. Quelle est la sortie de ce code ?\n\n"
                    "x = [1, 2, [3, 4]]\n"
                    "y = x[:]\n"
                    "y[2][0] = 10\n"
                    "print(x)",
        "options": [
            "a) [1, 2, [3, 4]]",
            "b) [1, 2, [10, 4]]",
            "c) Une erreur est levée",
            "d) Rien"
        ],
        "answer": "b"
    },
    {
        "question": "91. Que retourne cette expression ?\n\n"
                    "bool('False')",
        "options": [
            "a) True",
            "b) False",
            "c) Une erreur est levée",
            "d) None"
        ],
        "answer": "a"
    },
    {
        "question": "92. Quelle est la sortie de ce code ?\n\n"
                    "a = 10\n"
                    "b = 10.0\n"
                    "print(a is b)",
        "options": [
            "a) True",
            "b) False",
            "c) Une erreur est levée",
            "d) None"
        ],
        "answer": "b"
    },
    {
        "question": "93. Que retourne cette expression ?\n\n"
                    "''.join(str(i) for i in range(10) if i % 2 == 0)",
        "options": [
            "a) '02468'",
            "b) [0, 2, 4, 6, 8]",
            "c) '0 2 4 6 8'",
            "d) Une erreur est levée"
        ],
        "answer": "a"
    },
    {
        "question": "94. Que fait ce code ?\n\n"
                    "def foo(bar=[]):\n"
                    " bar += [1]\n"
                    " return bar\n\n"
                    "print(foo())\n"
                    "print(foo())",
        "options": [
            "a) [1], [1]",
            "b) [1], [1, 1]",
            "c) Une erreur est levée",
            "d) [1], []"
        ],
        "answer": "b"
    },
    {
        "question": "95. Quelle est la sortie de ce code ?\n\n"
                    "def func():\n"
                    " return 'Hello', 'World'\n\n"
                    "result = func()\n"
                    "print(type(result))",
        "options": [
            "a) <class 'tuple'>",
            "b) <class 'str'>",
            "c) <class 'list'>",
            "d) Une erreur est levée"
        ],
        "answer": "a"
    },
    {
        "question": "96. En Pandas, comment regrouper un DataFrame df par la colonne 'date' et calculer la moyenne de chaque groupe ?",
        "options": [
            "a) df.group('date').mean()",
            "b) df.groupby('date').mean()",
            "c) df.group_by('date').mean()",
            "d) df.group_by('date').average()"
        ],
        "answer": "b"
    },
    {
        "question": "97. Quel paramètre de la fonction merge() est utilisé pour spécifier une jointure extérieure ?",
        "options": [
            "a) how='outer'",
            "b) how='left'",
            "c) how='right'",
            "d) how='inner'"
        ],
        "answer": "a"
    },
    {
        "question": "98. Comment transformer une colonne 'taille' d'un DataFrame df en utilisant une fonction lambda qui divise chaque élément par 2 ?",
        "options": [
            "a) df['taille'] = df['taille'].apply(lambda x: x/2)",
            "b) df.transform(lambda x: x['taille']/2)",
            "c) df['taille'] = df['taille'].map(lambda x: x/2)",
            "d) df['taille'].apply(lambda x: x/2)"
        ],
        "answer": "d"
    },
    {
        "question": "99. En Pandas, comment réinitialiser l'index d'un DataFrame df sans conserver l'ancien index ?",
        "options": [
            "a) df.reset_index()",
            "b) df.reset_index(drop=True)",
            "c) df.index_reset()",
            "d) df.reset(drop=True)"
        ],
        "answer": "b"
    },
    {
        "question": "100. Comment appliquer une fonction personnalisée à chaque groupe après avoir utilisé groupby() ?",
        "options": [
            "a) df.groupby('colonne').map(ma_fonction)",
            "b) df.groupby('colonne').transform(ma_fonction)",
            "c) df.groupby('colonne').apply(ma_fonction)",
            "d) df.group_apply('colonne', ma_fonction)"
        ],
        "answer": "c"
    },
    {
        "question": "101. Comment utiliser pivot_table() pour calculer la somme des ventes par produit et par région ?",
        "options": [
            "a) df.pivot_table(values='ventes', index='produit', columns='region', aggfunc='sum')",
            "b) df.pivot_table('produit', 'region', 'ventes', 'sum')",
            "c) df.pivot('produit', 'region', 'sum')",
            "d) df.pivot_table(sum='ventes', index='produit', columns='region')"
        ],
        "answer": "a"
    },
    {
        "question": "102. Quelle méthode utiliser pour concaténer verticalement deux DataFrames df1 et df2 ?",
        "options": [
            "a) pd.concat([df1, df2], axis=1)",
            "b) pd.concat([df1, df2], axis=0)",
            "c) df1.concat(df2)",
            "d) df1.append(df2)"
        ],
        "answer": "b"
    },
    {
        "question": "103. Comment convertir une colonne de chaînes de caractères en datetimes dans un DataFrame df ?",
        "options": [
            "a) df['date'] = pd.to_datetime(df['date'])",
            "b) df['date'] = pd.datetime(df['date'])",
            "c) df['date'] = df['date'].to_date()",
            "d) df['date'] = df['date'].astype(datetime)"
        ],
        "answer": "a"
    },
    {
        "question": "104. Comment vérifier si deux DataFrames df1 et df2 sont identiques dans leur contenu ?",
        "options": [
            "a) df1.equals(df2)",
            "b) df1.compare(df2)",
            "c) df1 == df2",
            "d) df1.is_equal(df2)"
        ],
        "answer": "a"
    },
    {
        "question": "105. Comment utiliser df.query() pour sélectionner les lignes où 'âge' est supérieur à 30 ?",
        "options": [
            "a) df.query('âge > 30')",
            "b) df.select('âge > 30')",
            "c) df.query('âge', 30)",
            "d) df.filter(age > 30)"
        ],
        "answer": "a"
    },
    {
        "question": "106. Comment calculer la différence entre les valeurs consécutives d'une colonne 'prix' dans un DataFrame df ?",
        "options": [
            "a) df['prix_diff'] = df['prix'].diff()",
            "b) df['prix_diff'] = df['prix'].difference()",
            "c) df['prix_diff'] = df['prix'].delta()",
            "d) df['prix_diff'] = df['prix'].change()"
        ],
        "answer": "a"
    },
    {
        "question": "107. Comment renommer la colonne 'ancien_nom' en 'nouveau_nom' dans un DataFrame df ?",
        "options": [
            "a) df.rename(columns={'ancien_nom': 'nouveau_nom'})",
            "b) df.rename({'ancien_nom': 'nouveau_nom'})",
            "c) df.columns.rename('ancien_nom', 'nouveau_nom')",
            "d) df.rename_column('ancien_nom', 'nouveau_nom')"
        ],
        "answer": "a"
    },
    {
        "question": "108. Comment créer une nouvelle colonne 'total' en additionnant les colonnes 'prix' et 'taxe' dans df ?",
        "options": [
            "a) df['total'] = df['prix'] + df['taxe']",
            "b) df['total'] = df.sum('prix', 'taxe')",
            "c) df['total'] = df.add('prix', 'taxe')",
            "d) df['total'] = df['prix'].add(df['taxe'])"
        ],
        "answer": "a"
    },
    {
        "question": "109. Quel est le moyen d'accéder à un sous-ensemble de lignes dans df, spécifiquement les lignes de 10 à 20 ?",
        "options": [
            "a) df.iloc[10:21]",
            "b) df.loc[10:20]",
            "c) df.rows[10:20]",
            "d) df.select_rows(10, 20)"
        ],
        "answer": "a"
    },
    {
        "question": "110. Comment utiliser transform() pour normaliser une colonne 'score' par groupe dans df ?",
        "options": [
            "a) df.groupby('groupe')['score'].transform(lambda x: x/x.max())",
            "b) df['score'].normalize('groupe')",
            "c) df.transform('score', 'groupe', 'normalize')",
            "d) df.groupby('groupe').normalize('score')"
        ],
        "answer": "a"
    },
    {
        "question": "111. Comment obtenir une liste des valeurs uniques de la colonne 'ville' dans df ?",
        "options": [
            "a) df['ville'].unique()",
            "b) df['ville'].values()",
            "c) df['ville'].distinct()",
            "d) df['ville'].uniques()"
        ],
        "answer": "a"
    },
    {
        "question": "112. Comment filtrer df pour obtenir les lignes où la colonne 'revenu' est NaN ?",
        "options": [
            "a) df[df['revenu'].isnull()]",
            "b) df[df['revenu'].isna()]",
            "c) df[df['revenu'] == None]",
            "d) df[df['revenu'].null()]"
        ],
        "answer": "a"
    },
    {
        "question": "113. Quel est le moyen de décaler les valeurs d'une colonne 'température' vers le bas dans df ?",
        "options": [
            "a) df['température_shift'] = df['température'].shift(1)",
            "b) df['température_shift'] = df['température'].shift(-1)",
            "c) df['température_shift'] = df['température'].roll(1)",
            "d) df['température_shift'] = df['température'].slide(1)"
        ],
        "answer": "a"
    },
    {
        "question": "114. Comment échantillonner aléatoirement 10% des lignes de df ?",
        "options": [
            "a) df.sample(frac=0.1)",
            "b) df.sample(n=10)",
            "c) df.sample(percent=10)",
            "d) df.select_random(0.1)"
        ],
        "answer": "a"
    },
    {
        "question": "115. Comment utiliser rolling() pour obtenir la moyenne mobile sur 5 périodes pour la colonne 'volume' dans df ?",
        "options": [
            "a) df['volume_rolling'] = df['volume'].rolling(window=5).mean()",
            "b) df['volume_rolling'] = df['volume'].average(5)",
            "c) df['volume_rolling'] = df['volume'].mov_avg(5)",
            "d) df['volume_rolling'] = df['volume'].mean(window=5)"
        ],
        "answer": "a"
    },
    {
        "question": "116. Comment remplir les valeurs manquantes de 'salaire' avec la moyenne de cette colonne dans df ?",
        "options": [
            "a) df['salaire'].fillna(df['salaire'].mean())",
            "b) df['salaire'].fill(df['salaire'].mean())",
            "c) df['salaire'].mean_fill()",
            "d) df['salaire'].fill_mean()"
        ],
        "answer": "a"
    },
    {
        "question": "117. Comment diviser un DataFrame df en sous-ensembles de taille 100 ?",
        "options": [
            "a) np.array_split(df, len(df)//100)",
            "b) df.split(100)",
            "c) df.partition(100)",
            "d) np.divide(df, 100)"
        ],
        "answer": "a"
    },
    {
        "question": "118. Comment supprimer les doublons basés uniquement sur la colonne 'email' dans df ?",
        "options": [
            "a) df.drop_duplicates(subset=['email'])",
            "b) df.unique('email')",
            "c) df.distinct('email')",
            "d) df.remove_duplicates('email')"
        ],
        "answer": "a"
    },
    {
        "question": "119. Comment calculer le taux de variation de la colonne 'prix' dans df ?",
        "options": [
            "a) df['prix_pct_change'] = df['prix'].pct_change()",
            "b) df['prix_pct_change'] = df['prix'].percentage()",
            "c) df['prix_pct_change'] = df['prix'].rate_of_change()",
            "d) df['prix_pct_change'] = df['prix'].delta()"
        ],
        "answer": "a"
    },
    {
        "question": "120. Comment créer un histogramme de la colonne 'quantité' dans df ?",
        "options": [
            "a) df['quantité'].plot.hist()",
            "b) df.plot.hist('quantité')",
            "c) df['quantité'].histogram()",
            "d) df.hist('quantité')"
        ],
        "answer": "a"
    },
    {
        "question": "121. Comment ajouter des colonnes d'indicateurs d'une colonne catégorielle 'genre' dans df ?",
        "options": [
            "a) pd.get_dummies(df['genre'])",
            "b) pd.indicators(df['genre'])",
            "c) pd.dummies(df['genre'])",
            "d) df.indicator_columns('genre')"
        ],
        "answer": "a"
    },
    {
        "question": "122. Comment fractionner la colonne 'nom_complet' en 'prénom' et 'nom' dans df ?",
        "options": [
            "a) df[['prénom', 'nom']] = df['nom_complet'].str.split(' ', expand=True)",
            "b) df.split('nom_complet', into=['prénom', 'nom'])",
            "c) df['nom_complet'].divide(['prénom', 'nom'])",
            "d) df[['prénom', 'nom']] = df['nom_complet'].split(' ', expand=True)"
        ],
        "answer": "a"
    },
    {
        "question": "123. Comment ajouter une colonne 'rang' basée sur la colonne 'score' dans df ?",
        "options": [
            "a) df['rang'] = df['score'].rank()",
            "b) df['rang'] = df['score'].order()",
            "c) df['rang'] = df['score'].graded()",
            "d) df['rang'] = df['score'].ranking()"
        ],
        "answer": "a"
    },
    {
        "question": "124. Comment créer une colonne 'catégorie' en utilisant des intervalles sur la colonne 'âge' dans df ?",
        "options": [
            "a) df['catégorie'] = pd.cut(df['âge'], bins=[0, 18, 65, 99])",
            "b) df['catégorie'] = pd.interval(df['âge'], [0, 18, 65, 99])",
            "c) pd.divide(df['âge'], intervals=[0, 18, 65, 99])",
            "d) df['catégorie'] = pd.cut(df['âge'], intervals=[0, 18, 65, 99])"
        ],
        "answer": "a"
    },
    {
        "question": "125. Comment utiliser apply() pour convertir toutes les valeurs d'une colonne 'température' de Celsius à Fahrenheit dans df ?",
        "options": [
            "a) df['température'] = df['température'].apply(lambda x: x * 9/5 + 32)",
            "b) df['température'] = df['température'].map(lambda x: x * 9/5 + 32)",
            "c) df.convert('température', 'Fahrenheit')",
            "d) df['température'] = df['température'].transform(lambda x: x * 9/5 + 32)"
        ],
        "answer": "a"
    },
    {
        "question": "126. Comment calculer la médiane de la colonne 'revenu' pour chaque groupe dans df ?",
        "options": [
            "a) df.groupby('groupe')['revenu'].median()",
            "b) df.groupby('groupe').median('revenu')",
            "c) df['revenu'].median('groupe')",
            "d) df.groupby('groupe')['revenu'].central()"
        ],
        "answer": "a"
    },
    {
        "question": "127. Comment réordonner les colonnes de df pour placer 'nom' avant 'prénom' ?",
        "options": [
            "a) df = df[['nom', 'prénom'] + df.columns.drop(['nom', 'prénom']).tolist()]",
            "b) df.reorder(['nom', 'prénom'])",
            "c) df.columns = ['nom', 'prénom']",
            "d) df.swap('nom', 'prénom')"
        ],
        "answer": "a"
    },
    {
        "question": "128. Comment filtrer df pour n'afficher que les lignes où 'date' est après le 1er janvier 2020 ?",
        "options": [
            "a) df[df['date'] > '2020-01-01']",
            "b) df.query('date > 2020-01-01')",
            "c) df.select('date > 2020-01-01')",
            "d) df.filter(date > '2020-01-01')"
        ],
        "answer": "a"
    },
    {
        "question": "129. Comment inverser l'ordre des lignes dans df ?",
        "options": [
            "a) df = df.iloc[::-1]",
            "b) df.reverse()",
            "c) df.reorder(reverse=True)",
            "d) df.descend()"
        ],
        "answer": "a"
    },
    {
        "question": "130. Comment utiliser groupby() et agg() pour obtenir la somme et la moyenne de 'ventes' par 'produit' dans df ?",
        "options": [
            "a) df.groupby('produit')['ventes'].agg(['sum', 'mean'])",
            "b) df.group_agg('produit', 'ventes', ['sum', 'mean'])",
            "c) df.aggregate('produit', 'ventes', ['sum', 'mean'])",
            "d) df.aggregate(['produit', 'ventes'], 'sum', 'mean')"
        ],
        "answer": "a"
    },
    {
        "question": "131. Comment convertir un DataFrame df en format de liste de dictionnaires ?",
        "options": [
            "a) df.to_dict(orient='records')",
            "b) df.to_list('dict')",
            "c) df.dict_list()",
            "d) df.convert('records')"
        ],
        "answer": "a"
    },
    {
        "question": "132. Comment calculer la variance de la colonne 'prix' dans df ?",
        "options": [
            "a) df['prix'].var()",
            "b) df.variance('prix')",
            "c) df['prix'].calculate_variance()",
            "d) df.var('prix')"
        ],
        "answer": "a"
    },
    {
        "question": "133. Comment supprimer les lignes avec des valeurs manquantes dans plus de 50% des colonnes de df ?",
        "options": [
            "a) df.dropna(thresh=int(0.5*len(df.columns)))",
            "b) df.remove_na(0.5)",
            "c) df.dropna(percent=50)",
            "d) df.remove_missing(thresh=50)"
        ],
        "answer": "a"
    },
    {
        "question": "134. Comment utiliser merge() pour effectuer une jointure à gauche entre df1 et df2 sur la colonne 'ID' ?",
        "options": [
            "a) pd.merge(df1, df2, how='left', on='ID')",
            "b) df1.join(df2, how='left', on='ID')",
            "c) df1.left_merge(df2, 'ID')",
            "d) pd.join(df1, df2, 'ID', 'left')"
        ],
        "answer": "a"
    },
    {
        "question": "135. Comment créer un DataFrame df à partir de plusieurs fichiers CSV stockés dans un dossier ?",
        "options": [
            "a) df = pd.concat([pd.read_csv(f) for f in glob.glob('dossier/*.csv')])",
            "b) df = pd.read_csv_batch('dossier')",
            "c) df = pd.concat_csv('dossier')",
            "d) df = pd.read_csv('dossier', multiple=True)"
        ],
        "answer": "a"
    }
]

# Ajout des nouvelles questions à la liste existante
questions.extend(extra_questions)
questions.extend(extra_generator_iterator_questions)
questions.extend(extra_context_decorator_questions)
questions.extend(extra_design_pattern_questions)
questions.extend(extra_metaprogramming_questions)
questions.extend(tricky_python_questions)

# Fonction pour exécuter le quiz
def run_quiz(questions):
    print("Bienvenue au quiz Python (Niveau intermédiaire/expert) !")
    print("Répondez en entrant 'a', 'b', 'c' ou 'd'.\n")
    score = 0

    # Mélanger les questions pour chaque exécution
    random.shuffle(questions)

    # Posez toutes les questions
    for i, q in enumerate(questions):
        print(f"Q{i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Votre réponse: ").strip().lower()
        if answer == q["answer"]:
            print("Correct !\n")
            score += 1
        else:
            print(f"Incorrect. La bonne réponse était: {q['answer']}.\n")

    print(f"Quiz terminé ! Vous avez obtenu {score}/{len(questions)} points.")

# Exécuter le quiz
def test(val, lst=[]):
 lst.append(val)
 return lst

print(test(1))
print(test(2, []))
print(test(3))
run_quiz(questions)
