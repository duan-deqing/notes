// docs/javascripts/mathjax.js
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]], // (1) 行内公式识别符
    displayMath: [["\\[", "\\]"]], // (2) 块级公式识别符
    processEscapes: true, // (3) 允许使用 \\(...\\) 和 \\[...\\]
    processEnvironments: true,
    tags: "ams", // (4) 自动给公式编号
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
    enableMenu: false, // 👈 添上这一行，即可全局禁用右键菜单
  },
};

document$.subscribe(() => {
  // (5) 配合 Instant Navigation
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
