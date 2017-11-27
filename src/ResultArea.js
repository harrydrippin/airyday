import React, { Component } from 'react';
import FlightPlanCard from "./FlightPlanCard";

var $ = require('jquery');

/*

<ResultArea airline={this.state.airline}
            flight_num={this.state.flight_num}
            year={this.state.year}
            month={this.state.month}
            day={this.state.day}
            depart={this.state.depart}
            arrival={this.state.arrival}
            result={this.state.result} />

*/

class ResultArea extends Component {
  goToTop() {
    $('html, body').animate({
        scrollTop: $('body').offset().top + 'px'
    }, 'slow');
    $('#gototop-button').css("visibility", "hidden");
  }

  render() {
    var key_count = -1;

    var guideText = "";

    var isAirlineExist = this.props.airline !== "";
    var isFlightNumExist = this.props.flight_num !== "";
    var isDepartExist = this.props.depart !== "";
    var isArrivalExist = this.props.arrival !== "";
    var isDataChecked = false;

    if (isAirlineExist || isFlightNumExist) {
      isDataChecked = true;
      guideText += "편명이 ";
      if (isAirlineExist) {
        guideText += "<strong>" + this.props.airline.toUpperCase() + "</strong>(으)로 시작하";
        if (isFlightNumExist) {
          guideText += "고 ";
        } else {
          guideText += "는<br>";
        }
      }
      if (isFlightNumExist) {
        guideText += "<strong>" + this.props.flight_num + "</strong>(으)로 끝나는<br>";
      }
    }

    if (this.props.year !== "" && this.props.month !== "" && this.props.day !== "") {
      isDataChecked = true;
      guideText += "<strong>" + this.props.year + "년 " + this.props.month + "월 " + this.props.day + "일</strong>의 ";
      if (isDepartExist || isArrivalExist) {
        guideText += "기록 중<br>";
      }
    }

    if (isDepartExist) {
      isDataChecked = true;
      guideText += "<strong>" + this.props.depart.toUpperCase() + "</strong>에서 출발";
      if(isArrivalExist) {
        guideText += ", ";
      } else {
        guideText += "하는 ";
      }
    }

    if (isArrivalExist) {
      isDataChecked = true;
      guideText += "<strong>" + this.props.arrival.toUpperCase() + "</strong>에 도착하는 ";
    }

    if (isDataChecked) {
      guideText += "기록을 검색합니다."
    }

    //guideText = guideText.replace("<br>", "</span><br><span class=\"guide-text\">")

    return (
      <section className="section-result">
        <div className="guide-cover">
        <span className="guide-text" dangerouslySetInnerHTML={{
          __html: guideText
        }}></span>
        </div>
        <div className="card-list" id="card-loaded">
        {this.props.result.map(function(item) {
          key_count++;
          return <FlightPlanCard key={key_count}
                       flightNum={item.flight_num}
                       flightType={item.flight_type}
                       regnum={item.regnum}
                       depart={item.depart}
                       departTime={item.depart_time}
                       arrival={item.arrival}
                       arrivalTime={item.arrival_time}
                       nowInfo={item.now_info}
                       isFpApplied={item.is_fp_applied}/>
        })}
        </div>
        <a onClick={this.goToTop.bind(this)} id="gototop-button">Top</a>
      </section>
    )
  }
}

export default ResultArea;
