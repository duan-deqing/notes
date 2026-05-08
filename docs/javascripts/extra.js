document$.subscribe(function () {
  var header = document.querySelector(".md-header");
  var hero = document.querySelector(".mdx-hero");
  var tabs = document.querySelector(".md-tabs");
  if (!header || !hero) return;

  function onScroll() {
    if (window.scrollY > hero.offsetHeight - header.offsetHeight) {
      header.classList.add("md-header--scrolled");
      if (tabs) {
        tabs.classList.add("md-tabs--scrolled");
        tabs.style.position = "fixed";
        tabs.style.top = header.offsetHeight + "px";
      }
    } else {
      header.classList.remove("md-header--scrolled");
      if (tabs) {
        tabs.classList.remove("md-tabs--scrolled");
        tabs.style.position = "absolute";
        tabs.style.top = "48px";
      }
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
});
