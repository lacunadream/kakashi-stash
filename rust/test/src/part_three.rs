struct Point {
    x: i32,
    y: i32,
}


// mutability is at property level
let mut point = Point { x: 0, y: 0 };

// field level mutability
struct Point {
    x: i32,
    y: Cell<i32>,
}

// update

struct Point3d {
    x: i32,
    y: i32,
    z: i32,
}

let mut point = Point3d { x: 0, y: 0, z: 0 };
point = Point3d { y: 1, .. point };

// data of several variants
enum Message {
    Quit,
    ChangeColor(i32, i32, i32),
    Move { x: i32, y: i32 },
    Write(String),
}