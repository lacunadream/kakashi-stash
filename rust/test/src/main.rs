fn main() {
    println!("Hello, world!");

    // mutability. for variables, standard rules of scoping and shawdoing apply
    let mut x: i32 = 1;


	fn plus_one(i: i32) -> i32 {
	    i + 1
	}

	// without type inference
	// function pointers
	let f: fn(i32) -> i32 = plus_one;

	// // with type inference
	// let f = plus_one;

	let six = f(5);
	let seven = plus_one(6);

	println!("{} lol {}", six, seven);

	// diverging function
	// fn diverges() -> ! {
	//     panic!("This function never returns!");
	// }


	let a = [0, 1, 2, 3, 4];
	let complete = &a[..]; // A slice containing all of the elements in a
	let middle = &a[1..4]; // A slice of a: only the elements 1, 2, and 3

	// different tupple vs array styles:
	// let tuple = (1, 2, 3);
	// let x = tuple.0;

	// let a = [1, 2, 3]; // a: [i32; 3]
	// let mut m = [1, 2, 3]; // m: [i32; 3]

	// IF
	if x == 5{
		println!("lol");
	} else if x == 7 {
		println!("asd");
	} else {
		println!("ok");
	}

	// Loop
	loop {
	    println!("Loop forever!");
	}

}

