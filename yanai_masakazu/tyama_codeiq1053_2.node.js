#!/usr/bin/env node

console.log(
// CODE_START
(function() {
  var text = "L71EQS78EVNX85HG95UJZ73VNW83UAG95UJS78EVYP79YJF84AG95UJNX85HS78EVZ73VNB88UQNZ46LP76XBZ73VNS78EVNX85HB88UQG95UJZ73VNW83UAG95UJS78EVYP79YJF84AG95UJNX85HS78EVZ73VNB88UQNZ46L";

  var answer = text.replace(
    /.{5}/g
    ,
    function(s){return'_ABCDEFGHIJKLMNOPQRSTUVWXYZ.'['G9G6TDYEB6EVSNL7PTZ7X7TEP7PDS7YPE8U8EWW8JFNXQ8L8B8C8XFNZ'.indexOf(s.substr(0,2))/2]}
  );

  return answer;
})()
// CODE_END
);