
  class ErrorMoveTracker extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: 'open' });

      // Create the template for the component
      const template = document.createElement('template');
      template.innerHTML = `
         <stats-item itemval='0'>errors: </item-val>
      `;

      // Append the template content to the shadow DOM
      this.shadowRoot.appendChild(template.content.cloneNode(true));

      // Initialize properties
      this.statsItem = this.shadowRoot.querySelector('stats-item');
    }

    // Define methods
    setMoves(m) {
      this.statsItem.setAttribute('itemval', m);
    }

    reset() {
      this.statsItem.setAttribute('itemval', 0);
    }

    getMoves() {
      return this.moves;
    }
  }

  // Register the custom element
  customElements.define('error-move-tracker', ErrorMoveTracker);
