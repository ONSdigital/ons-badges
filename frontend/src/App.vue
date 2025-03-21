<template>
    <div class="flex min-h-screen h-full flex-col bg-gray-200 dark:bg-gray-900">
        <div class="container mx-auto p-4 sm:p-10 flex-1">
            <header>
                <h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"><span class="text-transparent bg-clip-text bg-gradient-to-r to-[#206095] dark:to-[#a8bd3a] from-[#003c57] dark:from-[#f0f762]">ONS</span> Badges</h1>
                <p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">Generate dynamic ONS themed badges for README's</p>
            </header>

            <main class="py-10 sm:py-20">
                <div class="grid grid-cols-1 md:grid-cols-10 gap-10">
                    <div class="md:col-span-6">

                        <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Generate a preview</h2>
                        <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-8">
                            <form>
                                <div class="grid gap-4 md:grid-cols-2 md:gap-6">
                                    <div class="w-full">
                                        <label for="left_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Left Text</label>
                                        <input v-model="leftText" type="text" name="left_text" id="left_text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" required="">
                                    </div>
                                    <div class="w-full">
                                        <label for="right_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Right Text</label>
                                        <input v-model="rightText" type="text" name="brand" id="brand" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" required="">
                                    </div>
                                    <div class="md:col-span-2">
                                        <ColourSelect @update:selected="handleColorSelection"/>
                                    </div>
                                    <!-- Link preview -->
                                    <div class="md:col-span-2 overflow-hidden">
                                        <div class="mb-2">
                                            <p class="block text-sm font-medium text-gray-900 dark:text-white">Api Link</p>
                                            <small class="text-gray-700 dark:text-gray-200">Use this link to call the api to generate this badge</small>
                                        </div>

                                        <div class="overflow-scroll whitespace-nowrap">
                                            <a :href="apiLink" target="_blank" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">
                                            {{ apiLink }}
                                            </a>
                                        </div>


                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="md:col-span-4 ">
                        <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">SVG Preview</h2>
                        <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-8">
                            <div class="bg-white rounded-lg p-10 text-center overflow-scroll">
                                <svg :width="newGlobalWidth" height="40px" xmlns="http://www.w3.org/2000/svg"  style="transform: scale(2); transform-origin: top left;">
                                    <g id="ons-badge">
                                        <g id="middle">
                                            <rect id="background" :x="newBackgroundX" y="0" width="13.572" height="20" style="fill:#fff;"/>
                                        </g>
                                        <g id="left">
                                            <path id="left-shape" :d="newLeftShape" style="fill:#a8bd3a;"/>
                                            <g id="left-text-section">
                                                <text x="3.893px" y="14.039px" style="font-family: monospace; font-weight:400;font-size:11.315px;fill:#000000;">
                                                    {{ leftText }}
                                                </text>
                                            </g>
                                        </g>
                                        <g id="right">
                                            <path id="right-shape" :d="newRightShape" :fill="selectedColor.bg"/>
                                            <g id="right-text-section">
                                                <text :x="newRightTextX" y="14.039px" style="font-family: monospace; font-weight:400;font-size:11.315px;" :fill="selectedColor.fg">
                                                    {{ rightText }}
                                                </text>
                                            </g>
                                        </g>
                                    </g>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </main>

        </div>
        <Footer />
    </div>
</template>

<script>
import ColourSelect from "@/ColourSelect.vue";
import Footer from "@/Footer.vue";

export default {
    components: {Footer, ColourSelect},
    data() {
        return {

            // Store text
            leftText: "A",
            rightText: "B",

            charWidth: 7.5,
            selectedColor: { name: "standard", bg: "#013B61", fg: "#ffffff" },

        };
    },
    methods: {
        handleColorSelection(colour) {
            this.selectedColor = colour
        }
    },
    computed: {

        apiLink() {
            return `/api/badge/custom?left=${this.leftText}&right=${this.rightText}&colour=${this.selectedColor.name}`;
        },

        getTextWidth() {
            return (text) => {
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

        newBackgroundX()
        {
            return 4.744 + this.leftShift;
        },

        newLeftShape() {
            const newTop = 11.018 + this.leftShift;
            const newBottom = 0.58 + this.leftShift;
            const newStart = 4.744 + this.leftShift;

            return `M${newStart},20l-${newBottom},-0c-2.3,-0 -4.164,-1.864 -4.164,-4.164l0,-11.672c0,-2.3 1.864,-4.164 4.164,-4.164l${newTop},0l-10.438,20Z`;
        },


        newRightShape() {
            const newTop = 0.58 + this.rightShift;
            const newBottom = 11.018 + this.rightShift;
            const newStart = 18.315 + this.leftShift;

            return `M${newStart},0l${newTop},0c2.299,-0 4.164,1.864 4.164,4.164l-0,11.672c-0,2.3 -1.865,4.164 -4.164,4.164l-${newBottom},-0l10.438,-20Z`;
        },


        newRightTextX()
        {
            const originalPos = 20.464 ;
            return originalPos + this.leftShift;
        },

        newGlobalWidth()
        {
            return 24 + this.leftShift + this.rightShift;
        },


    }
};
</script>

