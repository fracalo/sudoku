
  class MoveTracker extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: 'open' });

      // Create the template for the component
      const template = document.createElement('template');
      template.innerHTML = `
         <stats-item itemval='0'>moves: </item-val>
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

    //attributeChangedCallback(name, oldValue, newValue) {
    //  if (name === 'moves') {
    //    this.statsItem.setAttribute('itemval', newValue);
    //  }
    //}
  }

  // Register the custom element
  customElements.define('move-tracker', MoveTracker);
