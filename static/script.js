document.getElementById("searchForm").addEventListener("submit", function () {
    document.getElementById("loading-spinner").style.display = "flex";
    let query = document.getElementById("query").value;
    let searches = JSON.parse(localStorage.getItem("recent_searches") || "[]");
    searches.unshift(query);
    searches = searches.slice(0, 5);
    localStorage.setItem("recent_searches", JSON.stringify(searches));
  });
  
  document.getElementById("viewFavourites").addEventListener("click", function () {
    loadFavourites();
    document.getElementById("favouritesModal").style.display = "block";
  });
  document.getElementById("closeFavourites").addEventListener("click", function () {
    document.getElementById("favouritesModal").style.display = "none";
  });
  
  document.getElementById("recentSearchesBtn").addEventListener("click", function () {
    loadRecentSearches();
    document.getElementById("recentSearchesModal").style.display = "block";
  });
  document.getElementById("closeRecentSearches").addEventListener("click", function () {
    document.getElementById("recentSearchesModal").style.display = "none";
  });
  
  window.addEventListener("click", function (event) {
    if (event.target === document.getElementById("favouritesModal")) {
      document.getElementById("favouritesModal").style.display = "none";
    }
    if (event.target === document.getElementById("recentSearchesModal")) {
      document.getElementById("recentSearchesModal").style.display = "none";
    }
  });
  
  document.addEventListener("click", function(e) {
    if (e.target && e.target.classList.contains("fav-button")) {
      let title = e.target.getAttribute("data-title");
      let link = e.target.getAttribute("data-link");
      addToFavourites(title, link);
    }
  });
  
  function addToFavourites(title, link) {
    let favs = JSON.parse(localStorage.getItem("favourites") || "[]");
    if (!favs.some(item => item.title === title && item.link === link)) {
      favs.push({ title, link });
      localStorage.setItem("favourites", JSON.stringify(favs));
      alert("Added to Favourites!");
    } else {
      alert("This product is already in your favourites.");
    }
  }
  
  function loadFavourites() {
    let favs = JSON.parse(localStorage.getItem("favourites") || "[]");
    const list = document.getElementById("favouritesList");
    list.innerHTML = "";
    if (favs.length === 0) {
      list.innerHTML = "<li>No favourites yet.</li>";
    } else {
      favs.forEach(function (item) {
        let li = document.createElement("li");
        li.innerHTML = `<a href="${item.link}" target="_blank">${item.title}</a>`;
        list.appendChild(li);
      });
    }
  }
  
  function loadRecentSearches() {
    let searches = JSON.parse(localStorage.getItem("recent_searches") || "[]");
    const list = document.getElementById("recentSearchesList");
    list.innerHTML = "";
    if (searches.length === 0) {
      list.innerHTML = "<li>No recent searches yet.</li>";
    } else {
      searches.forEach(function (search) {
        let li = document.createElement("li");
        li.innerHTML = `<a href="#" onclick="setQueryAndSearch('${search.replace(/'/g, "\\'")}'); return false;">${search}</a>`;
        list.appendChild(li);
      });
    }
  }
  
  function setQueryAndSearch(query) {
    document.getElementById("query").value = query;
    document.getElementById("recentSearchesModal").style.display = "none";
  }
  