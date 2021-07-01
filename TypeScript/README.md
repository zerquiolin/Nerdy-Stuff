# **_TypeScript_**

## **_Introduction_**

<br> <br>

### **~ How To Install**

<br> <br>

1. **_Global_**

   - **npm** install -g typescript

2. **_Local_** (Inside the proyect)

   - **npm** install typescript
     <br> <br>

### **~ How To Compile**

<br> <br>

1. **_Single Check_**

   - tsc **filename.ts**

2. **_Watch Mode_**

   - tsc **filename.tsc** -w
     <br>
     -w stands for "watch"
     <br> <br>

### **~ TypeScript Configuration**

<br> <br>

1.  Creating a JSON file:

        tsconfig.json

2.  Adding an object

    ```json
    {
      "CompilerOptions": {
        "rootDir": "./src",
        "outDir": "./build"
      }
    }
    ```

    - _rootDir:_ Contains the path where the .ts files are located.
    - _outDir:_ Contains the path where the compiler is going to create de .js files after transpiling them.

<br> <br>

## **Funciontality**

<br> <br>

### **~ Basic Types**

<br> <br>

    Once a variable is assign with a type, it can not longer recieve values from other types.

Our basic types are:

1.  boolean
2.  number
3.  string
4.  array
5.  tuple
6.  enum
7.  unknown
8.  any
9.  void
10. null & undefined
11. never
12. object
13. symbol
14. null
15. undefined

And much more!
<br> <br>

### **~ How To Set Types**

<br> <br>

Add a colon and it's type after the variable name.
<br> <br>

**_: string_** <br>
**_: number_** <br>
**_: boolean_** <br>
<br>

```typescript
const author: string = "zerquiolin";
const age: number = 18;
const isPro: boolean = true;
```

<br>

### **~ Type Inference**

<br> <br>

A variable infers what type is asigned, once it is initialized.

```typescript
let title = "TypeScript"; // Inferred string type
let year = 2021; // Inferred number type
let isCurrent = true; // Inferred boolean type
```

<br>

### **~ Union Type**

<br> <br>

Defines that a variable could contain more than one type.
<br>

To specify you'll be using different types, you have to use a vertical pipe **|** symbol:

```typescript
let random: number | string;
```

Once we declare our variable can be multiple types, we can asign values.

```typescript
random = 1; // Correct!
random = "hey!"; // Correct!
```

<br>

This not only works with types, we can implement the selected values we want:

```typescript
let fruit: "Apple" | "Banana" | "watermelon";
fruit = "Apple"; // Correct!
fruit = "Banana"; // Correct!
```

<br>

_Now, how can we know what type is currently on the variable?_

_~ With *typeof* we'll get what type if currently in our variable._

```typescript
typeof random = // Returns the actual type inside the variable.

if( typeof random === 'number' ) {
    // CODE
}
```

<br>

### **~ Arrays**

<br> <br>

You can declare a basic array, by setting its type and square brackets:

```typescript
const arrayOfStrings: string[] = ["hello", "there"];
```

You can also use a different sytnax:

```typescript
const anotherArrayOfStrings: Array<string> = ["hello", "there"];
```

There is not a difference between any of both, it's more a syntactical preference.

Another Example:

```typescript
const arrayOfNumbers: number[] = [1, 2, 3, 4, 5];
```

<br>

_Now, how can we set an array to accept more than one type?_

_~ By using unions!_

```typescript
const arrayOfStringsAndNumbers: (number | string)[] = [
  1,
  2,
  3,
  "hello",
  "there",
];
```

<br> <br>

### **~ Tuples**

<br> <br>

A tuple is very similar to arrays, the difference is, we have more control over the content.

It works by declaring and array of types in the order you want the content to be:

```typescript
const myTuple: [string, number, string, number, string, number] = [
  "one",
  1,
  "two",
  2,
  "three",
  3,
];
```

If any of the elements dont follow the given structure, TypeScript will not allow it.<br>
_(The lenght of the given array of types could be whatever you want)_
<br> <br>

### **~ Any**

<br> <br>

**Any** is a special type, which tells the TypeScript compiler that our value can be any type.

~ we should one be using **any** as our last resorce or for debbuging purposes!<br>

```typescript
let anyValue: any;
anyValue = 1; // Correct!
anyValue = "Hello There"; // Correct!
anyValue = true; // Correct!
```

As we are using **any**, we lost the _Strong Typing behaviour_ TypeScript provides us, and without it, the compiler completely ignores any type checking, that means we can call a function inside the variable that doesnt exits and still be accepted.
<br> <br>

### **~ Unknown**

<br> <br>
**Unknown** is very similar to any, but is known as the _"safer"_ version.

~ we should one be using **unknown** as our last resorce or for debbuging purposes!<br>

<br>

As we tried to called a function that doesnt exits inside a value on an any type variable, it made its way though the TypeScript compiler with no errors.
This situation will not happen with the **unknown** type, as well as not allowing a non unknown type variable to set himself to a value from an unknown type one.

```typescript
let unknownValue: unknown;
anyValue = 1; // Correct!
anyValue = "Hello There"; // Correct!
anyValue = true; // Correct!
```

<br>

### **~ Null & Undefined**

<br> <br>

**Null** is used when a value is explicitly empty.

```typescript
let nullVariable: null = null;
```

**Undefined** is used when ia value is just to be determined.

```typescript
let undefinedVariable: undefined;
```

    ~ doesnt have to be asign!

This core types are inmutable, this means, we could never change their values, so they will remain that way.

We could use this types just when we dont must to set a value to a variable.
<br> <br>

### **~ Enums**

<br> <br>

Used for cleaner code base, made for a more developer friendly eyes and more readable switch statements.

<br>

_How can we declare an enum?_

```typescript
enum coffeType {
  Americano,
  Cappucino,
  Frappucino,
  Espresso,
  Mocha,
}
```

_How can we assign an enum option?_

```typescript
const myfavoriteCoffeType: coffeType = coffeType.Americano;
```

    ~ Notice we assign the type as the enum!
    ~ This assign returns the index of the enum option!

_Can we set values to the enum options?_

```typescript
enum elementType {
  Fire = "red",
  Water = "blue",
  Wind = "grey",
  Earth = "brown",
}
```

_How can we assign those values?_

```typescript
const myfavoriteElementColor: elementType = elementType.Fire;
```

    ~ Notice we assign the type as the enum!
    ~ This assign returns the values of the enum opcion!

<br>

### **~ Functions**

<br> <br>

There is not such a mystery behind functions, what we could do is refactor our JavaScript functions into a safer version with TypeScript.

_JavaScript:_

```javascript
const combineTwoStrings = (StringA, StringB) => {
  return StringA + StringB;
};
```

_TypeScript:_

```typescript
const combineTwoStrings = (StringA: string, StringB: string): string => {
  return StringA + StringB;
};
```

    ~ Notice we added types to the parameters of the function as well as the function itself to ensure the correct values are gathered and returned!

<br>

### **~ Interface**

<br> <br>

Works as blueprints or shapes for an object!

_How an interface is defined?_

```typescript
interface bakeryItem {
  name: string;
  numberInStock: number;
  ingredients: string[];
  rating?: number;
}
```

    ~ When a '?' is placed after the variable name, it's telling the compiler it will not necessarily needs to be a value inside that variable.

_How can we assign our interface?_

```typescript
const myBakeryItem: bakeryItem = {
  name: "Red Velvet Cake",
  numberInStock: 1,
  ingredients: ["eggs", "milk", "sugar", "flour", "food colouring"],
};
```

    ~ Notice we didn't use the 'rating' variable, just as we define the variable as an optional variable it will not generate errors and the compiler will accept it.

If we dont assign the properties of the objects just as we declare them on the interface, the compiler will throw an error.

<br>

#### **_~ Extends_**

<br>

To extend an interface we should implement the keyword _'extends'_ and then the interface we want to extend of.

```typescript
interface brand {
  name: string;
}

interface device extends brand {
  model: string;
}
```

Now the interface 'device', have the property 'name' from 'brand'.

<br>

#### **_~ Merge_**

<br>

_Interface_ has a particular behaviour, when we declare and _Interface_ more than once with the same name, the compiler will interprete the _Interface_ it's extending to itself, this means, each time we declare an _Interface_ with the same exact name, they are going to merge and act as single one.

<br>

_Having this:_

```typescript
interface keyboard {
  brand: string;
}

interface keyboard {
  model: string;
}

interface keyboard {
  price: number;
}
```

_Is the same as:_

```typescript
interface keyboard {
  brand: string;
  model: string;
  price: number;
}
```

<br> <br>

### **~ Literal Types**

<br> <br>

In this ocation, _Type_ works just as _Interfaces_ does, they are practically the same, the difference is the syntactical structure and implementation!

<br>

_Which one should I use?_ <br>
_~ Apart from a syntactical preference, type is used when definning customized types that are easier to read and understand!_

Example:

```typescript
// Definning our custom type!
type itemPriceType = string | number;

// Asignin our custom type!
let myItem: itemPriceType = "999";
myItem = 999;
```

<br>

_How a type is defined?_

Instead of declaring the 'blueprint' by just defining the content inside the brackets, we also have to set the object to the _type_, by an equal '=' sign.

```typescript
type typeBrand = {
  name: string;
};
```

<br>

#### **~ Extends**

<br>

Instead of using the keyword _'extends'_, after the pair of brackets we should use _'&'_ sign and add the type we want to extend.

```typescript
type typeDevice = {
  model: string;
} & typeBrand;
```

<br>

_How can we assign our type?_

```typescript
const myDevice: typeDevice = {
  name: "zerquiolin's phone",
  model: "iphone 8",
};
```

<br>

**_- You can merge interfaces but not types!_**

<br>
