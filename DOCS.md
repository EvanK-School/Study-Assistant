# Documentation
### 1. Definition Functions

```python
choice(mydic, string, num=4)
```

**Choice** is a function for creating a multiple-choice question, and taking input.  
**Choice** has three arguments:
1. `mydic`  - The dictionary containing the terms as indices, and their definitions.
2. `string` - The string that will be asked to be defined.
3. `num`    - The optional argument for the number of possibles answers (defaulting to 4, and where `2 < num < 26`).

---

```python
impdoc(name, doctype=<*>)
```

**Impdoc** is a function for importing different types of documents for use by Study Assistant.
**Impdoc** has two arguments:
1. `name`    - The string that is the name of the document. Easy to understand
2. `doctype` - An optional argument that changes based on the file **impdoc** is imported from - it can be a specific type or `'auto'`matic.

### 2. File Specifications

1. First line must be `[//]: # ({'type': <type>})`
    - This is used by the file reader/importer to determine document type.

### 3. Separate Markup Documents

Feature has not been added yet.
