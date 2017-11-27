import React, { Component } from 'react';
import NavBar from "./NavBar";
import SearchArea from "./SearchArea";
import ResultArea from "./ResultArea";
import { Modal } from 'react-bootstrap';

var $ = require('jquery');

class AppContainer extends Component {
  constructor() {
    super(...arguments);
    this.state = {
      airline: "",
      flight_num: "",
      year: "",
      month: "",
      day: "",
      depart: "",
      arrival: "",
      modal: false,
      time_start: "",
      time_end: "",
      changelogmodal: true,
      result: []
    }
  }

  resetDetails() {
    this.setState({
      airline: "",
      flight_num: "",
      year: "",
      month: "",
      day: "",
      depart: "",
      arrival: "",
      time_start: "",
      time_end: ""
    });
  }

  modalClose() {
    this.setState({
      modal: false
    });
  }

  modalClose2() {
    this.setState({
      changelogmodal: false
    });
  }

  onDataChangeSubmit(type, data) {
    // eslint-disable-next-line
    this.state[type] = data;
    this.forceUpdate();
  }

  onSearchSubmit(type) {
    if (this.state.year === "" || this.state.month === "" || this.state.day === "") {
      this.setState({
        modal: true
      });
      return;
    }
    $('#search-button__out').html(type + " Bound 모드")
    $('#search-button__in').html("검색중입니다...");
    $('#search-button__out').css({
      border: "1px solid grey",
      background: "#FFFFFF",
      color: "grey"
    });
    $('#search-button__in').css({
      border: "1px solid grey",
      background: "#FFFFFF",
      color: "grey"
    });

    var realMonth = "";
    var realDay = "";

    if(this.state.month.length === 1) {
      realMonth = "0" + this.state.month;
    } else {
      realMonth = this.state.month;
    }

    if(this.state.day.length === 1) {
      realDay = "0" + this.state.day;
    } else {
      realDay = this.state.day;
    }
    console.log("Requesting...");
    var innerContext = this;
    $.get( "http://45.55.209.60:5000/search/" + type.toLowerCase(),
      {
        date: this.state.year + realMonth + realDay,
        airline: this.state.airline,
        flight_num: this.state.flight_num,
        depart: this.state.depart,
        arrival: this.state.arrival
      },
    function(data) {
      console.log("Starting data process...");
      console.log(data.results);
      data = data.results;
      console.log(parseInt(innerContext.state.time_start + "00", 10) + " ~ " + parseInt(innerContext.state.time_end + "00", 10));
      if (type === "Out") {
        data.sort(function(a, b) {
          if (a.depart_time === "알 수 없음") {
            return 100;
          } else if (b.depart_time === "알 수 없음") {
            return -100;
          } else {
            return parseInt(a.depart_time.replace(":", ""), 10) - parseInt(b.depart_time.replace(":", ""), 10);
          }
        });
        if (innerContext.state.time_start !== "" && innerContext.state.time_end !== "")
        data.forEach(function(value, index, ar) {
          if (parseInt(value.depart_time.replace(":", ""), 10) < parseInt(innerContext.state.time_start + "00", 10) ||
              parseInt(value.depart_time.replace(":", ""), 10) > parseInt(innerContext.state.time_end + "00", 10)) {
              console.log("Delete log:" + data[index]);
              delete data[index];
          }
        });
      } else {
        data.sort(function(a, b) {
          if (a.arrival_time === "알 수 없음") {
            return 100;
          } else if (b.arrival_time === "알 수 없음") {
            return -100;
          } else {
            return parseInt(a.arrival_time.replace(":", ""), 10) - parseInt(b.arrival_time.replace(":", ""), 10);
          }
        });
        if (innerContext.state.time_start !== "" && innerContext.state.time_end !== "")
        data.forEach(function(value, index, ar) {
          if (parseInt(value.arrival_time.replace(":", ""), 10) < parseInt(innerContext.state.time_start + "00", 10) ||
              parseInt(value.arrival_time.replace(":", ""), 10) > parseInt(innerContext.state.time_end + "00", 10)) {
              console.log("Delete log:" + data[index]);
              delete data[index];
          }
        });
      }

      console.log("FlightPlan data received.");
      console.log(data);
      innerContext.setState({
        result: data
      });
      $('#search-button__out').html("Out Bound로 검색하기")
      $('#search-button__in').html("In Bound로 검색하기");
      $('#gototop-button').css("visibility", "visible");
      $('#search-button__out').css({
        background: "#1EAAF1",
        color: "white",
        border: "1.5px solid white",
        borderRight: "1.5px dashed white"
      });
      $('#search-button__in').css({
        background: "#1EAAF1",
        color: "white",
        border: "1.5px solid white",
        borderLeft: "1.5px dashed white"
      });

      if ($(window).width() > 991) {
        $('.screen-right').css("height", $(window).height() - 60);
      } else {
          $('html, body').animate({
              scrollTop: $('#card-loaded').offset().top + 'px'
          }, 'slow');
      }
    });
  }

  render() {
    return (
      <div id="wrapper">
        <NavBar />
        <div className="container-fluid">
          <div className="col-md-4 screen-left">
            <SearchArea airline={this.state.airline}
                        flight_num={this.state.flight_num}
                        year={this.state.year}
                        month={this.state.month}
                        day={this.state.day}
                        depart={this.state.depart}
                        arrival={this.state.arrival}
                        onDataChangeSubmit={this.onDataChangeSubmit.bind(this)}
                        onSearchSubmit={this.onSearchSubmit.bind(this)} />
          </div>
          <div className="col-md-8 screen-right result-area">
            <ResultArea airline={this.state.airline}
                        flight_num={this.state.flight_num}
                        year={this.state.year}
                        month={this.state.month}
                        day={this.state.day}
                        depart={this.state.depart}
                        arrival={this.state.arrival}
                        result={this.state.result} />
          </div>
        </div>
        <Modal show={this.state.modal}>
          <div className='modal-header'>
            <span style={{fontSize: "1.2em"}}>날짜 데이터가 없습니다!</span>
          </div>
          <div className='modal-body'>
            날짜 데이터가 없는 경우 조회가 되지 않습니다.<br/>날짜를 넣어주세요.
          </div>
          <div className='modal-footer'>
            <button className="btn btn-primary" onClick={this.modalClose.bind(this)}>닫기</button>
          </div>
        </Modal>
        <Modal show={this.state.changelogmodal}>
          <div className='modal-header'>
            <span style={{fontSize: "1.2em"}}>Changelog</span>
            <button className="btn btn-primary" style={{float: "right"}} onClick={this.modalClose2.bind(this)}>닫기</button>
          </div>
          <div className='modal-body'>
            <p>
              <strong>Ver. 0.2.3 (2017. 1. 1.)</strong>
                <ul>
                  <li>2017년 1월 1일을 조회하면 "201711"로 들어가는 버그 수정</li>
                  <li>새해 복 많이 받으세요 :)</li>
                </ul>
              <strong>Ver. 0.2.2 (2016. 12. 29.)</strong>
                <ul>
                  <li>날짜 데이터가 없을 시 창으로 안내 추가</li>
                  <li>Changelog 추가, 개발 중에는 항상 게시</li>
                </ul>
              <strong>Ver. 0.2.1</strong>
                <ul>
                  <li>검색 결과 리스트 디자인 모바일 최적화</li>
                  <li>검색 결과에 안내 문구 추가, 이후 UI 상단 고정 예정</li>
                </ul>
              <strong>Ver. 0.2.0</strong>
                <ul>
                  <li>검색 결과 리스트 디자인 완전 적용</li>
                  <li>Component 별 상태 안정성 개선</li>
                  <li>UBI-KAIS 서버 데이터 흐름 안정화</li>
                  <li>이제 서버에서 데이터를 100개씩 조회함</li>
                </ul>
              <strong>Ver. 0.1.2</strong>
                <ul>
                  <li>검색 폼 디자인 모바일 최적화</li>
                  <li>모든 페이지 상하 이동에 애니메이션 추가</li>
                </ul>
              <strong>Ver. 0.1.1</strong>
                <ul>
                  <li>검색 결과 리스트 디자인 개선</li>
                  <li>모바일에서 맨 위로 가기 버튼 추가</li>
                </ul>
              <strong>Ver. 0.1.0</strong>
                <ul>
                  <li>모바일 최적화 추가</li>
                  <li>일부 기기에서 폼이 비대칭으로 나오는 버그 수정</li>
                </ul>
              <strong>Ver. 0.0.1</strong>
                <ul>
                  <li>소스 전체 빌드 및 적용</li>
                </ul>
            </p>
          </div>
          <div className='modal-footer'>
            <button className="btn btn-primary" onClick={this.modalClose2.bind(this)}>닫기</button>
          </div>
        </Modal>
      </div>
    );
  }
}

export default AppContainer;
