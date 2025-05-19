
# ✅ Python, OOP, Web & Django – Exam Preparation Checklist (Target: Pass)

> ⏱️ **Time Left**: \~18 Hours
> 🎯 **Target Score**: Pass
> 🧑‍💻 **Level**: Beginner
> 📚 **Sources**: Classroom Notes, Lab Sheets, Previous Year Questions

---

## 1. 🐍 Python Programming Fundamentals

### 🔹 Python Basics

* [ ] Variables, data types, `print()`
* [ ] Loops: `for`, `while`
* [ ] Conditionals: `if-else`
* [ ] Practice: `text[::-1]` (reverse string)

### 🔹 Lists, Tuples, Sets

* [ ] Create and access lists (e.g., `["apple", "banana"]`)
* [ ] Tuples (immutable, e.g., `(1, 2)`)
* [ ] Sets (unique elements, e.g., `{1, 2, 3}`)
* [ ] Focus: Add items, basic list operations
* ❌ No dictionaries in syllabus

### 🔹 Functions

* [ ] Define/call functions (`def add(a, b): return a + b`)
* [ ] Practice: Function to return square of a number

### 🔹 File Input/Output

* [ ] Read from file using `open("file.txt", "r")`
* [ ] Write to file, handle exceptions using `try/except`

---

## 2. ⚙️ Object-Oriented Programming & Analysis

### 🔹 Requirement Analysis

* [ ] Identify classes, attributes, and methods from a scenario
* [ ] Practice: Library → Book → title, borrow()

### 🔹 Classes and Objects

* [ ] Define class with attributes and methods
* [ ] Example:

```python
class Dog:
    def bark(self):
        print("Woof")
```

### 🔹 Inheritance & Abstract Base Class

* [ ] Write parent-child class with `@abstractmethod`
* [ ] Use ABC module:

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

### 🔹 Access Modifiers

* [ ] Use public, protected (`_attr`), private (`__attr`)
* [ ] Practice getter methods

### 🔹 Class Diagrams

* [ ] Draw class diagram with attributes/methods
* [ ] Practice from real-world scenarios

---

## 3. 🌐 Web Development Basics

### 🔹 HTML

* [ ] Write table:

```html
<table>
  <tr><td>1</td></tr>
</table>
```

* [ ] Create forms with input, radio, button
* [ ] Use `colspan`, `rowspan` in tables
* [ ] Lists: ordered & unordered

### 🔹 CSS

* [ ] Style with color and font-size

```css
p {
  color: blue;
  font-size: 16px;
}
```

---

## 4. 🚀 Django Framework Essentials

### 🔹 Django Architecture (MVT)

* [ ] Explain MVT pattern
* [ ] Draw request flow: `URL → View → Model → Template`

### 🔹 URLs and Views

* [ ] Map URL: `path('posts/', views.post_list)`
* [ ] View with: `Post.objects.all()`
* [ ] Practice writing basic View & URL

### 🔹 Django Superuser

* [ ] Create with:

```bash
python manage.py createsuperuser
```

* [ ] Access and use `/admin`

### 🔹 Models and Admin CRUD

* [ ] Define model with `title`, `content`
* [ ] Register in admin using `admin.site.register()`
* [ ] Perform CRUD via admin panel

### 🔹 Django Forms – Create

* [ ] Basic HTML Form:

```html
<form method="post">
  {% csrf_token %}
  <input type="text" name="title">
</form>
```

* [ ] Save using:

```python
Post(title=request.POST['title']).save()
```

### 🔹 Django Forms – Update & Delete

* [ ] Edit data using pre-filled forms
* [ ] Delete using:

```python
Post.objects.get(id=1).delete()
```

### 🔹 Media Handling

* [ ] Model with `ImageField`:

```python
photo = models.ImageField(upload_to='images/')
```

* [ ] Configure `MEDIA_URL`, `MEDIA_ROOT` in `settings.py`
* [ ] Use `enctype="multipart/form-data"` in form
* [ ] View for handling file upload

---

## 5. 📜 Previous Year Questions

* [ ] Practice 3–4 sample questions:

  * [ ] Write a Model
  * [ ] Create a Table in HTML
  * [ ] Simple Python Function
  * [ ] Form handling in Django

---

## 📌 Exam Strategy

* ✅ **First Attempt**: Python & HTML (easy marks)
* 🎯 **High Focus**: OOP & Django (core marks)
* ✍️ **Practice by Hand**: Code, diagrams
* 🤝 **Group Support**: Ask peers for examples
* 📚 **Final Revision**: Lab/class notes, shared materials

---

## 📁 Recommended Resources

* Class slides and lab sheets
* Previous year papers
* Your group messages (for Django/media/form help)
