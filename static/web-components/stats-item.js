
class StatsItem extends HTMLElement {
  static get observedAttributes() {
    return ['itemval'];
  }

  constructor() {
    super();
    this.attachShadow({ mode: 'open' });

      const template = document.createElement('template');
      template.innerHTML = `
        <style>
          .wrap{
            display: flex;
            flex-direction: row;
            color: rgb(229 231 235 / var(--tw-text-opacity, 1))
          }
          #label {
            padding-right: 1rem;
          }
        </style>
        <div class="wrap">
          <div id="label"><slot></slot></div>
          <div id="itemval">0</div>
        </div>
      `;

    // Append the template content to the shadow DOM
    this.shadowRoot.appendChild(template.content.cloneNode(true));

    // Reference to the label element
    this.itemval = this.shadowRoot.querySelector('#itemval');
  }

  // Handle attribute changes
  attributeChangedCallback(name, oldValue, newValue) {
    if (name === 'itemval') {
      this.itemval.innerText = newValue;
    }
  }
}

// Register the custom element
customElements.define('stats-item', StatsItem);
