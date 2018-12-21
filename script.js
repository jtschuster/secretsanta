
var namesDiv = document.getElementById("data");
var addBtn = document.getElementById("add-email-btn");
var pickNamesBtn = document.getElementById("pick-names-btn")
var namesIn = document.getElementById("namesInput");
var emailIn = document.getElementById("emailInput")
var names = [];
var ishad = [];
var hasname = [];
var namesEmails = [];
var emails = [];
var num_of_emails = 0;
var num_of_names = 0;

function findCommas(stringList) {
    var fcommas = [];
    for (i = 0; i < stringList.length; i++) {
        if (stringList[i] === ",") {
            fcommas.push(i);
        }
    }
    console.log(fcommas);
    return fcommas;
}

function parsenames() {
    var rawnames = namesIn.value;
    console.log(rawnames);
    var commas = findCommas(rawnames);
    console.log(commas)
    var nameslist = [];

    nameslist.push(rawnames.substr(0, commas[0]));
    nameslist[nameslist.length - 1].trim();
    console.log(nameslist[nameslist.length - 1]);
    var ind1;
    var dist;
    for (var i = 1; i < commas.length; i++) {
        ind1 = commas[i-1] + 1;
        dist = commas[i] - ind1;
        nameslist.push(rawnames.substr(ind1, dist));
        nameslist[nameslist.length - 1].trim();
        console.log(nameslist[nameslist.length - 1]);
    }

    nameslist.push(rawnames.substr(commas[commas.length-1] + 1));
    console.log(nameslist[nameslist.length - 1]);
    nameslist[nameslist.length - 1].trim();

    return nameslist;
}

function add_str_to_div(string) {
    namesDiv.innerHTML = namesDiv.innerHTML.concat(string);
}

console.log("js loaded");

addBtn.onclick = function() {
    console.log(emailIn.value);
    var string_to_append = "";
    string_to_append = string_to_append.concat("<ul class='names'>");
    string_to_append = string_to_append.concat(emailIn.value);
    console.log("shoulda changed div text");
    emails.push(emailIn.value);
    
    var tempnameslist = parsenames();
    for (var i = 0; i < tempnameslist.length; i++) {
        num_of_names = num_of_names + 1;
        names.push(tempnameslist[i]);
        namesEmails.push(num_of_emails);
        string_to_append = string_to_append.concat("<li>".concat(tempnameslist[i]).concat("</li>"));
    }
    console.log(string_to_append);
    string_to_append = string_to_append.concat("</ul>");
    add_str_to_div(string_to_append);


    num_of_emails = num_of_emails +1;
}

function findname(ind) {
    var works = false;
    hasname[ind] = Math.floor(Math.random() * names.length);
    if (emails[ind] != emails[hasname[ind]]) {
        works = true;
    }
    var gonethruonce = 0;
    while (works == false) {
        console.log(ishad[hasname[ind]]);
        hasname[ind] = hasname[ind] + 1;
        if (hasname[ind] >= names.length) {
            hasname[ind] = 0;
            gonethruonce = 1;
            if (gonethruonce == 1) {
                break;
            }
        }
        if (emails[ind] != emails[hasname[ind]] && ishad[hasname[ind]] == "?") {
            works = true;
            ishad[hasname[ind]] = "";
            console.log("this works");
        }
    }
}


function pickNames() {
    ishad = "?".repeat(names.length).split("");
    for (var i = 0; i < names.length; i++) {
        findname(i);
        console.log(names[i] + " has " + hasname[i]);
    }
}

pickNamesBtn.onclick = function() {
    pickNames();
    namesDiv.innerHTML = "";
    var addstr = "";
    var k = 0;
    for (var i = 0; i < emails.length; i++) {
        add_str_to_div(addstr);
        addstr = "";
        addstr = addstr.concat("<ul>".concat(emails[i]));
        while (namesEmails[k] == i) {
            addstr = addstr.concat("<li>").concat(names[k]);
            addstr = addstr.concat(" has ");
            addstr = addstr.concat(names[hasname[k]]);
            addstr = addstr.concat("</li>");
            k++;
        }
    }
}

