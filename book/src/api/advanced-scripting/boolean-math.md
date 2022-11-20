# Boolean Math

The *Boolean Math* node gives access to common boolean operations, such as `AND`, `NOT`, `XOR`, etc.

However, it can be cumbersome to use the `boolean_math` function in complex boolean expressions.

```python
# Check if the two values equal, or if the first is true.
x = False
y = True
return boolean_math(
    operation=BooleanMath.Operation.OR
    boolean=(
        boolean_math(
            operation=BooleanMath.Operation.XNOR # Equal
            boolean=(x, y)
        ),
        x
    )
)
```

A few operators are available to make boolean math easier and more readable.

```python
# Check if the two values equal, or if the first is true.
x = False
y = True
return (x == y) | x
```

The operators available are:

* `==` - `XNOR`
* `!=` - `XOR`
* `|` - `OR`
* `&` - `AND`
* `~` - `NOT`

> You *cannot* use the built-in Python keywords `and`, `or`, and `not`. You must use the custom operators above to create *Boolean Math* nodes.