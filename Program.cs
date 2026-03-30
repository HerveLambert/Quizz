// C# Expert Quiz (100 QCM) - .NET 6+
// Compile: dotnet new console -n QuizCSharp ; replace Program.cs ; dotnet run

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;

public record Question(string Text, string[] Options, char Answer);

public static class Program
{
    private static readonly Random Rng = new();

    public static void Main()
    {
        var questions = BuildQuestions();
        RunQuiz(questions);
    }

    private static void RunQuiz(List<Question> questions)
    {
        Console.WriteLine("Bienvenue au quiz C# (Niveau expert) !");
        Console.WriteLine("Répondez en entrant 'a', 'b', 'c' ou 'd'.\n");

        Shuffle(questions);

        int score = 0;
        for (int i = 0; i < questions.Count; i++)
        {
            var q = questions[i];
            Console.WriteLine($"Q{i + 1}: {q.Text}");
            foreach (var opt in q.Options) Console.WriteLine(opt);

            Console.Write("Votre réponse: ");
            var input = (Console.ReadLine() ?? "").Trim().ToLowerInvariant();
            char ans = input.Length > 0 ? input[0] : '?';

            if (ans == q.Answer)
            {
                Console.WriteLine("Correct !\n");
                score++;
            }
            else
            {
                Console.WriteLine($"Incorrect. La bonne réponse était: {q.Answer}.\n");
            }
        }

        Console.WriteLine($"Quiz terminé ! Vous avez obtenu {score}/{questions.Count} points.");
    }

    private static void Shuffle<T>(IList<T> list)
    {
        for (int i = list.Count - 1; i > 0; i--)
        {
            int j = Rng.Next(i + 1);
            (list[i], list[j]) = (list[j], list[i]);
        }
    }

    private static List<Question> BuildQuestions()
    {
        var qs = new List<Question>();

        // ----------------------------
        // POO / classes / properties
        // ----------------------------
        qs.Add(new Question(
            "1. En C#, comment déclarer une classe `Voiture` avec un constructeur qui initialise un champ `marque` ?",
            new[]
            {
                "a) class Voiture { string marque; Voiture(string marque){ marque = marque; } }",
                "b) class Voiture { private string marque; public Voiture(string marque){ this.marque = marque; } }",
                "c) class Voiture(string marque) { this.marque = marque; }",
                "d) class Voiture { public Voiture(){ marque = \"\"; } }"
            },
            'b'
        ));

        qs.Add(new Question(
            "2. Quelle différence principale entre un champ `readonly` et un champ `const` ?",
            new[]
            {
                "a) `readonly` est évalué à la compilation, `const` à l'exécution",
                "b) `const` peut être assigné dans le constructeur, `readonly` non",
                "c) `const` est évalué à la compilation, `readonly` peut être assigné au constructeur",
                "d) Aucune, ils sont identiques"
            },
            'c'
        ));

        qs.Add(new Question(
            "3. Quelle syntaxe crée une propriété auto-implémentée `Age` accessible en lecture/écriture ?",
            new[]
            {
                "a) public int Age();",
                "b) public int Age { get; set; }",
                "c) public int Age { read; write; }",
                "d) public property int Age;"
            },
            'b'
        ));

        qs.Add(new Question(
            "4. Comment empêcher l'héritage d'une classe en C# ?",
            new[]
            {
                "a) sealed class MaClasse { }",
                "b) static class MaClasse { }",
                "c) private class MaClasse { }",
                "d) locked class MaClasse { }"
            },
            'a'
        ));

        qs.Add(new Question(
            "5. Quel mot-clé permet de référencer l'instance courante dans une classe ?",
            new[]
            {
                "a) self",
                "b) this",
                "c) me",
                "d) current"
            },
            'b'
        ));

        qs.Add(new Question(
            "6. Quel est l'effet de `virtual` sur une méthode ?",
            new[]
            {
                "a) Elle ne peut pas être appelée",
                "b) Elle peut être surchargée avec `override` dans une classe dérivée",
                "c) Elle est statique",
                "d) Elle est forcément abstraite"
            },
            'b'
        ));

        qs.Add(new Question(
            "7. Quelle déclaration définit une interface en C# ?",
            new[]
            {
                "a) abstract class IFoo { }",
                "b) interface IFoo { void Bar(); }",
                "c) class interface IFoo { void Bar(); }",
                "d) module IFoo { void Bar(); }"
            },
            'b'
        ));

        qs.Add(new Question(
            "8. Quel est le rôle principal d'une classe `abstract` ?",
            new[]
            {
                "a) Interdire l'héritage",
                "b) Empêcher la création d'instances directes et servir de base",
                "c) Forcer toutes les méthodes à être statiques",
                "d) Optimiser les performances"
            },
            'b'
        ));

        qs.Add(new Question(
            "9. Quelle différence entre `override` et `new` sur une méthode ?",
            new[]
            {
                "a) `new` surcharge, `override` masque",
                "b) `override` redéfinit le polymorphisme, `new` masque (hiding)",
                "c) Aucun, c'est pareil",
                "d) `new` est interdit en C#"
            },
            'b'
        ));

        qs.Add(new Question(
            "10. Les `records` (C# 9+) sont principalement conçus pour :",
            new[]
            {
                "a) Les types mutables à haute perf",
                "b) Les types immuables orientés données avec égalité par valeur",
                "c) Remplacer toutes les classes",
                "d) Éviter l'héritage"
            },
            'b'
        ));

        // ----------------------------
        // Collections / generics
        // ----------------------------
        qs.Add(new Question(
            "11. Quelle collection est la plus adaptée pour des recherches clé -> valeur en O(1) moyen ?",
            new[]
            {
                "a) List<T>",
                "b) Dictionary<TKey,TValue>",
                "c) LinkedList<T>",
                "d) Queue<T>"
            },
            'b'
        ));

        qs.Add(new Question(
            "12. Quelle est la sortie de ce code ? `var a = new List<int>{1,2,3}; var b = a; b.Add(4); Console.WriteLine(a.Count);`",
            new[]
            {
                "a) 3",
                "b) 4",
                "c) Erreur de compilation",
                "d) 0"
            },
            'b'
        ));

        qs.Add(new Question(
            "13. Comment faire une copie superficielle (shallow) d'une List<T> ?",
            new[]
            {
                "a) var b = a;",
                "b) var b = new List<T>(a);",
                "c) var b = a.CopyDeep();",
                "d) var b = (List<T>)a.Clone();"
            },
            'b'
        ));

        qs.Add(new Question(
            "14. Quelle contrainte générique impose qu'un type ait un constructeur sans paramètre ?",
            new[]
            {
                "a) where T : new()",
                "b) where T : class()",
                "c) where T : ctor()",
                "d) where T : default()"
            },
            'a'
        ));

        qs.Add(new Question(
            "15. `IEnumerable<T>` vs `ICollection<T>` : différence clé ?",
            new[]
            {
                "a) `IEnumerable` permet d'itérer, `ICollection` ajoute Count/Add/Remove",
                "b) `IEnumerable` permet d'ajouter, `ICollection` non",
                "c) Ils sont identiques",
                "d) `ICollection` ne peut pas être parcouru avec foreach"
            },
            'a'
        ));

        qs.Add(new Question(
            "16. Quel est l'effet de `var` en C# ?",
            new[]
            {
                "a) Typage dynamique à l'exécution",
                "b) Inférence de type à la compilation",
                "c) Désactive le typage",
                "d) Force le type object"
            },
            'b'
        ));

        qs.Add(new Question(
            "17. Quelle collection garantit l'ordre d'insertion ?",
            new[]
            {
                "a) HashSet<T>",
                "b) Dictionary<TKey,TValue> (toujours)",
                "c) List<T>",
                "d) Stack<T>"
            },
            'c'
        ));

        qs.Add(new Question(
            "18. Quelle instruction crée un tableau de 3 entiers initialisés à 0 ?",
            new[]
            {
                "a) int[] a = new int[3];",
                "b) int[] a = new int(3);",
                "c) int[] a = {0,0};",
                "d) array<int> a = 3;"
            },
            'a'
        ));

        qs.Add(new Question(
            "19. Quelle est la sortie ? `Console.WriteLine(\"abc\".ToUpperInvariant());`",
            new[]
            {
                "a) abc",
                "b) ABC",
                "c) Abc",
                "d) Erreur"
            },
            'b'
        ));

        qs.Add(new Question(
            "20. Boxing : que se passe-t-il ? `object o = 42;`",
            new[]
            {
                "a) 42 est stocké comme int sur la pile uniquement",
                "b) 42 (type int) est boxé en object sur le tas",
                "c) Erreur de compilation",
                "d) Conversion implicite en string"
            },
            'b'
        ));

        // ----------------------------
        // LINQ (équivalent manip de données)
        // ----------------------------
        qs.Add(new Question(
            "21. LINQ : comment filtrer les nombres pairs d'une liste `xs` ?",
            new[]
            {
                "a) xs.Filter(x => x%2==0)",
                "b) xs.Where(x => x % 2 == 0)",
                "c) xs.Select(x => x%2==0)",
                "d) xs.GroupBy(x => x%2==0)"
            },
            'b'
        ));

        qs.Add(new Question(
            "22. LINQ : que retourne `Select` ?",
            new[]
            {
                "a) Un filtre",
                "b) Une projection (map)",
                "c) Un tri",
                "d) Une agrégation"
            },
            'b'
        ));

        qs.Add(new Question(
            "23. Quelle méthode LINQ effectue un tri croissant ?",
            new[]
            {
                "a) SortBy",
                "b) OrderBy",
                "c) Arrange",
                "d) Rank"
            },
            'b'
        ));

        qs.Add(new Question(
            "24. Quelle est la sortie ? `new[]{3,1,4,1}.OrderByDescending(x=>x).ToArray()`",
            new[]
            {
                "a) [1,1,3,4]",
                "b) [4,3,1,1]",
                "c) [1,3,1,4]",
                "d) Erreur"
            },
            'b'
        ));

        qs.Add(new Question(
            "25. Quelle est la différence majeure entre `First()` et `FirstOrDefault()` ?",
            new[]
            {
                "a) `First()` retourne toujours null",
                "b) `First()` jette si la séquence est vide, `FirstOrDefault()` non",
                "c) `FirstOrDefault()` jette toujours",
                "d) Aucune"
            },
            'b'
        ));

        qs.Add(new Question(
            "26. LINQ : comment faire une jointure (join) sur clé entre `a` et `b` ?",
            new[]
            {
                "a) a.Merge(b, onKey)",
                "b) a.Join(b, x=>x.Id, y=>y.Id, (x,y)=>...)",
                "c) a.Zip(b)",
                "d) a.Concat(b)"
            },
            'b'
        ));

        qs.Add(new Question(
            "27. `GroupBy` suivi de `Sum` permet :",
            new[]
            {
                "a) De trier",
                "b) De regrouper puis agréger",
                "c) De cloner",
                "d) De faire du multithreading"
            },
            'b'
        ));

        qs.Add(new Question(
            "28. Quelle méthode LINQ force l'exécution immédiate (matérialisation) ?",
            new[]
            {
                "a) Where",
                "b) Select",
                "c) ToList",
                "d) GroupBy"
            },
            'c'
        ));

        qs.Add(new Question(
            "29. Deferred execution : `Where` et `Select` sont généralement :",
            new[]
            {
                "a) Exécutés immédiatement",
                "b) Exécutés à l'itération (lazy)",
                "c) Exécutés seulement en debug",
                "d) Interdits sans ToList"
            },
            'b'
        ));

        qs.Add(new Question(
            "30. Quelle est la sortie ? `Enumerable.Range(0,5).Where(x=>x%2==0).Select(x=>x*x).ToArray()`",
            new[]
            {
                "a) [0,4,16]",
                "b) [0,1,4,9,16]",
                "c) [0,2,4,6]",
                "d) [1,4,16]"
            },
            'a'
        ));

        // ----------------------------
        // Iterators / yield / foreach
        // ----------------------------
        qs.Add(new Question(
            "31. À quoi sert `yield return` ?",
            new[]
            {
                "a) À retourner une List<T> complète",
                "b) À produire une séquence paresseuse (iterator)",
                "c) À paralléliser automatiquement",
                "d) À ignorer les exceptions"
            },
            'b'
        ));

        qs.Add(new Question(
            "32. Quel type retourne typiquement une méthode utilisant `yield return` ?",
            new[]
            {
                "a) List<T>",
                "b) IEnumerable<T>",
                "c) Dictionary<T,T>",
                "d) Task<T>"
            },
            'b'
        ));

        qs.Add(new Question(
            "33. Quelle est la sortie ?\n`IEnumerable<int> Gen(){ yield return 1; yield return 2; }\nConsole.WriteLine(Gen().First());`",
            new[]
            {
                "a) 0",
                "b) 1",
                "c) 2",
                "d) Erreur"
            },
            'b'
        ));

        qs.Add(new Question(
            "34. Que se passe-t-il si on itère deux fois sur un iterator `yield` (sans le matérialiser) ?",
            new[]
            {
                "a) La seconde itération renvoie toujours vide",
                "b) L'iterator peut être ré-exécuté (nouvelle énumération) selon l'implémentation",
                "c) Erreur de compilation",
                "d) Il devient automatiquement une liste"
            },
            'b'
        ));

        qs.Add(new Question(
            "35. Quelle interface expose `MoveNext()` et `Current` ?",
            new[]
            {
                "a) IEnumerable<T>",
                "b) IEnumerator<T>",
                "c) ICollection<T>",
                "d) IList<T>"
            },
            'b'
        ));

        // ----------------------------
        // IDisposable / using (context manager)
        // ----------------------------
        qs.Add(new Question(
            "36. Le rôle principal de `using` (statement) est :",
            new[]
            {
                "a) Optimiser le JIT",
                "b) Garantir l'appel de Dispose() même en cas d'exception",
                "c) Importer un namespace uniquement",
                "d) Déclarer une variable globale"
            },
            'b'
        ));

        qs.Add(new Question(
            "37. Quelle interface doit être implémentée pour être utilisable avec `using` ?",
            new[]
            {
                "a) IClosable",
                "b) IDisposable",
                "c) IFinalizable",
                "d) IContext"
            },
            'b'
        ));

        qs.Add(new Question(
            "38. Le finalizer (`~MaClasse()`) :",
            new[]
            {
                "a) Est déterministe et immédiat",
                "b) Est non déterministe et géré par le GC",
                "c) Remplace Dispose() automatiquement",
                "d) N'existe pas en C#"
            },
            'b'
        ));

        // ----------------------------
        // Exceptions / flow
        // ----------------------------
        qs.Add(new Question(
            "39. Quelle instruction relance l'exception originale en conservant la stacktrace ?",
            new[]
            {
                "a) throw ex;",
                "b) throw;",
                "c) raise;",
                "d) rethrow;"
            },
            'b'
        ));

        qs.Add(new Question(
            "40. Exception filters : quelle syntaxe est correcte ?",
            new[]
            {
                "a) catch (Exception ex) if (cond) { }",
                "b) catch (Exception ex) when (cond) { }",
                "c) catch when (cond) (Exception ex) { }",
                "d) catch (cond) { }"
            },
            'b'
        ));

        // ----------------------------
        // async/await
        // ----------------------------
        qs.Add(new Question(
            "41. `await` : effet principal ?",
            new[]
            {
                "a) Bloque le thread jusqu'à la fin",
                "b) Rend le code asynchrone non-bloquant (avec continuation)",
                "c) Lance une nouvelle tâche sur un thread dédié à coup sûr",
                "d) Désactive les exceptions"
            },
            'b'
        ));

        qs.Add(new Question(
            "42. Une méthode `async` qui ne retourne pas de valeur retourne typiquement :",
            new[]
            {
                "a) void",
                "b) Task",
                "c) IEnumerable",
                "d) Action"
            },
            'b'
        ));

        qs.Add(new Question(
            "43. Quel est un risque classique de `.Result` ou `.Wait()` sur une Task en contexte UI/ASP.NET ?",
            new[]
            {
                "a) Accélération",
                "b) Deadlock potentiel",
                "c) Suppression d'exceptions",
                "d) Forçage du multithread"
            },
            'b'
        ));

        // ----------------------------
        // Value vs Reference / string interning / nullable
        // ----------------------------
        qs.Add(new Question(
            "44. Les `struct` en C# sont principalement :",
            new[]
            {
                "a) Types référence",
                "b) Types valeur",
                "c) Toujours alloués sur le tas",
                "d) Identiques aux records"
            },
            'b'
        ));

        qs.Add(new Question(
            "45. `string` en C# est :",
            new[]
            {
                "a) mutable",
                "b) immutable",
                "c) un struct",
                "d) un pointeur brut"
            },
            'b'
        ));

        qs.Add(new Question(
            "46. Nullable reference types (C# 8+) : `string?` signifie :",
            new[]
            {
                "a) string non-null garanti",
                "b) string pouvant être null (annotation)",
                "c) string alloué sur la pile",
                "d) string boxé"
            },
            'b'
        ));

        qs.Add(new Question(
            "47. `int?` est un alias de :",
            new[]
            {
                "a) Nullable<int>",
                "b) Optional<int>",
                "c) Maybe<int>",
                "d) int|nil"
            },
            'a'
        ));

        // ----------------------------
        // Delegates / events / lambdas
        // ----------------------------
        qs.Add(new Question(
            "48. Quel type représente une fonction prenant un int et renvoyant un string ?",
            new[]
            {
                "a) Action<int>",
                "b) Func<int, string>",
                "c) Predicate<string>",
                "d) Delegate<int,string>"
            },
            'b'
        ));

        qs.Add(new Question(
            "49. Un `event` en C# est principalement :",
            new[]
            {
                "a) Un champ public simple",
                "b) Un mécanisme d'abonnement/désabonnement (Observer-like)",
                "c) Un thread",
                "d) Un attribut de compilation"
            },
            'b'
        ));

        qs.Add(new Question(
            "50. Différence clé entre `Action` et `Func` ?",
            new[]
            {
                "a) Action retourne une valeur, Func non",
                "b) Func retourne une valeur, Action retourne void",
                "c) Ils sont identiques",
                "d) Action est pour async seulement"
            },
            'b'
        ));

        // ----------------------------
        // Attributes / Reflection (metaprogramming analogue)
        // ----------------------------
        qs.Add(new Question(
            "51. Quel concept C# se rapproche le plus des 'decorators' Python (au sens annotation/métadonnées) ?",
            new[]
            {
                "a) using",
                "b) attributes (ex: [Obsolete])",
                "c) namespaces",
                "d) partial classes"
            },
            'b'
        ));

        qs.Add(new Question(
            "52. Comment récupérer les attributes d'une méthode via reflection ?",
            new[]
            {
                "a) method.Attributes()",
                "b) method.GetCustomAttributes()",
                "c) method.ReadAttributes()",
                "d) method.Meta()"
            },
            'b'
        ));

        qs.Add(new Question(
            "53. Quelle API reflection obtient le Type d'une instance `obj` ?",
            new[]
            {
                "a) typeof(obj)",
                "b) obj.type()",
                "c) obj.GetType()",
                "d) Type.of(obj)"
            },
            'c'
        ));

        qs.Add(new Question(
            "54. `dynamic` en C# signifie :",
            new[]
            {
                "a) Typage résolu à la compilation",
                "b) Résolution des membres à l'exécution (runtime binder)",
                "c) Identique à var",
                "d) Interdit en .NET"
            },
            'b'
        ));

        // ----------------------------
        // Design patterns (comme ton bloc)
        // ----------------------------
        qs.Add(new Question(
            "55. Un pattern qui retourne toujours la même instance :",
            new[]
            {
                "a) Singleton",
                "b) Factory",
                "c) Adapter",
                "d) Strategy"
            },
            'a'
        ));

        qs.Add(new Question(
            "56. Pattern qui crée des objets sans exposer la classe concrète :",
            new[]
            {
                "a) Abstract Factory",
                "b) Observer",
                "c) Visitor",
                "d) Iterator"
            },
            'a'
        ));

        qs.Add(new Question(
            "57. Pattern qui ajoute dynamiquement des fonctionnalités à un objet :",
            new[]
            {
                "a) Decorator",
                "b) Proxy",
                "c) Flyweight",
                "d) Memento"
            },
            'a'
        ));

        qs.Add(new Question(
            "58. Pattern où une chaîne de handlers traite/passe la requête :",
            new[]
            {
                "a) Chain of Responsibility",
                "b) Builder",
                "c) Prototype",
                "d) Template Method"
            },
            'a'
        ));

        qs.Add(new Question(
            "59. Pattern qui encapsule une requête/opération comme objet :",
            new[]
            {
                "a) Command",
                "b) Mediator",
                "c) Composite",
                "d) Facade"
            },
            'a'
        ));

        qs.Add(new Question(
            "60. Pattern pour réagir à des changements (publish/subscribe) :",
            new[]
            {
                "a) Observer",
                "b) Strategy",
                "c) Factory Method",
                "d) Adapter"
            },
            'a'
        ));

        qs.Add(new Question(
            "61. Pattern : encapsuler un algorithme interchangeable :",
            new[]
            {
                "a) Strategy",
                "b) Singleton",
                "c) Visitor",
                "d) Prototype"
            },
            'a'
        ));

        // ----------------------------
        // Tricky / pièges C#
        // ----------------------------
        qs.Add(new Question(
            "62. Quelle est la sortie ?\n`var a = new[]{1,2,3}; var b = a; b[0]=10; Console.WriteLine(a[0]);`",
            new[]
            {
                "a) 1",
                "b) 10",
                "c) Erreur",
                "d) 0"
            },
            'b'
        ));

        qs.Add(new Question(
            "63. Optional params : quand sont évaluées les valeurs par défaut ?",
            new[]
            {
                "a) À l'exécution à chaque appel",
                "b) À la compilation côté appelant",
                "c) À l'exécution côté appelé uniquement",
                "d) Jamais"
            },
            'b'
        ));

        qs.Add(new Question(
            "64. Closures : sortie ?\n`var fs=new List<Func<int>>(); for(int i=0;i<3;i++) fs.Add(()=>i); Console.WriteLine(string.Join(',', fs.Select(f=>f())));`",
            new[]
            {
                "a) 0,1,2",
                "b) 3,3,3",
                "c) 2,2,2",
                "d) Erreur"
            },
            'b'
        ));

        qs.Add(new Question(
            "65. Comment corriger le piège de capture dans un for ci-dessus ?",
            new[]
            {
                "a) Mettre `checked`",
                "b) Copier i dans une variable locale `var j=i; fs.Add(()=>j);`",
                "c) Utiliser `lock`",
                "d) Utiliser `unsafe`"
            },
            'b'
        ));

        qs.Add(new Question(
            "66. Quelle est la sortie ?\n`int x=0; void Incr(){ x++; } Incr(); Incr(); Console.WriteLine(x);`",
            new[]
            {
                "a) 0",
                "b) 1",
                "c) 2",
                "d) Erreur"
            },
            'c'
        ));

        qs.Add(new Question(
            "67. `==` sur string compare :",
            new[]
            {
                "a) les références",
                "b) le contenu (valeur) en C#",
                "c) toujours false",
                "d) uniquement la longueur"
            },
            'b'
        ));

        qs.Add(new Question(
            "68. Quelle différence entre `ReferenceEquals(a,b)` et `a==b` (string) ?",
            new[]
            {
                "a) Aucune",
                "b) ReferenceEquals compare référence, `==` compare contenu",
                "c) `==` compare référence, ReferenceEquals contenu",
                "d) ReferenceEquals est interdit"
            },
            'b'
        ));

        qs.Add(new Question(
            "69. Quelle est la sortie ? `Console.WriteLine( (object)1 == (object)1 );`",
            new[]
            {
                "a) True (valeur)",
                "b) False (référence) car boxing distinct",
                "c) Erreur",
                "d) Dépend du runtime"
            },
            'b'
        ));

        qs.Add(new Question(
            "70. `Enumerable.Range(1,3)` produit :",
            new[]
            {
                "a) 1,2,3",
                "b) 1,2",
                "c) 0,1,2",
                "d) 1,2,3,4"
            },
            'a'
        ));

        // ----------------------------
        // LINQ advanced / Grouping / Dictionary
        // ----------------------------
        qs.Add(new Question(
            "71. Quel est l'effet de `ToDictionary(k=>k.Id)` si des clés sont dupliquées ?",
            new[]
            {
                "a) La dernière écrase silencieusement",
                "b) Exception (ArgumentException)",
                "c) Les doublons sont ignorés",
                "d) Crée un Dictionary de listes automatiquement"
            },
            'b'
        ));

        qs.Add(new Question(
            "72. Quelle méthode LINQ permet de supprimer les doublons ?",
            new[]
            {
                "a) Unique()",
                "b) Distinct()",
                "c) DropDuplicates()",
                "d) RemoveDup()"
            },
            'b'
        ));

        qs.Add(new Question(
            "73. `SelectMany` est surtout utilisé pour :",
            new[]
            {
                "a) Trier",
                "b) Aplatir (flatten) une séquence de séquences",
                "c) Créer des dictionnaires",
                "d) Changer de thread"
            },
            'b'
        ));

        qs.Add(new Question(
            "74. Complexité moyenne de recherche dans Dictionary :",
            new[]
            {
                "a) O(1)",
                "b) O(log n)",
                "c) O(n)",
                "d) O(n log n)"
            },
            'a'
        ));

        // ----------------------------
        // Dates / immutabilité / parsing
        // ----------------------------
        qs.Add(new Question(
            "75. `DateTime` est :",
            new[]
            {
                "a) mutable",
                "b) immutable (struct valeur)",
                "c) une classe référence mutable",
                "d) un pointeur"
            },
            'b'
        ));

        qs.Add(new Question(
            "76. Parsing robuste invariant : quelle API ?",
            new[]
            {
                "a) DateTime.Parse(\"...\") sans culture",
                "b) DateTime.ParseExact(..., CultureInfo.InvariantCulture, ...)",
                "c) DateTime.Read(...)",
                "d) DateTime.FromString(...)"
            },
            'b'
        ));

        // ----------------------------
        // Pattern matching / switch
        // ----------------------------
        qs.Add(new Question(
            "77. Pattern matching : quel `switch` est valide ?",
            new[]
            {
                "a) switch(x) { case int n when n>0: ... }",
                "b) switch(x) { when int n>0: ... }",
                "c) switch { case x>0: ... }",
                "d) match(x) { case ... }"
            },
            'a'
        ));

        // ----------------------------
        // Span / perf / strings
        // ----------------------------
        qs.Add(new Question(
            "78. `string` concat dans une boucle : meilleur outil pour éviter trop d'allocations ?",
            new[]
            {
                "a) string + string",
                "b) StringBuilder",
                "c) Console.WriteLine",
                "d) Interpolated string uniquement"
            },
            'b'
        ));

        // ----------------------------
        // Threading basics
        // ----------------------------
        qs.Add(new Question(
            "79. `lock(obj)` sert à :",
            new[]
            {
                "a) Bloquer le GC",
                "b) Synchroniser l'accès concurrent (monitor)",
                "c) Rendre async plus rapide",
                "d) Garantir l'ordre LINQ"
            },
            'b'
        ));

        // ----------------------------
        // Equality / Hashing
        // ----------------------------
        qs.Add(new Question(
            "80. Pour utiliser un type comme clé de Dictionary, il faut surtout :",
            new[]
            {
                "a) Un ToString() unique",
                "b) Un Equals cohérent et un GetHashCode cohérent",
                "c) Un constructeur vide",
                "d) Être sealed"
            },
            'b'
        ));

        // ----------------------------
        // More expert questions (81..100)
        // ----------------------------
        qs.Add(new Question(
            "81. `using var f = ...;` (C# 8+) signifie :",
            new[]
            {
                "a) Dispose() à la fin du scope",
                "b) Dispose() immédiatement",
                "c) Jamais de Dispose()",
                "d) Dispose() seulement en release"
            },
            'a'
        ));

        qs.Add(new Question(
            "82. Quelle est la sortie ? `Console.WriteLine(0.1 + 0.2 == 0.3);`",
            new[]
            {
                "a) True",
                "b) False (précision flottante)",
                "c) Erreur",
                "d) Dépend du CPU"
            },
            'b'
        ));

        qs.Add(new Question(
            "83. Quelle API compare des doubles avec tolérance ?",
            new[]
            {
                "a) Math.Abs(a-b) < eps",
                "b) a == b",
                "c) a.Equals(b) toujours",
                "d) Double.CompareTo avec 0"
            },
            'a'
        ));

        qs.Add(new Question(
            "84. `checked` en C# :",
            new[]
            {
                "a) Désactive l'overflow",
                "b) Force une exception en cas d'overflow arithmétique",
                "c) Convertit en long automatiquement",
                "d) Optimise les divisions"
            },
            'b'
        ));

        qs.Add(new Question(
            "85. Différence entre `==` et `.Equals()` en général :",
            new[]
            {
                "a) `==` appelle toujours ReferenceEquals",
                "b) Dépend des surcharges, mais `.Equals` est la sémantique d'égalité logique typique",
                "c) `.Equals` compare toujours la référence",
                "d) Aucun des deux n'existe"
            },
            'b'
        ));

        qs.Add(new Question(
            "86. `HashSet<T>` est surtout utile pour :",
            new[]
            {
                "a) Préserver l'ordre",
                "b) Tester l'appartenance rapidement et unicité",
                "c) Faire des tris stables",
                "d) FIFO"
            },
            'b'
        ));

        qs.Add(new Question(
            "87. `Span<T>` est :",
            new[]
            {
                "a) Toujours sur le tas",
                "b) Une vue sur mémoire (stack/heap) pour éviter allocations, type ref struct",
                "c) Un wrapper LINQ",
                "d) Un type sérialisable JSON par défaut"
            },
            'b'
        ));

        qs.Add(new Question(
            "88. `Task.WhenAll(tasks)` :",
            new[]
            {
                "a) Attend la première tâche finie",
                "b) Attend toutes les tâches et agrège les exceptions",
                "c) Exécute les tâches séquentiellement",
                "d) Tue les tâches en retard"
            },
            'b'
        ));

        qs.Add(new Question(
            "89. LINQ : différence entre `Any()` et `Count()>0` ?",
            new[]
            {
                "a) `Any()` peut s'arrêter dès le premier élément (souvent plus efficace)",
                "b) `Count()>0` est toujours plus rapide",
                "c) `Any()` matérialise toujours",
                "d) Aucune"
            },
            'a'
        ));

        qs.Add(new Question(
            "90. Quelle est la sortie ?\n`var xs = Enumerable.Range(1,3).Select(x => { Console.Write(x); return x; }); Console.Write(\"-\"); xs.ToList();`",
            new[]
            {
                "a) 123-",
                "b) -123",
                "c) 1-23",
                "d) - (rien d'autre)"
            },
            'b'
        ));

        qs.Add(new Question(
            "91. `IQueryable<T>` vs `IEnumerable<T>` : différence clé ?",
            new[]
            {
                "a) IQueryable exécute toujours en mémoire",
                "b) IQueryable peut traduire l'expression (ex: SQL) via provider",
                "c) IEnumerable est pour bases de données uniquement",
                "d) Aucun"
            },
            'b'
        ));

        qs.Add(new Question(
            "92. `record` : l'égalité par défaut est :",
            new[]
            {
                "a) Par référence",
                "b) Par valeur (structure des composants)",
                "c) Désactivée",
                "d) Aléatoire"
            },
            'b'
        ));

        qs.Add(new Question(
            "93. `init` accessor (C# 9+) permet :",
            new[]
            {
                "a) D'assigner uniquement dans l'initialiseur/constructeur (immutabilité pratique)",
                "b) D'assigner uniquement en lecture",
                "c) D'assigner uniquement en private",
                "d) De bypasser le constructeur"
            },
            'a'
        ));

        qs.Add(new Question(
            "94. `ref` parameter signifie :",
            new[]
            {
                "a) Passage par valeur",
                "b) Passage par référence (lecture/écriture) et doit être initialisé avant l'appel",
                "c) Lecture seule",
                "d) Identique à out"
            },
            'b'
        ));

        qs.Add(new Question(
            "95. `out` parameter signifie :",
            new[]
            {
                "a) La variable doit être initialisée avant l'appel",
                "b) La méthode doit assigner la variable avant de retourner",
                "c) Il est en lecture seule",
                "d) Il empêche les exceptions"
            },
            'b'
        ));

        qs.Add(new Question(
            "96. `using System.Linq;` sert à :",
            new[]
            {
                "a) Activer le GC",
                "b) Importer les extensions LINQ (Where/Select/...)",
                "c) Activer async/await",
                "d) Déclarer des namespaces dynamiques"
            },
            'b'
        ));

        qs.Add(new Question(
            "97. Quelle méthode LINQ correspond le plus à un 'pivot' simple (regroupement par clé + projection) ?",
            new[]
            {
                "a) Zip",
                "b) GroupBy + ToDictionary/Select",
                "c) Concat",
                "d) Reverse"
            },
            'b'
        ));

        qs.Add(new Question(
            "98. Quelle est la sortie ? `Console.WriteLine(bool.Parse(\"False\"));`",
            new[]
            {
                "a) True",
                "b) False",
                "c) Erreur",
                "d) null"
            },
            'b'
        ));

        qs.Add(new Question(
            "99. Différence majeure entre `List<T>` et `Array` ?",
            new[]
            {
                "a) Array est redimensionnable, List non",
                "b) List est redimensionnable, Array a une taille fixe",
                "c) List est value-type",
                "d) Array ne supporte pas foreach"
            },
            'b'
        ));

        qs.Add(new Question(
            "100. Reflection : comment obtenir toutes les méthodes publiques d'un type `t` ?",
            new[]
            {
                "a) t.Methods",
                "b) t.GetMethods()",
                "c) t.ReadMethods()",
                "d) t.PublicMethods()"
            },
            'b'
        ));

        return qs;
    }
}
