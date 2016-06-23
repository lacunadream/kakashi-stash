// var React = require('react');
import React from 'react'
import ReactDOM from 'react-dom'
// var ReactDOM = require('react-dom');
import Home from './components/Home'
// var Home = require('./components/Home')

var UserGist = React.createClass({
  getInitialState: function() {
    return {
      username: '',
      lastGistUrl: ''
    };
  },

  componentDidMount: function() {
    this.serverRequest = $.get(this.props.source, function (result) {
      var lastGist = result[0];
      console.log(lastGist)
      this.setState({
        username: lastGist.owner.login,
        lastGistUrl: lastGist.html_url
      });
    }.bind(this));
  },

  componentWillUnmount: function() {
    this.serverRequest.abort();
  },

  render: function() {
    console.log(this.state)
    return (
      <div>
        {this.state.username}'s last gist is
        <a href={this.state.lastGistUrl}>here</a>.
        <asdasd/>
      </div>
    );
  }
});

// class UserGist extends React.Component {
//   render() {
//     return 
//     <div> hi  </div>
//   }
// }


var Asdasd = React.createClass({
  render: function() {
    return <div> lol </div>

  }
})

const KelloMessage = (props) => <div> {props.name} </div>;

ReactDOM.render(
  <Home name="https://api.github.com/users/octocat/gists" />,document.getElementById('app')
);