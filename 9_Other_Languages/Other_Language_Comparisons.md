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

### C++

- Single line: `// comment`
- Multi-line: `/* comment */`

### Java

- Single line: `// comment`
- Multi-line: `/* comment */`

### C#

- Single line: `// comment`
- Multi-line: `/* comment */`

## Data Types

### Python

- Dynamically typed: Types are inferred at runtime.
- Basic types: `int`, `float`, `str`, `bool`, `list`, `dict`, etc.
- No fixed sizes; depends on implementation.

### C++

- Statically typed with fixed sizes (may vary by platform/compiler).
- Basic types:
  - `bool`: 1 byte (true/false)
  - `char`: 1 byte (single character/ASCII)
  - `int`: 2 or 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Strings: `std::string` (variable size)

### Java

- Statically typed with fixed sizes.
- Primitive types:
  - `boolean`: 1 byte (true/false)
  - `char`: 2 bytes (Unicode character)
  - `int`: 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Reference types: `String`, arrays, objects.

### C#

- Statically typed with fixed sizes.
- Basic types:
  - `bool`: 1 byte (true/false)
  - `char`: 2 bytes (Unicode character)
  - `int`: 4 bytes (whole numbers)
  - `float`: 4 bytes (6-7 decimal digits)
  - `double`: 8 bytes (15 decimal digits)
- Strings: `string` (reference type)

## Variables

### Python

- Dynamically typed: No need to declare type explicitly.
- Example: `x = 5` or `name = "Hello"`

### C++

- Statically typed: Must declare type.
- Example: `int x = 5;` or `std::string name = "Hello";`
- Supports const: `const int y = 10;`

### Java

- Statically typed: Must declare type.
- Example: `int x = 5;` or `String name = "Hello";`
- Primitive types and reference types.

### C#

- Statically typed: Must declare type.
- Example: `int x = 5;` or `string name = "Hello";`
- Supports var for implicit typing: `var x = 5;`

## Functions

### Python

- Defined with `def` keyword.
- No return type declaration.
- Example:

```python
def greet(name):
    return f"Hello, {name}!"
```

### C++

- Must specify return type and parameter types.
- Example:

```cpp
std::string greet(std::string name) {
    return "Hello, " + name + "!";
}
```

### Java

- Must specify return type and parameter types.
- Belong to classes (methods).
- Example:

```java
public String greet(String name) {
    return "Hello, " + name + "!";
}
```

### C#

- Must specify return type and parameter types.
- Can be static or instance methods.
- Example:

```csharp
public string Greet(string name) {
    return $"Hello, {name}!";
}
```

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
