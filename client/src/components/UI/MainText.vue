<template>
  <div class="link" :class="fontFamily" :style="styleObject">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'main-text',
  props: {
    fontFamily: String,
    fontSize: Number,
    fontStyle: String,
    fontWeight: Number,
    color: String,
  },
  data() {
    return {
      styleObject: {
        fontSize: (this.fontSize ?? 20) + 'px',
        fontStyle: this.fontStyle ?? 'normal',
        fontWeight: this.fontWeight ?? 400,
        color: this.color ?? '#000000',
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.montSer {
  font-family: 'Montserrat', sans-serif;
}
</style>
