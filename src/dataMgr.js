var $ = require('jquery');

if (!String.prototype.format) {
    String.prototype.format = function() {
        var str = this.toString();
        if (!arguments.length)
            return str;
        var args = typeof arguments[0],
            args = (("string" == args || "number" == args) ? arguments : arguments[0]);
        for (arg in args)
            str = str.replace(RegExp("\\{" + arg + "\\}", "gi"), args[arg]);
        return str;
    }
}

function dataMgr() {
  this.getUbiData = function(type, date, airline, flight_num, depart, arrival) {
    let UBI_URL = "http://ubikais.fois.go.kr/biz/fpl/{type}.jsp?srch_date={date}&srch_al={airline}&srch_fln={flight_num}&srch_dep={depart}&srch_arr={arrival}"
              .format({
                type: type,
                date: date,
                airline: airline,
                flight_num: flight_num,
                depart: depart,
                arrival: arrival
              });

    $.ajax({
            url: UBI_URL,
            success: function(data, textStatus) {
              // TODO;
              console.log(data)
            },
            dataType: "xml"
    });
  }

  this.getAirportData = function(keyword) {
    return 'goodbye!';
  }
}

module.exports = dataMgr;
