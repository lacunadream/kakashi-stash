// function bar(a,b) {
// 	var asd = 2000
// 	function asdf(bb, cb) {
// 		k = bb + cb
// 		return k
// 	}
// 	g = asdf(b, function(2000) {
// 		return asd
// 	})
// 	return a + g
// }
// console.log(bar(1,1))



function bar(callback) {
	var k = 100
	callback(k)

}

function foo(argg) {
	console.log(argg)
}

// bar(foo)
