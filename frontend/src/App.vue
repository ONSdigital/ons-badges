<template>
  <div class="text-gray-100 h-screen p-6 bg-gray-800">
    <div class="grid grid-cols-4 gap-2 w-full">
      <!-- Controls -->
      <div class="col-span-1 p-4 ">
        <!-- Controls -->
        <div class="col-span-1 p-4">
          <h3 class="text-xl mb-4">Enter Text for Left and Right</h3>
          <div>
              <label for="left_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Left text (width: {{leftShift}})</label>
              <input v-model="leftText" type="text" id="left_text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="A" required />
          </div>
          <div class="mt-6">
              <label for="right_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Right text (width: {{rightShift}})</label>
              <input v-model="rightText" type="text" id="right_text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="B" required />
          </div>
          <hr class="my-10">
          <h3 class="text-xl mb-4">Colours</h3>


          <div v-for="(color, index) in colorOptions" :key="index" class="flex items-center mb-4">
            <input type="radio" :id="'color-' + index" v-model="selectedColor" :value="color" class="radio">
            <label :for="'color-' + index" class="ms-2 text-sm font-medium" :style="{color: color.fg}">{{ color.name }}</label>
          </div>




        </div>
      </div>

      <!-- SVG Preview -->
      <div class="col-span-3 bg-white flex justify-center items-center">
        <div class="bg-white">
          <svg :width="newGlobalWidth" height="312px" xmlns="http://www.w3.org/2000/svg">
              <g id="production-pill">
                  <g id="middle">
                      <rect id="background" :x="newBackground" y="0" width="211.717" height="312" style="fill:#fff;"/>
                  </g>
                  <g id="left">
                      <path id="left-shape" :d="newLeft" style="fill:#a8bd3a;"/>
                      <g id="left-text-section">
                        <text x="60.727px" y="219.003px" style="font-family: monospace; font-weight:600;font-size:176.512px;fill:#000000;">
                          {{leftText}}
                        </text>
                      </g>
                  </g>
                  <g id="right">
                      <path id="right-shape" :d="newRight" :fill="selectedColor.bg"/>
                      <g id="right-text-section">
                          <text :x="newRightTextPos" y="219.003px" style="font-family: monospace; font-weight:600;font-size:176.512px;" :fill="selectedColor.fg">
                            {{rightText}}
                          </text>
                      </g>
                  </g>
              </g>
          </svg>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

      // Store text
      leftText: "A",
      rightText: "B",

      charWidth: 109.283,

      // Orignal widths
      originalGlobalWidth: 360, //Pixels
      selectedColor: { name: "Default", bg: "#013B61", fg: "#ffffff" },
      colorOptions: [
        { name: "Default", bg: "#013B61", fg: "#ffffff" },
        { name: "Error", bg: "#D0021B", fg: "#ffffff" },
        { name: "Success", bg: "#0F8243", fg: "#ffffff" },
        { name: "Warning", bg: "#FA6401", fg: "000000" },
        { name: "Gray", bg: "#414042", fg: "#ffffff" }
      ]

    };
  },
  computed: {
    getTextWidth() {
        return (text, font = "176.512px 'monospace'") => {
          return text.length * this.charWidth;
        };
      },

    leftShift() {
      if (!this.leftText){
        return 0;
      }
      return parseInt(this.getTextWidth(this.leftText), 10);
    },
    rightShift() {
      if (!this.rightText){
        return 0;
      }
      return parseInt(this.getTextWidth(this.rightText), 10);
    },

    newBackground()
    {
      const newPos = 74 + this.leftShift;
      return newPos;
    },

    newLeft(){
      const newTop = 171.876 + this.leftShift;
      const newBottom = 9.039 + this.leftShift;
      const newStart = 74 + this.leftShift;
      return `M${newStart},312l-${newBottom},0c-35.877,0 -64.961,-29.084 -64.961,-64.961l0,-182.078c0,-35.877 29.084,-64.961 64.961,-64.961l${newTop},0l-162.837,312Z`;
    },

    newRight()
    {
      const newTop = 9.039 + this.rightShift;
      const newBottom = 171.877 + this.rightShift;
      const newStart = 285.717 + this.leftShift;
      return `M${newStart},0l${newTop},0c35.877,-0 64.961,29.084 64.961,64.961l-0,182.078c-0,35.877 -29.084,64.961 -64.961,64.961l-${newBottom},0l162.838,-312Z`;
    },

    newRightTextPos()
    {
      const originalPos = 272.444;
      return originalPos + this.leftShift;
    },

    newGlobalWidth()
    {
      return this.originalGlobalWidth + this.leftShift + this.rightShift;
    },


  }
};
</script>

<style scoped>
/* Optional: Add custom styling */
</style>
