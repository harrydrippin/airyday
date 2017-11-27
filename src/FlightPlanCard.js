import React, {Component} from 'react';

/*
{this.props.nowInfo}
{this.props.isFpApplied}
*/

class FlightPlanCard extends Component {
  render() {
    var nowHeuristicInfo = "";
    switch(this.props.nowInfo) {
      case "ARR":
        nowHeuristicInfo = "최근에 목적지에 도착함";
        break;
      case "DEP":
        nowHeuristicInfo = "최근에 출발이 확인됨";
        break;
      case "DLA":
        nowHeuristicInfo = "현재 지연이 확인됨";
        break;
      case "CNL":
        nowHeuristicInfo = "취소됨";
        break;
      default:
        nowHeuristicInfo = "최근 정보 없음";
        break;
    }

    var nowHeuristicFpApplied = "";
    if(this.props.isFpApplied === "Y") {
      nowHeuristicFpApplied = "비행 계획 제출 확인";
    } else if(this.props.isFpApplied === "N") {
      nowHeuristicFpApplied = "비행 계획 미제출";
    } else {
      nowHeuristicFpApplied = "비행 계획 알 수 없음";
    }

    return (
      <div className="row plan-card-wrapper">
        <div className="col-md-11 plan-card">
          <span className="plan-card__flightNum">{this.props.flightNum}</span>
          <span className="plan-card__slash">/</span>
          <span className="plan-card__flightType">{this.props.flightType + ", "}</span>
          <span className="plan-card__regnum">{this.props.regnum}</span><br/>
          <span className="plan-card__label">출발&nbsp;</span>
          <span className="plan-card__depart">{this.props.depart}</span>
          <span className="plan-card__departTime">{", " + this.props.departTime}</span>
          <span className="plan-card__label">도착&nbsp;</span>
          <span className="plan-card__arrival">{this.props.arrival}</span>
          <span className="plan-card__arrivalTime">{", " + this.props.arrivalTime}</span><br/>
          <span className="plan-card__nowInfo">{nowHeuristicInfo + ", " + nowHeuristicFpApplied}</span>
        </div>
      </div>
    )
  }
}

export default FlightPlanCard;
