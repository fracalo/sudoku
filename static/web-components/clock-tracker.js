
  class ClockTracker extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: 'open' });
      this.time = 0;

      // Create the template for the component
      const template = document.createElement('template');
      template.innerHTML = `
         <stats-item itemval='0'>clock: </stats-item>
      `;

      // Append the template content to the shadow DOM
      this.shadowRoot.appendChild(template.content.cloneNode(true));

      // Initialize properties
      this.statsItem = this.shadowRoot.querySelector('stats-item');
    }

    setDuration(m) {
        this._duration = m * 1000
        this.statsItem.setAttribute('itemval', this.getTime());
    }

    stopClock() {
      clearInterval(this.interval);
      this.interval = null;
      this._stopFlag = true
    }

    calcTime = () => {
        if (this._stopFlag) {
          this._stopFlag = undefined
          this._startClock = undefined 
          return 
        }
        this._duration = Date.now() - this._startClock

        this.statsItem.setAttribute('itemval', this.getTime());

        setTimeout(this.calcTime, 200)
    }

    startClock() {
      this._duration = 0 
      this._startClock = Date.now()
      requestAnimationFrame(this.calcTime)
    }

    getDuration() {
      return this._duration / 1000
    }

    getTime() {
      const t = Math.floor(this._duration / 1000)
      let minutes = Math.floor(t / 60);
      let seconds = t % 60;
      let millis = this._duration % 1000

      let minStr = minutes.toString().padStart(2, '0')
      let secStr = seconds.toString().padStart(2, '0')
      let milStr = millis.toString().padStart(3, '0')

      return `${minStr}:${secStr}:${milStr}`
    }
  }

  customElements.define('clock-tracker', ClockTracker);
