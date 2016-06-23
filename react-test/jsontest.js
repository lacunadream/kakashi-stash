var a = randomValue()
var b = randomValue()

function randomValue() {
	rand = Math.random(0,1)
	if (rand > 0.5) {
		return 'yes'
	} else {
		return undefined 
	}
}

console.log(a, b)

// var obj = {'c': undefined, 'd':undefined}
var obj = ['c', 'd']

var fuckArray = {}

for (something in obj) {
	console.log(something)
}