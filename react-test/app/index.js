var React = require('react');
var ReactDOM = require('react-dom');

var routes = require('./config/routes')

ReactDOM.render(
	routes,
	document.getElementById('app')
);


// var Container = React.createClass({
//   render: function () {
//     return (
//       <Wrapper>
//         <Welcome name={'lacunadream'}/>
//         <Hello />
//       </Wrapper>
//     )
//   }
// });

// var Wrapper = React.createClass({
//   render: function () {
//     return (
//       <div style={{backgroundColor: 'pink'}}>
//         <h1> Header! </h1>
//         {this.props.children}
//       </div>
//     )
//   }
// });

// var Welcome = React.createClass({
//   render: function () {
//     return <div>Welcome {this.props.name}!</div>
//   }
// });

// var Hello = React.createClass({
//   render: function () {
//     return <div>Hello ReactJS Program!</div>
//   }
// })

// ReactDOM.render(<Container />, document.getElementById('app'));
// // const KelloMessage = (props) => <div> {props.name} </div>;
// // const HelloMessage = (props) => <div>Hello {props.name}</div>;

// // ReactDOM.render(<KelloMessage name="jkjk"/>, document.getElementById('app'))