/* Auto-advance a Marp bespoke HTML deck forever (booth loop).
 *
 * Query params: ?interval=SECONDS (default 10), ?pause=1 to start paused.
 * Click or press Space to pause/resume. Meant for `chromium --kiosk`.
 */
(function () {
  var params = new URLSearchParams(location.search);
  var interval = (parseFloat(params.get("interval")) || 10) * 1000;
  var paused = params.get("pause") === "1";
  var total = document.querySelectorAll("svg[data-marpit-svg]").length;

  function key(k) {
    document.dispatchEvent(new KeyboardEvent("keydown", { key: k, code: k, bubbles: true }));
  }
  function current() {
    var n = parseInt(location.hash.replace("#", ""), 10);
    return isNaN(n) ? 1 : n;
  }
  function tick() {
    if (paused) return;
    key(current() >= total ? "Home" : "ArrowRight");
    document.title = "slide " + current() + "/" + total;
  }

  document.addEventListener("click", function () { paused = !paused; });
  document.addEventListener("keydown", function (e) {
    if (e.isTrusted && e.key === " ") paused = !paused;
  });
  setInterval(tick, interval);
})();
