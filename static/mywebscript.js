let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) { // Handle all completed requests
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else if (this.status == 400) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "An error occurred!";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}