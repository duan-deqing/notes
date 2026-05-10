// 文件位置: docs/javascripts/mermaid-init.js

(function () {
  const themeVariablesLight = {
    primaryColor: "#4caf50",
    primaryTextColor: "#ffffff",
    lineColor: "#b0bec5",
    secondaryColor: "#f5f5f5",
    tertiaryColor: "#fafafa",
    noteBkgColor: "#fff9c4",
    noteTextColor: "#333333",
  };

  const themeVariablesDark = {
    primaryColor: "#81c784",
    primaryTextColor: "#000000",
    lineColor: "#4a4a4a",
    secondaryColor: "#2b2b2b",
    tertiaryColor: "#1e1e1e",
    noteBkgColor: "#f9a825",
    noteTextColor: "#ffffff",
  };

  function getMermaidThemeVariables() {
    const isDarkMode =
      document.body.getAttribute("data-md-color-scheme") === "slate";
    return isDarkMode ? themeVariablesDark : themeVariablesLight;
  }

  function initializeMermaid() {
    if (typeof mermaid === "undefined") return;
    mermaid.initialize({
      startOnLoad: false,
      securityLevel: "loose",
      theme: "base",
      themeVariables: getMermaidThemeVariables(),
    });
    // 重新渲染所有未渲染的图表
    document
      .querySelectorAll(".mermaid:not([data-processed])")
      .forEach(async (element) => {
        await mermaid.run({ nodes: [element] });
      });
  }

  // 监听 Material 主题切换事件
  const observer = new MutationObserver(() => {
    if (typeof mermaid !== "undefined") {
      initializeMermaid();
    }
  });
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });

  // 页面加载时初始化
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeMermaid);
  } else {
    initializeMermaid();
  }
})();
