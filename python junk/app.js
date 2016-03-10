var request = require('request');

request('http://192.168.15.1/cgi-bin/sysconf.cgi?page=ajax.asp&action=local_address_lease_status', function(error, response, body) {
	console.log(body)
})