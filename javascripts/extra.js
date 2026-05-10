document$.subscribe(function () {
  var header = document.querySelector(".md-header");
  var hero = document.querySelector(".mdx-hero");
  var tabs = document.querySelector(".md-tabs");
  if (!header || !hero) return;

  if (tabs) {
    tabs.removeAttribute("hidden");
    tabs.style.display = "block";
    tabs.style.visibility = "visible";
    tabs.style.setProperty("--md-tabs-opacity", "1");

    var tabList = tabs.querySelector(".md-tabs__list");
    if (tabList) {
      tabList.style.display = "flex";
      tabList.style.visibility = "visible";
    }

    var observer = new MutationObserver(function () {
      if (tabs.hasAttribute("hidden")) {
        tabs.removeAttribute("hidden");
      }
      if (tabs.style.display === "none") {
        tabs.style.display = "block";
      }
    });
    observer.observe(tabs, {
      attributes: true,
      attributeFilter: ["hidden", "style"],
    });
  }

  function onScroll() {
    var scrollY = window.scrollY;
    var heroHeight = hero.offsetHeight;
    var headerHeight = header.offsetHeight;

    if (scrollY > heroHeight - headerHeight) {
      header.classList.add("md-header--scrolled");
    } else {
      header.classList.remove("md-header--scrolled");
    }

    // 滚动时淡入tabs
    if (tabs) {
      var fadeEnd = heroHeight * 0.8;
      if (scrollY <= 0) {
        tabs.style.setProperty("--md-tabs-opacity", "1");
      } else if (scrollY >= fadeEnd) {
        tabs.style.setProperty("--md-tabs-opacity", "0");
      } else {
        tabs.style.setProperty(
          "--md-tabs-opacity",
          (1 - scrollY / fadeEnd).toFixed(2),
        );
      }
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
});
