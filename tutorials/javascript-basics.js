// this is a test file


let y = 'this is a sentence';
console.log(y);

let z = '1';
console.log(z + 5);

let num = 1;
console.log(num + 5);

let a = 'cat';
let b = 'dog';
b = 'zaboomafoo';

console.log(a + ' ' + b);

console.log(typeof z);
console.log(typeof num);

const constantVariable = 10;
console.log(constantVariable);



// Booleans (true or false)
let a = 100;
console.log(a === 100);
console.log(a === 99);
console.log(a >= 99);


// Conditional
let babyStatus = 'crying';

if (babyStatus === 'not crying') {
  console.log('chill');
} else if (babyStatus === 'crying') {
  console.log('panic');
}

let hour = 12;
let greeting = 'it is the apocalypse';
console.log(hour === 12);

if (false) {
  greeting = "it is noon";
}

console.log(greeting);


// For Loop

// initial value; condition as long as true; iteration counter up/down
// at beginning of for loop, i = 0
for (let i = 5; i <= 10; i++) {
  // run if i <= 10, stop if hits 11

  if (i === 8) {
    console.log('hello, this is 8');
  } else {
    console.log(i);
  }
  // at end of loop, add 1 to i
}



// Functions
// Classes




