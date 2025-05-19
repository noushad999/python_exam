1. Python Programming Fundamentals (33% - ~4.5 hours)

Basics (1 hour)

What to Learn: Variables (int, float, str), data types, input/output (input(), print()), control structures (if-else, nested if, loops: for, while).
Key Concepts: Conditional logic (e.g., leap year check), loop patterns (e.g., number pyramids).
Examples:

Leap year: if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): print("Leap year")
Pattern: for i in range(1, 6): print("* " * i)


Practice: Write a program to check if a number is positive/negative and print a pattern.


Lists/Tuples/Sets (1 hour)

What to Learn: List operations (indexing, slicing, append, remove), finding max/min, duplicates; tuple conversion; set basics (unique elements).
Key Concepts: List comprehension, tuple immutability, set difference.
Examples:

Find duplicates: def find_duplicates(lst): return list(set([x for x in lst if lst.count(x) > 1]))
List to tuple: tuple_lst = tuple([1, 2, 3])


Practice: Find the highest absolute value in a list, convert a list to a tuple and calculate average.


Functions (1 hour)

What to Learn: Define functions with parameters, return values, mathematical operations (e.g., sum of series, perfect square).
Key Concepts: Default arguments, lambda functions.
Examples:

Series sum: def series_sum(n): return sum(3 * i + 1 for i in range(n))
Lambda: add = lambda x, y: x + y


Practice: Write a function to sum odd numbers in a list, use lambda for multiplication.


File I/O (1 hour)

What to Learn: Open/read/write files (open(), read(), write(), append), error handling with try/except.
Key Concepts: Append mode ('a'), filtering data from files.
Examples:

Write: with open('output.txt', 'a') as f: f.write('Data\n')
Read filter: with open('grades.txt') as f: names = [line.split()[0] for line in f if int(line.split()[1]) > 70]


Practice: Read a file of student grades, write names with grades > 80 to a new file.


Mathematical Functions (0.5 hours)

What to Learn: Implement functions for series, factorials, or statistical calculations.
Key Concepts: Loops for summation, recursive thinking.
Examples: def factorial(n): return 1 if n == 0 else n * factorial(n-1)
Practice: Calculate the sum of a series like <math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>7</mn><mo>+</mo><mo>…</mo><mo>+</mo><mi>n</mi></mrow><annotation encoding="application/x-tex">1 + 4 + 7 + \ldots + n</annotation></semantics></math>.



2. Object-Oriented Programming & Analysis (27% - ~3.5 hours)

Classes/Objects (1 hour)

What to Learn: Define classes, attributes, methods, constructors (__init__), instance methods.
Key Concepts: Object creation, method calls.
Examples:

class Rectangle: def __init__(self, length, width): self.length = length; self.width = width


Practice: Create a Student class with name and grade, add a method to display info.


Inheritance (1 hour)

What to Learn: Subclassing, method overriding, super() for parent access.
Key Concepts: Inheritance hierarchy, polymorphism.
Examples:

class Car(Vehicle): def __init__(self, color): super().__init__("ModelX", 2020); self.color = color


Practice: Create a Dog class inheriting from Animal, override a method.


Abstract Classes (0.5 hours)

What to Learn: Define abstract classes (using ABC, abstractmethod), differentiate from regular classes.
Key Concepts: Abstract methods, real-life examples (e.g., Mobile device).
Examples:

from abc import ABC, abstractmethod; class Mobile(ABC): @abstractmethod def camera(): pass


Practice: Explain with an example (e.g., Vehicle vs. Car).


Class Diagrams (1 hour)

What to Learn: Draw UML diagrams for inheritance, association.
Key Concepts: Boxes for classes, arrows for relationships.
Examples: Diagram for Animal → Dog with attributes/methods.
Practice: Draw a diagram for Shape → Circle with area method.



3. Web Development Basics (10% - ~1.5 hours)

HTML (1 hour)

What to Learn: Structure (tags: <html>, <head>, <body>), tables (<table>, <tr>, <td>), images (<img>).
Key Concepts: Nesting tags, attribute usage (e.g., src, alt).
Examples:

<table><tr><td>Name</td><td>Alice</td></tr></table>


Practice: Create a table with 2 columns and 3 rows.


CSS (0.5 hours)

What to Learn: Inline/block styling, properties (border, color, font-size, text-align).
Key Concepts: Selectors, basic styling.
Examples:

<style> table { border: 1px solid black; }</style>


Practice: Style a table with border and background color.



4. Django Framework Essentials (25% - ~3.5 hours)

Architecture (0.5 hours)

What to Learn: MVT pattern (Model, View, Template), directory structure.
Key Concepts: Flow of request/response.
Examples: Diagram showing URL → View → Template.
Practice: Explain with a diagram.


URLs/Views (1 hour)

What to Learn: Define URL patterns (urls.py), create views (views.py).
Key Concepts: URL routing, view functions.
Examples:

path('', views.home, name='home')
def home(request): return render(request, 'home.html')


Practice: Write a URL and view for a welcome page.


Superuser (0.5 hours)

What to Learn: Create superuser (createsuperuser), access admin panel.
Key Concepts: Admin login, user management.
Examples: python manage.py createsuperuser
Practice: Write the command and explain its use.


Models/Admin CRUD (1 hour)

What to Learn: Define models (models.py), register in admin (admin.py).
Key Concepts: Field types (CharField, IntegerField), CRUD basics.
Examples:

class Book(models.Model): title = models.CharField(max_length=100)


Practice: Create a Student model and register it.


Forms (0.5 hours)

What to Learn: Basic form handling (create, process input).
Key Concepts: Form validation, template integration.
Examples: from django import forms; class NameForm(forms.Form): name = forms.CharField()
Practice: Write a simple form for name input.



5. Previous Year Questions & Theory/Diagrams (18% - ~1.5 hours)

Previous Year Questions (1 hour)

What to Learn: Review Q1–Q8 from analysis (e.g., leap year, file I/O, model design).
Key Concepts: Identify recurring themes (File I/O, Inheritance).
Practice: Re-solve selected questions.


Theory/Diagrams (0.5 hours)

What to Learn: Explain Django components (e.g., Admin, URLs), draw class diagrams.
Key Concepts: Role of components, UML basics.
Examples: Explain Admin panel, draw Animal → Dog.
Practice: Write a theory on URLs/Views, draw a diagram.
