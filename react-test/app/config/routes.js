var React = require('react')
var ReactRouter = require('react-router')
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute
var Main = require('../components/Main')
var Home = require('../components/Home')
var hashHistory = ReactRouter.hashHistory
var LOL = require('../components/LOL')
var Asd = require('../components/asd')

var routes = (
	<Router history={hashHistory}>
		<Route path='/' component={Main}>
			<IndexRoute component={Home} />
			<Route path='/home' component={Asd} />

		</Route>
	</Router>
)

module.exports = routes


			// <IndexRoute component={Home} />		
			// <IndexRoute component={LOL} />	

						// 		<IndexRoute component={LOL, Home} />