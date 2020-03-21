function chy(obj) {
    var rr = $("input[type='radio']:checked").val();
    print(rr)
    if (rr == "caregiver") {
        document.getElementById("patient-user-name").style.display = "";
    } else {
        document.getElementById("patient-user-name").style.display = "none";
    }
}