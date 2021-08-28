# Py VRB Compiler

<p align="center">
<img src="https://www.python.org/static/img/python-logo-large.c36dccadd999.png?1576869008" width="100px">
<h3 align="center">Python VRB Compiler</h3>

---

### About

The VRB Script Language (VRBS) is a oldschool function based programming language created with Pyhton. This language has only one format to type code: Function (Callable) formats. Check the example bellow:

VRBS Fibonacci
```vrbs
int(x,1)
int(y,1)
int(z,0)
label(loop)
    output_ln($x)
    calc($x,+,$y,z)
    parse_int($z,z)
    var(x,$y)
    var(y,$z)
if($x,<,100,loop)
```

Output
```txt
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
```
