<template>
    <div class="h-full bg-gray-200 dark:bg-gray-900">
        <div class="container mx-auto p-10">
            <header>
                <h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"><span class="text-transparent bg-clip-text bg-gradient-to-r to-[#a8bd3a] from-[#f0f762]">ONS</span> Badges</h1>
                <p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">Generate dynamic ONS themed badges for README's</p>
            </header>

            <main class="py-20">
                <div class="grid grid-cols-10 gap-10">
                    <div class="col-span-6 ">

                        <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Generate a preview</h2>
                        <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-8">
                            <form>
                                <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                                    <div class="w-full">
                                        <label for="left_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Left Text</label>
                                        <input type="text" name="left_text" id="left_text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" required="">
                                    </div>
                                    <div class="w-full">
                                        <label for="right_text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Right Text</label>
                                        <input type="text" name="brand" id="brand" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" required="">
                                    </div>

                                    <div class="sm:col-span-2">
                                        <ColourSelect/>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-span-4 ">
                        <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">SVG Preview</h2>
                        <div class="bg-gray-100 dark:bg-gray-800 rounded-lg p-8">
                            <div class="bg-white rounded-lg p-8">
                                SVG
                            </div>
                        </div>
                    </div>
                </div>
            </main>

        </div>
    </div>
</template>

<script>
import ColourSelect from "@/ColourSelect.vue";

export default {
    components: {ColourSelect},
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
