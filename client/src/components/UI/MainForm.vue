<template>
  <input class="input" type="text" />
</template>

<script>
export default {
  name: 'main-form',
  props: {
    modelValue: [String, Number],
  },
  methods: {
    updateInput(event) {
      this.$emit('update:modelValue', event.target.value);
    },
    //:value="modelValue" @input="updateInput"
  },
};
</script>

<style lang="scss">
.input {
  // color: #4dd362;
  background: none;
  border: 1px solid #9c53d5;
}
</style>
