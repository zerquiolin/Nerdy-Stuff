# Big O

Language used for talking about how much and algorithm takes to run. We can compare two different algorithms with Big O to see which one is better, which one has better performance.

As the number of elements increases the number of operations which affects performance directly also increases.

Big O allows us to know how much operations are made inside an algorithm.

## Complexity

![BigO_Complexity](../Data%20Estructures/BigO%20Complexity.png)

## Notations

### O(1) - Constant Time

Only runs one process, no matter how much elements are taken in, we are only doing one thing.

### O(n) - Linear Time

It runs an operation over each element, making it processes always be the same as the elements (inputs).

## Rules Book

We can get different O Notations based on the algorithm, for example:

```typescript
const funChallenge(input){
    let a = 10; // O(1)

    for (let i = 0; i < array.length; i++) { // O(n)
        anotherFunction(); // O(n)
        a++; // O(n)
    }

    return a; // O(1)
}
```

For this specific function we will get the notation:

    O(2 + 3n)

As you see the notation gets harder to read as the function's complexity increases, so there are some simple rules in order to simplify the notation and its readibility.

### Worst Case

Big O only cares for the worst case, meaning the algorithm will run the n possible times.

### Remove Constants

By removing all the constants we only focus on whats showing on the charts, meaning we only care on the algorithm's decrease of efficiency.

### Different Terms for Inputs

```typescript
function compressBoxesTwice(boxes, boxes2) {
  boxes.array.forEach((box) => {
    console.log(box);
  });
  boxes2.array.forEach((box) => {
    console.log(box);
  });
}
```

As we can see in this example, we might say the _Time Complexity_ is **O(n)** since we hace two loops which both share the _O(n) Linear Time_, but it is actually wrong, because of "Different Terms for Inputs" rule, we have to specify the _Time Complexity_ for both of the elements(inputs).

Which the _Time Complexity_ of the example above will be:

    O(n + m)

Meaning both _n_ & _m_ refers to linear time.

### Drop Non Dominants

# Data Structures

## What Are Data Structures?

Data structure is a data organization, management, and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.
