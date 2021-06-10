# **_Node Js_**

Node Js allow us to run Js Code outside the browser, it was build on chrome's V8 Js Engine (Tool that compiles our code into machine code!), and also let us create secure, functional and escalable _FullStack Web Applications_ way easier!<br>

---

<br>

### **Requirements**

<br>
Basic Understandin on:

~ Html.<br>
~ Css.<br>
~ Js: ES6.<br>

- Callbacks.<br>
- Promises.<br>
- Asynd-Await.<br>

<br><br>

### **What You Will Learn**

<br>

~ Node fundamentals.<br>

- Complex Rest API
- Mern App
- Projects.

~ Express Js.<br>
~ mongoDB.<br>
~ Mongoose.<br>
~ Aplicaitons.<br>
~ Deployment.<br>

<br>

---

<br>

## **~ Introduction**

<br><br>

Differences between Browser's and Node Js

| Browser          | Node Js          |
| ---------------- | ---------------- |
| DOM              | No DOM           |
| Window           | No Window        |
| Interactive Apps | Server Side Apps |
| No Filesystem    | Filesystem       |
| Fragmentation    | Versions         |
| ES6 Modules      | Common Js        |

<br>

### **Install Node Js**

<br>

Navidate to [NodeJs](https://nodejs.org/en/) and download the LTD version (Long Term Support).

Once installed, check in your terminal with the command **node --version** to check the version and verify everything is correct!

<br>

### **How do we get Node to evaluate our code?**

<br><br>

#### **REPL (Read-Eval-Print Loop)**

<br>

It bassicaly takes the user inputs, executes them and returns the result to the user.

<br>

**_How can we use REPL?_**

~ We have to type **node** and hit enter, the we will have an angle bracker **>**, this means we are inside the REPL.

```typescript
PC C: something> node
> const success = 1;
> success
1
```

To exit the REPL just hit **CTRL + C** \* 2

<br>

#### **CLI (Command Line Interface)**

<br>

Allows the user to respond to visual prompts by typing single commands into the interface and receiving a reply in the same way.

<br>

So instead of writting our code inside the terminal, we can run a serious Node application typing **node + filePath** and it'll handle everything!

```typescript
PC C: something> node app.js
```

<br>

#### **Which one should I choose?**

<br>

REPL is often used to starters and playing around, CLI is used for everything else, for beginners, playing around on REPL is perfect, but, for mastering your skills, CLI will do the job!

<br><br>

## **~ Node Fundamentals**

<br> <br>

### **GLobals**

<br>

No matter where we are in the application, we can always access these variables.

Some variables:

~ \_\_dirname: Path to current directory.<br>
~ \_\_filename - file name.<br>
~ require - function to use modeules (CommonJs).<br>
~ module - info about current module (file).<br>
~ process - info about environment where the program is being executed.

<br>

### **Modules (Encapsulated code)**

<br>

As we are only calling one file it's extremly complex to writte and entire app in just one file, so we have to split it on modules!

Every file is a module by default, so after creating a new file with our needed code we can export what we only need by using **module.exports** and setting it to an object with the varibales we want to share!

```javascript
// local
const secret = "secret";

// shared
const hello = "Hi, How are you!?";
const bye = "Bye, Nice to meet you!";

// exports
module.exports = { hello, bye };
```

On the main file, we can import this information by using **require**!

```javascript
// imports
const phrases = require("./filepath");

~ Notice inside the require parenthesis we set the file path where we are exporting our data.
~ Now, 'phrases' has the object: {hello, bye}.

~ We can also destructure the object:
const { hello, bye } = require("./filepath");
```

<br>

#### **Alternative flavor**

<br>

We can also export our code by:

```javascript
module.exports.items = [1, 2];

const device = {
  name: "kerboard",
};
module.exports.electronicDevice = device;
```

<br>

### **Mind Grenade**

<br>

Instead of setting out the modules, once we require a file without asign it to a variable it'll invoque what's inside the called file.

<br>

### **Built-In Modules**

<br>

Here are some of the most used Built-In Modules!
I'll briefly explain some of the uses and methods each module has, so don't think this is all we have!

<br>

#### **OS**

<br>

Provides many useful properties and methods for interacting with the operating system as well as the server.

<br>

_How to import?_

```javascript
const os = require("os");
```

_How to access it's methods and properties?_

```javascript
// Info about the current user
const user = os.userInfo();

// How long the computer has been running
const upTime = os.uptime();
```

<br>

#### **PATH**

<br>

Let's you interact with path's easily.

<br>

_How to import?_

```javascript
const path = require("path");
```

_How to access it's methods and properties?_

```javascript
// Get our actual path
const ourPath = path.sep();

// How to normalize path's
const filePath = path.join("/som/", "folder", "file.txt"); // it'll return '/som/folder/file.txt'

// Imagine we have a file.txt and we want to read what's inside of it
const base = path.basename(filePath); // Here we will get the text inside the file.

// So, you want an absolute path?
// Here we will set the same path to our file.txt we set on the 'filePath' variable
const absolutePath = path.resolve(__dirname, "som", "folde", "file.txt"); // Remember the global variables? __dirname will provide our current path and .resolve will join that path with the variables we pass
```

<br>

#### **FS (File System)**

<br>

There are two flavors when it comes to file module:

<br>

**_~ Sync (Blocking)_**

<br>

```javascript
// So, do you want to read and write a file?
// First, we implement FS by destructuring the readFileSync and writeFileSync!
const { readFileSync, writeFileSync } = require("fs");

// To get the data from a file we have to call the readFileSync function and set the parameters: 1. File path. & 2. Character encoding.
const dataFile = readFileSync("./folder/subfolder/file.txt", "utf8");

// To create or write on a file, we have to call the writeFileSync function and set the parameters: 1. File name. (If the file name doesn't exits, node will created automaticly) & 2. Data.
writeFileSync("./folder/subfolder/myFile.txt", "Hey, this is my file!");

// With only two parameters we are creating or overwriting the data inside selected file, but if we want to append it, we must pass an extra parameter: 3. append.
writeFileSync("./folder/subfolder/myFile.txt", "Hey, this is my file!", {
  flag: "a",
});
```

<br>

**_~ Async (Non-Blocking)_**

<br>

```javascript
// If we want to recreate the read and write methods from the Async examples, we now have to implement CallBacks!

// Instead of requiring Sync functions we now need to call Async functions!
const { readFile, writeFile } = require("fs");

// Now on the readFile we have a third parameter, the 'callback' function, which will tell us if the program failed or succeeded!
readFile("./myFile.txt", "utf8", (error, result) => {
  if (error) {
    console.log(error);
    return;
  }

  // The callback also apply on the writeFile function!
  writeFile(
    "./mySecondFile.txt",
    `Here is the result from the first file: ${result}`,
    (error, result) => {
      if (error) {
        console.log(error);
        return;
      }

      console.log("success!");
    }
  );
});
```

<br>

**_~ Sync Vs Async!_**

<br>

_Sync is a line-by-line reader that will be executing the code as it's reading it, this could have an impact on performance if we are working with several users and demanding tasks, creating death time for the user, waiting until the tasks from other users are done._

_Async is a background worker, it's not a line-by-line reader, so it could be doing more tasks while the async function is still running in the background, making the workflow a lot more consistent and fluid, decreasing the death time for the user._

<br>

#### **HTTP**

<br>

Server side AKA Http Module!


<br>

<br><br>

## **Express Tutorial**

```

```
