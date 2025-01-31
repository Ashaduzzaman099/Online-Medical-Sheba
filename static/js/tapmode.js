function openTab(evt, tabName) {
  // Get all elements with class="tab-content" and hide them
  let tabContent = document.getElementsByClassName("tab-content");
  for (let i = 0; i < tabContent.length; i++) {
    tabContent[i].style.display = "none";
  }

  // Get all elements with class="tab-link" and remove the class "active"
  let tabLinks = document.getElementsByClassName("tab-link");
  for (let i = 0; i < tabLinks.length; i++) {
    tabLinks[i].className = tabLinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// By default, open the first tab
document.addEventListener("DOMContentLoaded", function () {
  document.getElementsByClassName("tab-content")[0].style.display = "block";
});
