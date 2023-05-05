window.cookieconsent.initialise({
  palette: {
    popup: {
      background: "#000"
    },
    button: {
      background: "#0c6c8a"
    }
  },
  name: "consentcookie",
  type: "opt-in",
  domain: "https://recess-eu-project.github.io/",
  secure: true,
  content: {
    "href": "https://recess-eu-project.github.io/privacy",
  },
  onInitialise: function (status) {
    var type = this.options.type;
    var didConsent = this.hasConsented();
    if (type == 'opt-in' && didConsent) {
      // enable cookies
      loadGAonConsent();
    }
    if (type == 'opt-out' && !didConsent) {
      // disable cookies
    }
  },
  onStatusChange: function(status, chosenBefore) {
    var type = this.options.type;
    var didConsent = this.hasConsented();
    if (type == 'opt-in' && didConsent) {
      // enable cookies
      loadGAonConsent();
    }
    if (type == 'opt-out' && !didConsent) {
      // disable cookies
    }
  },
  onRevokeChoice: function() {
    var type = this.options.type;
    if (type == 'opt-in') {
      // disable cookies
    }
    if (type == 'opt-out') {
      // enable cookies
      loadGAonConsent();
    }
  }
});
console.log(window.cookieconsent);