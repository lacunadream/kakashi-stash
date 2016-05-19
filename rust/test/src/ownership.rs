fn main() {
	let mut x = 5;

	let y = &mut x;    // -+ &mut borrow of x starts here
	                   //  |
	*y += 1;           //  |
	                   //  |
	println!("{}", x); // -+ - try to borrow x here
	                   // -+ &mut borrow of x ends here
}


// borrowing
fn foo(v1: &Vec<i32>, v2: &Vec<i32>) -> i32 {
}

// one or more references (&T) to a resource,
// exactly one mutable reference (&mut T).


// implicit
fn foo(x: &i32) {
}

// explicit
fn bar<'a>(x: &'a i32) {
}


// Lifetime rules (Elision)

// Each elided lifetime in a function’s arguments becomes a distinct lifetime parameter.
// If there is exactly one input lifetime, elided or not, that lifetime is assigned to all elided lifetimes in the return values of that function.
// If there are multiple input lifetimes, but one of them is &self or &mut self, the lifetime of self is assigned to all elided output lifetimes.

