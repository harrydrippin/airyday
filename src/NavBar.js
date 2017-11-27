import React, { Component } from 'react';
import "./logo.svg";

class NavBar extends Component {
  render() {
    return (
      <nav className="navbar">
        <div className="container-fluid">
          <span className="brand-name">AiryDay Beta</span>
          <span className="version-name">&nbsp;&nbsp;Ver. 0. 2. 3. (InDevelop, Build 20170101004035)</span>
        </div>
      </nav>
    )
  }
}

export default NavBar;
