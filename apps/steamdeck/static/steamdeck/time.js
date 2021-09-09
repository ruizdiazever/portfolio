var countDownDate = new Date("dec 1, 2021 00:00:00").getTime();

var x = setInterval(function () {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    document.getElementById("days").innerHTML = days + "d " + hours + "h "+ minutes + "m " + seconds + "s ";

    var decEnd = (days + 31);
    var q1_begin = (days + 31);
    var q1_end = (q1_begin + 90);    
    document.getElementById("time").innerHTML = "Dec " + days + "-" + decEnd + " days | Q1 " + q1_begin + "-" + q1_end + " days";

    if (distance < 0) {
        clearInterval(x);
        document.getElementById("days").innerHTML = "EXPIRED";
    }
}, 1000);
