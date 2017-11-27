import React, { Component } from 'react';

var $ = require('jquery');

class SearchArea extends Component {
  onAirlineChange(event) {
    this.props.onDataChangeSubmit("airline", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onFlightNumChange(event) {
    this.props.onDataChangeSubmit("flight_num", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onYearChange(event) {
    this.props.onDataChangeSubmit("year", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onMonthChange(event) {
    this.props.onDataChangeSubmit("month", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onDayChange(event) {
    this.props.onDataChangeSubmit("day", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onDepartChange(event) {
    this.props.onDataChangeSubmit("depart", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onArrivalChange(event) {
    this.props.onDataChangeSubmit("arrival", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onTimeStartChange(event) {
    this.props.onDataChangeSubmit("time_start", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onTimeEndChange(event) {
    this.props.onDataChangeSubmit("time_end", event.target.value);
    this.inputRender();
    event.preventDefault();
  }

  onSearchOut(event) {
    this.props.onSearchSubmit("Out");
    event.preventDefault();
  }

  onSearchIn(event) {
    this.props.onSearchSubmit("In");
    event.preventDefault();
  }

  inputRender() {
    $('input[type="text"]')
      .keyup(this.resizeInput)
      .each(this.resizeInput);
  }

  resizeInput() {
    $(this).attr('size', $(this).val().length === 0 ? $(this).attr('placeholder').length : $(this).val().length);
  }

  render() {
    return (
      <section className="section-search">
        <div className="form-group">
          <span className="form-label">편명</span><br/>
          <input type="text" className="form-input__airline"
                 placeholder="KAL" value={this.props.airline}
                 size="3" onChange={this.onAirlineChange.bind(this)}/>
          <span className="form-label__airline_between">/&nbsp;</span>
          <input type="text" className="form-input__flightnum"
                 placeholder="561" value={this.props.flight_num}
                 size="3" onChange={this.onFlightNumChange.bind(this)}/>
        </div>
        <div className="form-group">
          <span className="form-label">날짜 (필수 데이터)</span><br/>
          <input type="text" className="form-input__date_year"
                 placeholder="2016" value={this.props.year}
                 size="4" onChange={this.onYearChange.bind(this)}/>
          <span className="form-label__date_between">/&nbsp;</span>
          <input type="text" className="form-input__date_month"
                 placeholder="12" value={this.props.month}
                 size="2" onChange={this.onMonthChange.bind(this)}/>
          <span className="form-label__date_between">/&nbsp;</span>
          <input type="text" className="form-input__date_day"
                 placeholder="25" value={this.props.day}
                 size="2" onChange={this.onDayChange.bind(this)}/>
        </div>
        <div className="form-group">
          <span className="form-label">출발지</span><br/>
          <input type="text" className="form-input__depart"
                 placeholder="RKSI" value={this.props.depart}
                 size="4" onChange={this.onDepartChange.bind(this)}/>
        </div>
        <div className="form-group">
          <span className="form-label">도착지</span><br/>
          <input type="text" className="form-input__arrival"
                 placeholder="VTBS" value={this.props.arrival}
                 size="4" onChange={this.onArrivalChange.bind(this)}/>
        </div>
        <div className="form-group">
          <span className="form-label">검색 시간</span><br/>
          <input type="text" className="form-input__time_start"
                 size="1" placeholder="12" value={this.props.time_start}
                 onChange={this.onTimeStartChange.bind(this)}/>
          <span className="form-label__date_between">시 ~&nbsp;</span>
          <input type="text" className="form-input__time_end"
                 size="1" placeholder="15" value={this.props.time_end}
                 onChange={this.onTimeEndChange.bind(this)}/>
          <span className="form-label__date_between">시</span>
        </div>
        <div className="btn-group" role="group">
          <button className="btn btn-default search-button-out" id="search-button__out" onClick={this.onSearchOut.bind(this)}>Out Bound로 검색하기</button>
          <button className="btn btn-default search-button-in" id="search-button__in" onClick={this.onSearchIn.bind(this)}>In Bound로 검색하기</button>
        </div>
      </section>
    )
  }
}

export default SearchArea;
