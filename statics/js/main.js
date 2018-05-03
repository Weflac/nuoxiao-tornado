/**
 * Created by Bin on 2018/2/9.
 */

  !function(t, e) {
    "object" == typeof exports && "object" == typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define([], e) : "object" == typeof exports ? exports.inView = e() : t.inView = e()
  }
  (this, function() {
      return function(t) {
        function e(i) {
          if (n[i]) return n[i].exports;
          var o = n[i] = {
            exports: {},
            id: i,
            loaded: !1
          };
          return t[i].call(o.exports, o, o.exports, e),
            o.loaded = !0,
            o.exports
        }
        var n = {};
        return e.m = t,
          e.c = n,
          e.p = "",
          e(0)
      } ([function(t, e, n) {
        "use strict";
        var i = function(t) {
          return t && t.__esModule ? t: {
            default:
            t
          }
        } (n(2));
        t.exports = i.
          default
      },
        function(t, e) {
          t.exports = function(t) {
            var e = typeof t;
            return null != t && ("object" == e || "function" == e)
          }
        },
        function(t, e, n) {
          "use strict";
          function i(t) {
            return t && t.__esModule ? t: {
              default:
              t
            }
          }
          Object.defineProperty(e, "__esModule", {
            value: !0
          });
          var o = i(n(9)),
            r = i(n(3)),
            u = n(4);
          e.
            default = function() {
            if ("undefined" != typeof window) {
              var t = ["scroll", "resize", "load"],
                e = {
                  history: []
                },
                n = {
                  offset: {},
                  threshold: 0,
                  test: u.inViewport
                },
                i = (0, o.
                  default)(function() {
                    e.history.forEach(function(t) {
                      e[t].check()
                    })
                  },
                  100);
              t.forEach(function(t) {
                return addEventListener(t, i)
              }),
              window.MutationObserver && addEventListener("DOMContentLoaded",
                function() {
                  new MutationObserver(i).observe(document.body, {
                    attributes: !0,
                    childList: !0,
                    subtree: !0
                  })
                });
              var s = function(t) {
                if ("string" == typeof t) {
                  var i = [].slice.call(document.querySelectorAll(t));
                  return e.history.indexOf(t) > -1 ? e[t].elements = i: (e[t] = (0, r.
                    default)(i, n), e.history.push(t)),
                    e[t]
                }
              };
              return s.offset = function(t) {
                if (void 0 === t) return n.offset;
                var e = function(t) {
                  return "number" == typeof t
                };
                return ["top", "right", "bottom", "left"].forEach(e(t) ?
                  function(e) {
                    return n.offset[e] = t
                  }: function(i) {
                    return e(t[i]) ? n.offset[i] = t[i] : null
                  }),
                  n.offset
              },
                s.threshold = function(t) {
                  return "number" == typeof t && t >= 0 && t <= 1 ? n.threshold = t: n.threshold
                },
                s.test = function(t) {
                  return "function" == typeof t ? n.test = t: n.test
                },
                s.is = function(t) {
                  return n.test(t, n)
                },
                s.offset(0),
                s
            }
          } ()
        },
        function(t, e) {
          "use strict";
          function n(t, e) {
            if (! (t instanceof e)) throw new TypeError("Cannot call a class as a function")
          }
          Object.defineProperty(e, "__esModule", {
            value: !0
          });
          var i = function() {
              function t(t, e) {
                for (var n = 0; n < e.length; n++) {
                  var i = e[n];
                  i.enumerable = i.enumerable || !1,
                    i.configurable = !0,
                  "value" in i && (i.writable = !0),
                    Object.defineProperty(t, i.key, i)
                }
              }
              return function(e, n, i) {
                return n && t(e.prototype, n),
                i && t(e, i),
                  e
              }
            } (),
            o = function() {
              function t(e, i) {
                n(this, t),
                  this.options = i,
                  this.elements = e,
                  this.current = [],
                  this.handlers = {
                    enter: [],
                    exit: []
                  },
                  this.singles = {
                    enter: [],
                    exit: []
                  }
              }
              return i(t, [{
                key: "check",
                value: function() {
                  var t = this;
                  return this.elements.forEach(function(e) {
                    var n = t.options.test(e, t.options),
                      i = t.current.indexOf(e),
                      o = i > -1,
                      r = n && !o,
                      u = !n && o;
                    r && (t.current.push(e), t.emit("enter", e)),
                    u && (t.current.splice(i, 1), t.emit("exit", e))
                  }),
                    this
                }
              },
                {
                  key: "on",
                  value: function(t, e) {
                    return this.handlers[t].push(e),
                      this
                  }
                },
                {
                  key: "once",
                  value: function(t, e) {
                    return this.singles[t].unshift(e),
                      this
                  }
                },
                {
                  key: "emit",
                  value: function(t, e) {
                    for (; this.singles[t].length;) this.singles[t].pop()(e);
                    for (var n = this.handlers[t].length; --n > -1;) this.handlers[t][n](e);
                    return this
                  }
                }]),
                t
            } ();
          e.
            default = function(t, e) {
            return new o(t, e)
          }
        },
        function(t, e) {
          "use strict";
          Object.defineProperty(e, "__esModule", {
            value: !0
          }),
            e.inViewport = function(t, e) {
              var n = t.getBoundingClientRect(),
                i = n.top,
                o = n.right,
                r = n.bottom,
                u = n.left,
                s = n.width,
                f = n.height,
                c = {
                  t: r,
                  r: window.innerWidth - u,
                  b: window.innerHeight - i,
                  l: o
                },
                a = {
                  x: e.threshold * s,
                  y: e.threshold * f
                };
              return c.t > e.offset.top + a.y && c.r > e.offset.right + a.x && c.b > e.offset.bottom + a.y && c.l > e.offset.left + a.x
            }
        },
        function(t, e) { (function(e) {
          var n = "object" == typeof e && e && e.Object === Object && e;
          t.exports = n
        }).call(e,
          function() {
            return this
          } ())
        },
        function(t, e, n) {
          var i = n(5),
            o = "object" == typeof self && self && self.Object === Object && self,
            r = i || o || Function("return this")();
          t.exports = r
        },
        function(t, e, n) {
          var i = n(1),
            o = n(8),
            r = n(10),
            u = "Expected a function",
            s = Math.max,
            f = Math.min;
          t.exports = function(t, e, n) {
            function c(e) {
              var n = m,
                i = y;
              return m = y = void 0,
                j = e,
                g = t.apply(i, n)
            }
            function a(t) {
              return j = t,
                b = setTimeout(p, e),
                k ? c(t) : g
            }
            function l(t) {
              var n = t - j,
                i = e - (t - w);
              return O ? f(i, x - n) : i
            }
            function d(t) {
              var n = t - w,
                i = t - j;
              return void 0 === w || n >= e || n < 0 || O && i >= x
            }
            function p() {
              var t = o();
              return d(t) ? h(t) : void(b = setTimeout(p, l(t)))
            }
            function h(t) {
              return b = void 0,
                T && m ? c(t) : (m = y = void 0, g)
            }
            function v() {
              var t = o(),
                n = d(t);
              if (m = arguments, y = this, w = t, n) {
                if (void 0 === b) return a(w);
                if (O) return b = setTimeout(p, e),
                  c(w)
              }
              return void 0 === b && (b = setTimeout(p, e)),
                g
            }
            var m, y, x, g, b, w, j = 0,
              k = !1,
              O = !1,
              T = !0;
            if ("function" != typeof t) throw new TypeError(u);
            return e = r(e) || 0,
            i(n) && (k = !!n.leading, O = "maxWait" in n, x = O ? s(r(n.maxWait) || 0, e) : x, T = "trailing" in n ? !!n.trailing: T),
              v.cancel = function() {
                void 0 !== b && clearTimeout(b),
                  j = 0,
                  m = w = y = b = void 0
              },
              v.flush = function() {
                return void 0 === b ? g: h(o())
              },
              v
          }
        },
        function(t, e, n) {
          var i = n(6);
          t.exports = function() {
            return i.Date.now()
          }
        },
        function(t, e, n) {
          var i = n(7),
            o = n(1),
            r = "Expected a function";
          t.exports = function(t, e, n) {
            var u = !0,
              s = !0;
            if ("function" != typeof t) throw new TypeError(r);
            return o(n) && (u = "leading" in n ? !!n.leading: u, s = "trailing" in n ? !!n.trailing: s),
              i(t, e, {
                leading: u,
                maxWait: e,
                trailing: s
              })
          }
        },
        function(t, e) {
          t.exports = function(t) {
            return t
          }
        }])
    }),
  function(t) {
    t(document).ready(function() {
      setTimeout(function() {
          t(".loader").addClass("hidden").delay(200).remove(),
            t(".slide-in").each(function() {
              t(this).addClass("visible")
            })
        },
        1900),
        inView(".ll-image").on("enter",
          function(t) {
            void 0 !== t.dataset.imgSrc && t.setAttribute("src", t.dataset.imgSrc)
          }),
        t('[data-toggle="popover"]').popover(),
        t('[data-toggle="tooltip"]').tooltip(),
        t(".example a").click(function(t) {
          "#" === t.target.getAttribute("href") && t.preventDefault()
        }),
        t("#scroll-to-content").click(function(e) {
          e.preventDefault(),
          void 0 !== e.target.dataset.scrollTo && t("html, body").animate({
              scrollTop: t(e.target.dataset.scrollTo).offset().top - 100
            },
            1e3)
        });
      var e = t(".sticky-header");
      inView(".page-content").on("enter",
        function() {
          e.addClass("active")
        }).on("exit",
        function() {
          e.removeClass("active")
        }),
        t("#slider-example-1").customSlider({
          start: [20, 80],
          range: {
            min: 0,
            max: 100
          },
          connect: !0
        }),
        t("#slider-example-2").customSlider({
          start: [20, 80],
          range: {
            min: 0,
            max: 100
          },
          connect: !0,
          tooltips: !0
        }),
        t("#slider-example-3").customSlider({
          start: [20, 80],
          range: {
            min: 0,
            max: 100
          },
          connect: !0,
          tooltips: !0,
          pips: {
            mode: "positions",
            values: [0, 25, 50, 75, 100],
            density: 5
          }
        }),
        t("#datepicker-example-1").datepicker({}),
        t("#datepicker-example-2").datepicker({})
    })
  } (jQuery);
