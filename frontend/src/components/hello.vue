<script>
import Counter from "./counter"

export default {
    components: {Counter},
}
</script>

<template>
  <div>
    <p>Hello, World!</p>
    <counter/>

    <form action="/api/add" method="post">
      <label for="name">名前：</label><input type="text" name="name" />
      <label for="birthday">誕生日：</label><input type="date" name="birthday" />
      <input type="submit" name="submit" />
    </form>
  </div>
</template>

<style lang="scss">
p {
    font-size: 24px;
}
</style>