<template>
    <div class="bg-gray-100 rounded-lg p-4">
        <fieldset>
            <legend class="block mb-2 text-sm font-medium text-gray-900">Choose a colour</legend>
            <RadioGroup v-model="colour" class="mt-6 flex items-center gap-x-3">

                <div class="flex flex-col items-center gap-y-1">
                    <RadioGroupOption v-slot="{ checked }" value="default">
                        <label
                            aria-label="default"
                            :class="[
                    'relative flex cursor-pointer items-center justify-center rounded-full p-1 text-[#003c57] ring-current focus:outline-hidden',
                      checked && 'ring-3 ring-offset-1'
                ]"
                        >
                            <input type="radio" name="color-choice" value="Pink" class="sr-only">
                            <span aria-hidden="true" class="size-8 rounded-full border border-black/10 bg-current"></span>
                        </label>
                    </RadioGroupOption>
                    <small class="text-gray-900  text-center w-full">Default</small>
                </div>

                <div class="flex flex-col items-center gap-y-1">
                    <RadioGroupOption v-slot="{ checked }" value="danger">
                        <label
                            aria-label="Danger"
                            :class="[
                    'relative flex cursor-pointer items-center justify-center rounded-full p-1 text-[#d0021b] ring-current focus:outline-hidden',
                      checked && 'ring-3 ring-offset-1'
                ]"
                        >
                            <input type="radio" name="color-choice" value="Pink" class="sr-only">
                            <span aria-hidden="true" class="size-8 rounded-full border border-black/10 bg-current"></span>
                        </label>
                    </RadioGroupOption>
                    <small class="text-gray-900  text-center w-full">Danger</small>
                </div>

                <div class="flex flex-col items-center gap-y-1">
                    <RadioGroupOption v-slot="{ checked }" value="success">
                        <label
                            aria-label="Success"
                            :class="[
                    'relative flex cursor-pointer items-center justify-center rounded-full p-1 text-[#0f8243] ring-current focus:outline-hidden',
                      checked && 'ring-3 ring-offset-1'
                ]"
                        >
                            <input type="radio" name="color-choice" value="Pink" class="sr-only">
                            <span aria-hidden="true" class="size-8 rounded-full border border-black/10 bg-current"></span>
                        </label>
                    </RadioGroupOption>
                    <small class="text-gray-900  text-center w-full">Success</small>
                </div>

                <div class="flex flex-col items-center gap-y-1">
                    <RadioGroupOption v-slot="{ checked }" value="warning">
                        <label
                            aria-label="Warning"
                            :class="[
                    'relative flex cursor-pointer items-center justify-center rounded-full p-1 text-[#fa6401] ring-current focus:outline-hidden',
                      checked && 'ring-3 ring-offset-1'
                ]"
                        >
                            <input type="radio" name="color-choice" value="Pink" class="sr-only">
                            <span aria-hidden="true" class="size-8 rounded-full border border-black/10 bg-current"></span>
                        </label>
                    </RadioGroupOption>
                    <small class="text-gray-900  text-center w-full">Warning</small>
                </div>
            </RadioGroup>
        </fieldset>
    </div>

</template>

<script setup>
  import { ref } from 'vue'
  import {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupOption,
  } from '@headlessui/vue'

  const colour = ref('default')
</script>
