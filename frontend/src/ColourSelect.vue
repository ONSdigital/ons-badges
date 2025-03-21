<template>
        <fieldset>
            <legend class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Choose a colour</legend>
            <div class="bg-gray-100 rounded-lg p-4">
                <RadioGroup v-model="selectedColour" class="flex flex-wrap gap-4" @update:modelValue="emitSelection">
                <div v-for="(option, index) in colorOptions" :key="index" class="flex flex-col items-center gap-y-1">
                    <RadioGroupOption v-slot="{ checked }" :value="option">
                        <label
                            :aria-label="option.name"
                            :class="[
                                'relative flex cursor-pointer items-center justify-center rounded-full p-0.5 ring-current focus:outline-hidden',
                                option.classes,
                                checked && 'ring-3 ring-offset-1'
                            ]"
                        >
                            <input type="radio" name="color-choice" :value="option.name" class="sr-only">
                            <span aria-hidden="true" class="size-8 rounded-full border border-black/10 bg-current"></span>
                        </label>
                    </RadioGroupOption>
                    <small class="text-gray-900 text-center w-full">{{ option.name }}</small>
                </div>
            </RadioGroup>
            </div>
        </fieldset>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
import { RadioGroup, RadioGroupOption } from '@headlessui/vue'

const emit = defineEmits(['update:selected'])

const colorOptions = [
    { name: "standard", bg: "#013B61", fg: "#ffffff", classes: "text-ons-default" },
    { name: "error", bg: "#D0021B", fg: "#ffffff", classes: "text-ons-danger" },
    { name: "success", bg: "#0F8243", fg: "#ffffff", classes: "text-ons-success" },
    { name: "warning", bg: "#FA6401", fg: "#000000", classes: "text-ons-warning" },
    { name: "grey", bg: "#414042", fg: "#ffffff", classes: "text-ons-grey" }
]

const selectedColour = ref(colorOptions[0])

const emitSelection = (value) => {
    emit('update:selected', value)
}
</script>
