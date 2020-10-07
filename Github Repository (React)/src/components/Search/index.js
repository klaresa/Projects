import React, { Component } from 'react';
import './style.css';
import apiGit from "../../service/api";

class Search extends Component {

  // you dont really need it now
  // constructor(props){
  //   super(props);
  state = {
    placeholder : "klaresa",
    user: '',

    data:[]
  };
  // }

  componentDidMount() {
    this.setState({ user: ''} );
  }

  updateInputValue(event) {
    this.setState({ user: event.target.value });
  }

  checkRepo = async () => {
      if (this.state.user !== ''){
        const userName = this.state.user;
        const response = await apiGit.get(`${userName}/repos`);
        const respall = response.data;
        this.setState({data: respall});
      } else {
        alert("Enter user name!")
      }
  };

  render() {
    const { data } = this.state;
    return (
        // it starts with a div
        <div className="repo-search">
        <input id="inputD" required placeholder={this.state.placeholder} onChange={event => this.updateInputValue(event)}/>
        <button onClick={this.checkRepo}>Check</button>

          {data.map(repos => (
            <article className="repos" key={repos.id} id={repos.id}>
              <p><strong>{repos.name}</strong></p>
              <p><a href={repos.html_url}>{repos.html_url}</a></p>
            </article>
          ))}

        </div>
        // it ends with it
    );
  }
}

export default Search;
