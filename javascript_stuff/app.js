var Q = require('q')
var Promise = require("bluebird");
var fs = require('fs')

// shit pile starts here

function cakap(x) {
	console.log(x)
}

function cakap1() {
	console.log('1')
}

function cakap2(x) {
	console.log('2')
}

// return Q.fcall(function() {
// 	return 10;
// })

function wtf() {
	return Q.promise(function(resolve, reject) {
		function asd() {
			console.log(22)
			resolve(22)
		}
	})
}

function wtf2() {
	var deferred = Q.defer()
	deferred.reject(22)
	return deferred.promise
}

// fuck2(0)
// 	.then(function(x){
// 		fuck2(x)
// 	})
// 	.then(function(x){
// 		return fuck5(x)
// 	})
// 	.then(function(x){
// 		return fuck5(x)
// 	})

// fuck2(0)
// 	// .then(function(x){
// 	// 	fuck(0,x)
// 	// })
// 	.then(function(x) {
// 		return new Promise(function(resolve) {
// 			console.log(x)
// 			resolve(x)
// 		})
// 	}, function(x) {
// 		console.log(x)
// 	})
// 	.then(function(x) {
// 		return new Promise(function(resolve) {
// 			console.log(x)
// 			resolve(x)
// 		})
// 	}, function(x) {
// 		console.log(x)
// 	})
// 	.then(function(x) {
// 		console.log(x)
// 	}, function(x) {
// 		console.log(x)
// 	})			

// fuck2(1)
// 	.then(function(y) {
// 		fuck2(y)
// 	})
// 	.then(function(k) {
// 		cakap(k)
// 	}, function(k) {
// 		console.log('reject ' + k)
// 	}).catch(function(e) {
// 		console.log(e)
// 	})

// fuck5(1)
// 	.then(function(x){
// 		var deferred = Promise.defer()
// 		console.log('ccbc ' + x)
// 		deferred.resolve(x)
// 		return deferred.promise
// 	})
// 	.then(function(x){
// 		return new Promise(function(resolve, reject) {
// 			console.log('ccb ' + x)
// 			resolve(x)
// 		})
// 	})
// 	.then(function(x){
// 		fuck5(x)
// 	})
// 	.catch(function(e) {
// 		console.log('3' + e)
// 	})

// Promise.resolve('foo').then(function () {
//   return Promise.resolve('bar');
// }).then(function (result) {
//   console.log(result);
// });

// fuck2().then(cibai2)
cibai3(cibai2)

function cibai3(callback) {
	fs.readFile('random.txt','utf-8', function(err, data) {
		if (err) {
			console.log(err)
		}
		console.log(data)
		callback(data)
	})
}


function cibai2(asd) {
	console.log('123 ' + asd)
}
function cibai() {
	return new Promise(function(resolve) {
		console.log('wut')
		resolve
	})
}
function fuck(a,b) {
	return new Promise(function(resolve, reject) {
		var x = Math.random(a,b);
		if (x < 0.8) {
			resolve(x)
			console.log('first fuck ' + x)
		} else {
			reject(x)
		}
	})
}

function fuck2(a) {
	return Q.fcall(function(resolve, reject) {
		var x = a+1
		console.log('fuck2 ' + a)
		resolve(x)
	})
}

function fuck3(a) {
	return new Promise(function(resolve, reject) {
		var x = a+1
		console.log(x)
		console.log(typeof x)
		resolve(x)
	})
}

function fuck4 (a) {
	return new Promise(function(resolve) {
		console.log(a)
	})
}

function fuck5 (a) {
	var deferred = Q.defer()
	console.log('1 '+ a)
	deferred.resolve(a)
	return deferred.promise
}

var x = 0
function wtf(a) {
	var x = x + a
	return x
}

// wtf(1)
// var zzzzz = wtf(5)
// console.log(zzzzz)

var abc = ['a', 'b', 'c']

function printout(error, data) {
	if (error) {
		console.log(error)
	} else {
		console.log(data)
	}
}

// fs.readFile('random.txt', 'utf-8', printout);
function asd (n) {
	return { cibai: n}
}

// var names = [ 'tomato', 'turnip', 'lovage', 'snap pea', 'carrot', 'zucchini' ];
// var vegetables = names.map(function(n) {return {cibai:n}});

// console.log(names)
// console.log(vegetables)

// function cb(abc) {
//   console.log(abc)
// }
// function main(callback) {
//   callback(123)
// }
// main(cb)

// var lol = [0,1,2,3,4]
// var ss = lol.reduce(function(previousValue, currentValue, index, array) {
//   return previousValue + currentValue;
// }, 10);

// console.log(ss)