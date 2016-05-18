var x = 0;  // x is declared global, then assigned a value of 0

console.log(x)

console.log(typeof z); // undefined, since z doesn't exist yet

function a() { // when a is called,
  var y = 2;   // y is declared local to function a, then assigned a value of 2

  console.log(x, y);   // 0 2 

  function b() {       // when b is called
    x = 3;  // assigns 3 to existing global x, doesn't create a new global var
    y = 4;  // assigns 4 to existing outer y, doesn't create a new global var
    z = 5;  // creates a new global variable z and assigns a value of 5. 
  }         // (Throws a ReferenceError in strict mode.)

  b();     // calling b creates z as a global variable
  console.log("lol " + typeof y)

  console.log(x, y, z);  // 3 4 5
}

a();                   // calling a also calls b
console.log(x, z);     // 3 5
console.log(typeof x); // undefined as y is local to function a
console.log(typeof y)
console.log(typeof z)

// var = function level scoping. ```if``` is not a function, hence the third console.log is still within the same function level scope as the second var declaration	 

// var x = 1;
// console.log(x); // 1
// if (true) {
// 	var x = 2;
// 	console.log(x); // 2
// }
// console.log(x); // 2

// let = block level scoping. a is equal to 2 only within the middle block
let aa = 1;
console.log(aa); // 1
if (true) {
	let aa = 2;
	console.log(aa); // 2
}
console.log(aa); // 1

// declaration vs initialization
var ba // declaration
ba = 1 // initialization 

// Function expressions do not get fully hoisted to the top. Hence the error

function test() {
	// foo(); // TypeError "foo is not a function"
	bar(); // "this will run!"
	var foo = function () { // function expression assigned to local variable 'foo'
		console.log(11);
	}
	function bar() { // function declaration, given the name 'bar'
		console.log(22);
	}
	foo() // This runs!
}
test();

//function declaration > variable d
// var init > function dec

function aaa(x) {
    return x * 2;
}
var aaa;
console.log(aaa)