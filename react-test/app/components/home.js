var React = require('react')

var Home = React.createClass({
	render: function() {
		return (
			<div> wee {this.props.name}  </div>
			)
	}
})

module.exports = Home;