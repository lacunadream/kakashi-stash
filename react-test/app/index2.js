// var React = require('react');
import React from 'react'
import ReactDOM from 'react-dom'
// var ReactDOM = require('react-dom');
// import Home from './components/Home'
// var Home = require('./components/Home')

import Select from 'react-select'

// var UserGist = React.createClass({
//   getInitialState: function() {
//     return {
//       username: '',
//       lastGistUrl: ''
//     };
//   },

//   componentDidMount: function() {
//     this.serverRequest = $.get(this.props.source, function (result) {
//       var lastGist = result[0];
//       console.log(lastGist)
//       this.setState({
//         username: lastGist.owner.login,
//         lastGistUrl: lastGist.html_url
//       });
//     }.bind(this));
//   },

//   componentWillUnmount: function() {
//     this.serverRequest.abort();
//   },

//   render: function() {
//     console.log(this.state)
//     return (
//       <div>
//         {this.state.username}'s last gist is
//         <a href={this.state.lastGistUrl}>here</a>.
//         <asdasd/>
//       </div>
//     );
//   }
// });

// // class UserGist extends React.Component {
// //   render() {
// //     return 
// //     <div> hi  </div>
// //   }
// // }


// var Asdasd = React.createClass({
//   render: function() {
//     return <div> lol </div>

//   }
// })

// class Test extends React.Component {
//   constructor(props) {
//     super(props)
//     this.state = {
//       val : 'All'
//     }
//   }

//   updateVal (newval) {
//     this.setState({
//       val: newval
//     })
//   }
  
//   render() {
//       var options = [
//       { value: 'one', label: 'One' },
//       { value: 'two', label: 'Two' }
//   ];
//     return (
//       <div>
//         <Select onChange = {this.updateVal.bind(this)} options={options} val={this.state.val} name="form-field-name" />
//       </div>
//       )
//   }

// }

var Test = React.createClass({
  render: function() {
  var options = [
    { value: 'one', label: 'One' },
    { value: 'two', label: 'Two' }
];

function logChange(val) {
    console.log("Selected: " + val);
}
return(
<Select
    name="form-field-name"
    value="one"
    options={options}
    onChange={logChange}
/>
)
  }


})

// const KelloMessage = (props) => <div> {props.name} </div>;

ReactDOM.render(
  <Test name="https://api.github.com/users/octocat/gists" />,document.getElementById('app')
);