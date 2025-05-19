 # syllabus

Updated Exam Syllabus for Python and Django

1. Python Programming Fundamentals

# Python Basics:
## Variables, data types, print.
## Loops (for, while), conditionals (if-else).
Example: Print “Hello” 5 times, check if number is even.

### Lists, Tuples, Sets:
Lists: Create, access (e.g., ["apple", "banana"]).
Tuples: Immutable (e.g., (1, 2)).
Sets: Unique elements (e.g., {1, 2, 3}).
### Functions:
Define/call functions (e.g., def add(a, b): return a + b).
File Input/Output:
Read/write files with try/except (e.g., open("file.txt", "r")).

### 2. Object-Oriented Programming & Analysis
Requirement Analysis:
List class, attributes, methods from a scenario (e.g., Library → Book: title, borrow).
Classes and Objects:
Create/use classes (e.g., class Dog: def bark(self): print("Woof")).
Inheritance:
Parent-child classes with abstract methods (e.g., Animal, Cat).

Abstract Base Classes:

Use ABC, @abstractmethod (e.g., Shape with area).
Access Modifiers:

Public, private (__attribute), protected (_attribute).
Class Diagrams:

Draw class with attributes, methods (e.g., “Student”: name, study).

3. Web Development Basics

HTML:
Table, form, list, button, radio-button, colspan, rowspan.

Example: 2x2 table, form with text input.

CSS:

Text color, font-size (e.g., p {color: blue; font-size: 16px;}).

4. Django Framework Essentials
Django Architecture:
MVT: Model (data), View (logic), Template (webpage).
Example: URL → View → Model → Template flow.
URLs and Views:
Map URLs (e.g., path('posts/', views.post_list)).
Views to list/process data (e.g., Post.objects.all()).
Django Superuser:
Create: python manage.py createsuperuser.
Use: Manage data via /admin.
Models and Admin CRUD:
Models: Define data (e.g., Post: title, content).
Admin: Register models (e.g., admin.site.register(Post)).
CRUD: Create, read, update, delete.
Django Forms – Create:


# Forms to add data (e.g., <form method="post">{% csrf_token %}<input type="text">).
View to save (e.g., Post(title=request.POST['title']).save()).
Django Forms – Update & Delete:
Update: Edit data via forms (e.g., pre-filled form).
Delete: Remove data (e.g., Post.objects.get(id=1).delete()).
Media Handling in Django:
Model: ImageField (e.g., photo = models.ImageField(upload_to='images/')).
Settings: MEDIA_URL, MEDIA_ROOT.

Form: File upload (e.g., <form enctype="multipart/form-data">).

5. Previous Year Questions

Solve Python, OOP, HTML, CSS, Django questions from shared materials.

Resources: Classroom notes, lab exercises, shared materials.
Practice: Write code/diagrams by hand.
Focus: Python/HTML for easy marks, OOP/Django for high marks.
