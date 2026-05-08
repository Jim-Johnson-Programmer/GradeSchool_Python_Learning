# Language Comparisons: Variables, Functions, and Classes

This document compares the implementation of variables, functions, and classes across Python (interpreted), C++, Java, and C# (compiled languages).

## Language Domains

Different programming languages are often chosen based on their strengths for specific computing domains:

- **Back-end Computing**: Languages like Java, C#, and C++ are commonly used for server-side applications, enterprise systems, and high-performance computing due to their strong typing, performance, and scalability.
- **Databases**: SQL is the standard language for querying and managing relational databases, while languages like Python and JavaScript are used for NoSQL databases and data processing.
- **GUI Interfaces**: Languages such as JavaScript (with frameworks like React), C# (with WPF or WinForms), and Java (with Swing or JavaFX) are popular for building graphical user interfaces.
- **Admin/DevOps Processing**: Scripting languages like Python, Bash, and PowerShell, along with configuration languages like YAML, are frequently used for automation, system administration, and DevOps tasks due to their ease of use and rapid development capabilities.

## Comments

### Python

- Single line: `# comment`
- Multi-line: `""" comment """`

[W3Schools Python Comments](https://www.w3schools.com/python/python_comments.asp)

### C++

- Single line: `// comment`
- Multi-line: `/* comment */`

[W3Schools C++ Comments](https://www.w3schools.com/cpp/cpp_comments.asp)

### Java

- Single line: `// comment`
- Multi-line: `/* comment */`

[W3Schools Java Comments](https://www.w3schools.com/java/java_comments.asp)

### C#

- Single line: `// comment`
- Multi-line: `/* comment */`

[W3Schools C# Comments](https://www.w3schools.com/cs/cs_comments.php)

## Data Types

### Python

- Dynamically typed: Types are inferred at runtime.
- Basic types: `int`, `float`, `str`, `bool`, `list`, `dict`, etc.
- No fixed sizes; depends on implementation.

[W3Schools Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

### C++

- Statically typed with fixed sizes (may vary by platform/compiler).
- Basic types:
  - `bool`: 1 byte (true/false)
  - `char`: 1 byte (single character/ASCII)
  - `int`: 2 or 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Strings: `std::string` (variable size)

[W3Schools C++ Data Types](https://www.w3schools.com/cpp/cpp_data_types.asp)

### Java

- Statically typed with fixed sizes.
- Primitive types:
  - `boolean`: 1 byte (true/false)
  - `char`: 2 bytes (Unicode character)
  - `int`: 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Reference types: `String`, arrays, objects.

[W3Schools Java Data Types](https://www.w3schools.com/java/java_data_types.asp)

### C#

- Statically typed with fixed sizes.
- Basic types:
  - `bool`: 1 byte (true/false)
  - `char`: 2 bytes (Unicode character)
  - `int`: 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Strings: `string` (reference type)

[W3Schools C# Data Types](https://www.w3schools.com/cs/cs_data_types.php)

## Variables

### Python

- Dynamically typed: No need to declare type explicitly.
- Example: `x = 5` or `name = "Hello"`

[W3Schools Python Variables](https://www.w3schools.com/python/python_variables.asp)

### C++

- Statically typed: Must declare type.
- Example: `int x = 5;` or `std::string name = "Hello";`
- Supports const: `const int y = 10;`

[W3Schools C++ Variables](https://www.w3schools.com/cpp/cpp_variables.asp)

### Java

- Statically typed: Must declare type.
- Example: `int x = 5;` or `String name = "Hello";`
- Primitive types and reference types.

[W3Schools Java Variables](https://www.w3schools.com/java/java_variables.asp)

### C#

- Statically typed: Must declare type.
- Example: `int x = 5;` or `string name = "Hello";`
- Supports var for implicit typing: `var x = 5;`

[W3Schools C# Variables](https://www.w3schools.com/cs/cs_variables.php)

## Functions

### Python

- Defined with `def` keyword.
- No return type declaration.
- Example:

```python
def greet(name):
    return f"Hello, {name}!"
```

[W3Schools Python Functions](https://www.w3schools.com/python/python_functions.asp)

### C++

- Must specify return type and parameter types.
- Example:

```cpp
std::string greet(std::string name) {
    return "Hello, " + name + "!";
}
```

[W3Schools C++ Functions](https://www.w3schools.com/cpp/cpp_functions.asp)

### Java

- Must specify return type and parameter types.
- Belong to classes (methods).
- Example:

```java
public String greet(String name) {
    return "Hello, " + name + "!";
}
```

[W3Schools Java Methods](https://www.w3schools.com/java/java_methods.asp)

### C#

- Must specify return type and parameter types.
- Can be static or instance methods.
- Example:

```csharp
public string Greet(string name) {
    return $"Hello, {name}!";
}
```

[W3Schools C# Methods](https://www.w3schools.com/cs/cs_methods.php)

## Classes

### Python

- No access modifiers.
- Methods defined with `def`.
- Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}!"
```

[W3Schools Python Classes](https://www.w3schools.com/python/python_classes.asp)

### C++

- Access modifiers: public, private, protected.
- Constructor and destructor.
- Example:

```cpp
class Person {
private:
    std::string name;
public:
    Person(std::string n) : name(n) {}
    std::string greet() {
        return "Hello, I'm " + name + "!";
    }
};
```

[W3Schools C++ Classes](https://www.w3schools.com/cpp/cpp_classes.asp)

### Java

- Access modifiers: public, private, protected.
- Constructor required for initialization.
- Example:

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String greet() {
        return "Hello, I'm " + name + "!";
    }
}
```

[W3Schools Java Classes](https://www.w3schools.com/java/java_classes.asp)

### C#

- Access modifiers: public, private, protected, internal.
- Properties with getters/setters.
- Example:

```csharp
public class Person {
    public string Name { get; set; }

    public Person(string name) {
        Name = name;
    }

    public string Greet() {
        return $"Hello, I'm {Name}!";
    }
}
```

[W3Schools C# Classes](https://www.w3schools.com/cs/cs_classes.php)
