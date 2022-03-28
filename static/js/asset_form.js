function changeStatus() {

    var status = document.getElementById("balanceStatus");


    if (status.value == "D") {
        document.getElementById("fields").style.visibility = "visible";
    }
    else if (status.value == "T") {
        document.getElementById("fields").style.visibility = "visible";
    }
    else {
        document.getElementById("fields").style.visibility = "hidden";
    }

}

//calculate depriciation value

function depreciation() {

    var selectedValue = document.getElementById("balanceStatus").value;

    // if D
    if (selectedValue == 'D') {
        doubleDepreciation();
    }
    // call strait line
    // else
    else if (selectedValue == 'T') {
        straightline();
    }

    //Call
}


function doubleDepreciation() {
    //var depresult = (mainValue - 0)/year;

    let mainvalue = parseFloat(document.getElementById("bookvalue").value);
    let years = parseInt(document.getElementById("years").value);
    let purchaseYears = parseInt(document.getElementById("fromyear").value);


    let doubleDepreciationRate = ((1 / years) * 100 * 2);
    let current = new Date().getFullYear();
    let yearOfService = current - purchaseYears;

    for (let i = 0; i < yearOfService; i++) {
        let depreciationAmount = (mainvalue * doubleDepreciationRate) / 100;


        mainvalue = mainvalue - depreciationAmount;

    }
    document.getElementById("hgf").value = mainvalue;


}


//Static Value

function straightline() {

    //var depresult = (mainValue - 0)/year;
    var BookValue = parseFloat(document.getElementById("bookvalue").value);
    var Year = parseInt(document.getElementById("years").value);
    var YearFrom = parseInt(document.getElementById("fromyear").value);

    BookValue = parseFloat(BookValue);
    Year = parseInt(Year);
    YearFrom = parseInt(YearFrom);

    //const result=(MainValue-0)/Year;

    var RemainingBalance;
    var currentyear = new Date().getFullYear();

    RemainingBalance = (BookValue - ((BookValue / Year) * (currentyear - YearFrom)));


    document.getElementById("hgf").value = RemainingBalance;


}