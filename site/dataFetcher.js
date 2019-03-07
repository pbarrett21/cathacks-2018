active_index = 0

function testFunc(newIndex)
{
  active_index = parseInt(newIndex);
}

function formatSiteContent(content)
{
  siteContentDiv = document.getElementById("siteContent");

  // Split the string into different lists
  elementList = [];
  splitLists = content.split(";");
  splitLists.pop();
  for (item in splitLists)
  {
    newElement = splitLists[item].split(",");
    newElement[1] = newElement[1].substring(0, newElement[1].length)
    elementList.push(newElement);
  }

  // Create each item from the list
  htmlString = "<ul class=\"collapsible\">"
  var num_titles = 0;

  for (i in elementList)
  {
    if (elementList[i][0] === "title")
    {
      if (num_titles > 0)
        htmlString += "</div></li>"
      if (active_index == num_titles)
        htmlString += "<li class=\"active\" onclick=\"testFunc(" + num_titles.toString() + ")\">"
      else
        htmlString += "<li onclick=\"testFunc(" + num_titles.toString() + ")\">"
      htmlString += "<div class=\"collapsible-header\"><h2>" + elementList[i][1] + "</h2></div><div class=\"collapsible-body\">";
      num_titles++;
    }
    if (elementList[i][0] === "question")
    {
      htmlString += "<p style=\"font-weight: bold\">Question: " + elementList[i][1] + "</p>";
    }
    if (elementList[i][0] === "answer")
    {
      htmlString += "<p>" + elementList[i][1] + "</p>";
    }
    if (elementList[i][0] === "section")
    {
      htmlString += "<h3>" + elementList[i][1] + "</h3>";
    }
    if (elementList[i][0] === "note")
    {
      htmlString += "<p>Note: " + elementList[i][1] + "</p>";
    }
  }

  // Yay cheap workarounds
  htmlString += "</div></li></ul>"

  siteContentDiv.innerHTML = htmlString

  // Init the collapsibles
  M.AutoInit()
}

function makeSiteRequest()
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200)
    {
      formatSiteContent(xhttp.responseText);
    }
  };

  xhttp.open("GET", "http://www.acheapdomain.win:8000", true);
  xhttp.send();
}

makeSiteRequest()
window.setInterval(makeSiteRequest, 500);
